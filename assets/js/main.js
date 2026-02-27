const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

const copyIconSvg = `
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
  <path fill="currentColor" fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/>
</svg>`

const copyText = async (text) => {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text)
    return
  }

  const textarea = document.createElement('textarea')
  textarea.value = text
  textarea.setAttribute('readonly', '')
  textarea.style.position = 'fixed'
  textarea.style.left = '-9999px'
  document.body.appendChild(textarea)
  textarea.select()
  const copied = document.execCommand('copy')
  document.body.removeChild(textarea)
  if (!copied) {
    throw new Error('Copy command failed')
  }
}

const setupCodeCopyButtons = () => {
  const blocks = document.querySelectorAll('.highlight')
  blocks.forEach((block) => {
    if (block.querySelector('.code-copy-btn')) {
      return
    }

    const code = block.querySelector('pre > code')
    if (!code) {
      return
    }

    const button = document.createElement('button')
    button.type = 'button'
    button.className = 'code-copy-btn'
    button.innerHTML = copyIconSvg
    button.setAttribute('aria-label', 'Copy code block')
    button.title = 'Copy'

    button.addEventListener('click', async () => {
      const text = code.innerText.replace(/\n$/, '')
      try {
        await copyText(text)
        button.setAttribute('aria-label', 'Copied')
        button.title = 'Copied'
        button.classList.add('is-copied')
      } catch (err) {
        button.setAttribute('aria-label', 'Copy failed')
        button.title = 'Copy failed'
      }

      window.setTimeout(() => {
        button.setAttribute('aria-label', 'Copy code block')
        button.title = 'Copy'
        button.classList.remove('is-copied')
      }, 1400)
    })

    block.appendChild(button)
  })
}

const setupMultiScroller = (carousel) => {
  const maxPerSlide = parseInt(carousel.getAttribute('data-max-per-slide') || carousel.getAttribute('data-per-slide'), 10) || 1
  const itemMinWidth = Math.max(1, parseInt(carousel.getAttribute('data-item-min-width'), 10) || 220)
  const isResponsive = carousel.getAttribute('data-responsive') === 'true'
  const intervalMs = parseInt(carousel.getAttribute('data-interval'), 10) || 5000

  const viewport = carousel.querySelector('.carousel-multi-viewport')
  const track = carousel.querySelector('.carousel-multi-track')
  if (!viewport || !track) {
    return
  }

  const originalItems = Array.from(track.children)
  if (!originalItems.length) {
    return
  }

  let index = 0
  let isAnimating = false
  let currentPerSlide = 0

  const getPerSlide = () => {
    if (!isResponsive) {
      return maxPerSlide
    }

    const availableWidth = viewport.clientWidth || carousel.clientWidth || 0
    if (availableWidth <= 0) {
      return 1
    }

    const gapValue = window.getComputedStyle(carousel).getPropertyValue('--carousel-gap')
    const gap = Math.max(0, parseFloat(gapValue) || 0)
    const fitByWidth = Math.floor((availableWidth + gap) / (itemMinWidth + gap))
    return Math.max(1, Math.min(maxPerSlide, fitByWidth || 1))
  }

  const rebuildTrack = (perSlide) => {
    const safePerSlide = Math.max(1, Math.min(perSlide, originalItems.length))
    carousel.style.setProperty('--carousel-per-slide', String(safePerSlide))
    track.innerHTML = ''
    originalItems.forEach((item) => {
      track.appendChild(item)
    })

    if (originalItems.length > 1) {
      const clonesBefore = originalItems.slice(-safePerSlide).map(item => item.cloneNode(true))
      const clonesAfter = originalItems.slice(0, safePerSlide).map(item => item.cloneNode(true))
      clonesBefore.forEach(node => track.insertBefore(node, track.firstChild))
      clonesAfter.forEach(node => track.appendChild(node))
      index = safePerSlide
    } else {
      index = 0
    }
    currentPerSlide = safePerSlide
  }

  rebuildTrack(getPerSlide())

  const setPosition = (animate = true) => {
    const current = track.children[index]
    if (!current) {
      return
    }
    const offset = Math.max(0, current.offsetLeft - track.children[0].offsetLeft)
    track.style.transition = animate ? 'transform 0.5s ease' : 'none'
    track.style.transform = `translateX(-${offset}px)`
  }

  const move = (direction) => {
    if (isAnimating) {
      return
    }
    isAnimating = true
    index += direction
    setPosition(true)
  }

  const onTransitionEnd = () => {
    const totalOriginal = originalItems.length
    const firstOriginal = currentPerSlide
    const lastOriginal = currentPerSlide + totalOriginal - 1

    if (index > lastOriginal) {
      index = firstOriginal
      setPosition(false)
    } else if (index < firstOriginal) {
      index = lastOriginal
      setPosition(false)
    }
    isAnimating = false
  }

  const applyLayout = () => {
    const nextPerSlide = getPerSlide()
    if (nextPerSlide !== currentPerSlide) {
      rebuildTrack(nextPerSlide)
    }
    setPosition(false)
  }

  setPosition(false)
  track.addEventListener('transitionend', onTransitionEnd)

  const prevBtn = carousel.querySelector('[data-carousel-action="prev"]')
  const nextBtn = carousel.querySelector('[data-carousel-action="next"]')
  if (prevBtn) {
    prevBtn.addEventListener('click', () => move(-1))
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', () => move(1))
  }

  let timer = null
  const startAuto = () => {
    if (intervalMs > 0) {
      timer = window.setInterval(() => move(1), intervalMs)
    }
  }

  const stopAuto = () => {
    if (timer) {
      window.clearInterval(timer)
      timer = null
    }
  }

  carousel.addEventListener('mouseenter', stopAuto)
  carousel.addEventListener('mouseleave', startAuto)
  startAuto()

  window.addEventListener('resize', applyLayout)
  window.addEventListener('load', applyLayout, { once: true })

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(applyLayout).catch(() => {})
  }

  if ('ResizeObserver' in window) {
    const resizeObserver = new ResizeObserver(() => {
      applyLayout()
    })
    resizeObserver.observe(carousel)
    resizeObserver.observe(viewport)
  }

  const images = carousel.querySelectorAll('img')
  if (images.length) {
    let pending = images.length
    images.forEach((img) => {
      if (img.complete) {
        pending -= 1
      } else {
        img.addEventListener('load', () => {
          pending -= 1
          if (pending === 0) {
            setPosition(false)
          }
        }, { once: true })
      }
    })
    if (pending === 0) {
      setPosition(false)
    }
  }

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      applyLayout()
    })
  })
}

const setupMultiCarousels = () => {
  const carousels = document.querySelectorAll('.carousel-multi[data-max-per-slide], .carousel-multi[data-per-slide]')
  carousels.forEach(setupMultiScroller)
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    setupMultiCarousels()
    setupCodeCopyButtons()
  })
} else {
  setupMultiCarousels()
  setupCodeCopyButtons()
}
