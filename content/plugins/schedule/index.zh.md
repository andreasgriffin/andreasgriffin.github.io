---
title: "计划付款"
description: "计划一次性或定期的比特币付款，跟踪到期时间，并在 Bitcoin-Safe 中准备交易以供审核。"
draft: false
tags: ["Plugins"]
images: ["schedule.png"]
weight: 40
faq:
  title: "计划付款相关问题"
  items:
    - question: "可以只计划一次付款吗，还是只能计划定期付款？"
      answer: "两者都可以。您可以创建一次性付款、固定次数的重复付款，或持续进行的计划。"
    - question: "计划可以多久重复一次？"
      answer: "重复间隔可以设置为：\n- 分钟、小时或天\n- 周，可选择特定的星期几\n- 月或年，按日历日期或星期模式"
    - question: "可以用法定货币设置金额吗？"
      answer: "可以。您可以用以下方式设置金额：\n- 比特币\n- 受支持的法定货币\n\n法定货币金额可以使用：\n- 实时汇率\n- 每天 00:00 GMT 固定的 CoinGecko 汇率\n\n还可以为下一笔付款设置汇率覆盖。"
    - question: "地址会被重复使用吗？"
      answer: "不会。每个收款地址只使用一次。当某个收款人的地址用完后，您可以为该收款人添加更多地址。"
    - question: "Bitcoin-Safe 会自动发送付款吗？"
      answer: "不会。付款到期时，Schedule 会在 Bitcoin-Safe 中准备交易供您审核，签名和广播仍由您负责。"
    - question: "可以同时向多个收款人付款吗？"
      answer: "可以。选择多笔计划付款，然后点击**支付所选**。Bitcoin-Safe 会将它们合并为一笔批量交易。"
    - question: "如果某笔付款已通过现金或其他方式完成，该怎么办？"
      answer: "您可以添加一笔**链外**付款。它会在计划中记录该付款，而不需要比特币交易，从而让进度保持准确。"
---

### {{< page-title >}}

<p class="lead">计划比特币付款，让 Schedule 帮您跟踪哪些付款即将到期。</p>

<ul class="plugin-features">
<li>向员工付款，或安排其他定期支出</li>
<li>设置定期转账</li>
<li>计划一笔不能忘记的一次性付款</li>
</ul>

付款到期时，Schedule 会在 Bitcoin-Safe 中准备交易供您审核。您仍需负责签名和广播。

{{< video "schedule.mp4" controls >}}

### 灵活的付款计划

- 选择一次性付款、固定次数重复付款，或持续进行的计划。
- 设置开始日期和重复间隔：分钟、小时、天、周、月或年。周计划可以选择特定的星期几；月计划和年计划支持日历日期和星期模式。
- 以比特币或受支持的法定货币设置收款人、类别和金额。
- 对于法定货币金额，可以使用实时汇率，或每天 00:00 GMT 固定的 CoinGecko 汇率。可以为下一笔付款设置汇率覆盖。
- 固定次数的计划会显示每笔付款及总额的预览。

### 在钱包中准备付款

- 查看下次到期日期和付款进度；到期的付款会突出显示，并可能触发 Bitcoin-Safe 提示。
- 在交易编辑器中准备一笔到期付款或一批付款，收款人输出、标签和类别会自动填写。
- 签名和广播前，可以检查并自定义交易。
- 保存可重复使用的收款人，包括名称和多个地址。Schedule 可以为付款选择一个未使用的地址。

### 跟踪和管理计划

- 可按到期状态、计划类型或类别查找计划。列表会显示日期、已完成付款、频率、收款人、金额、类别和总额。
- 查看已完成的付款和即将到来的付款。匹配的钱包交易可以更新进度；您也可以手动添加付款或重新扫描钱包交易。
- 在首次记录付款之前可编辑计划，也可以复制或删除计划，并将计划以 JSON 备份导入和导出。

<section class="plugin-cta-band border rounded-4 bg-body-tertiary p-4 mt-5 text-center">
<h2 class="h4 mb-2">下载 Bitcoin-Safe</h2>
<p class="text-muted mb-3">插件已包含在 Bitcoin-Safe 中。下载应用即可试用。</p>
<div class="plugin-cta d-flex flex-column align-items-center gap-1">
<a class="btn btn-primary px-4" href="../../download/">下载 Bitcoin-Safe</a>
<small class="text-muted">免费开源 · Windows、macOS、Linux</small>
</div>
</section>

### 常见问题

<details>
<summary>可以只计划一次付款吗，还是只能计划定期付款？</summary>

两者都可以。您可以创建一次性付款、固定次数的重复付款，或持续进行的计划。

</details>

<details>
<summary>计划可以多久重复一次？</summary>

重复间隔可以设置为：

- 分钟、小时或天
- 周，可选择特定的星期几
- 月或年，按日历日期或星期模式

</details>

<details>
<summary>可以用法定货币设置金额吗？</summary>

可以。您可以用以下方式设置金额：

- 比特币
- 受支持的法定货币

法定货币金额可以使用：

- 实时汇率
- 每天 00:00 GMT 固定的 CoinGecko 汇率

还可以为下一笔付款设置汇率覆盖。

</details>

<details>
<summary>地址会被重复使用吗？</summary>

不会。每个收款地址只使用一次。当某个收款人的地址用完后，您可以为该收款人添加更多地址。

</details>

<details>
<summary>Bitcoin-Safe 会自动发送付款吗？</summary>

不会。付款到期时，Schedule 会在 Bitcoin-Safe 中准备交易供您审核，签名和广播仍由您负责。

</details>

<details>
<summary>可以同时向多个收款人付款吗？</summary>

可以。选择多笔计划付款，然后点击**支付所选**。Bitcoin-Safe 会将它们合并为一笔批量交易。

</details>

<details>
<summary>如果某笔付款已通过现金或其他方式完成，该怎么办？</summary>

您可以添加一笔**链外**付款。它会在计划中记录该付款，而不需要比特币交易，从而让进度保持准确。

</details>
</content>
