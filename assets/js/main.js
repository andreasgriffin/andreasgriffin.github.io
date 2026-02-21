const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

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

    const fitByWidth = Math.floor(availableWidth / itemMinWidth)
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

  window.addEventListener('resize', () => {
    const nextPerSlide = getPerSlide()
    if (nextPerSlide !== currentPerSlide) {
      rebuildTrack(nextPerSlide)
    }
    setPosition(false)
  })

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
      setPosition(false)
    })
  })
}

const setupMultiCarousels = () => {
  const carousels = document.querySelectorAll('.carousel-multi[data-max-per-slide], .carousel-multi[data-per-slide]')
  carousels.forEach(setupMultiScroller)
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', setupMultiCarousels)
} else {
  setupMultiCarousels()
}
