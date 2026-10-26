# Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models

[← 返回目录](../README.md)

- **作者**：Xin Zou, Yizhou Wang, Yibo Yan, Yuanhuiyi Lyu, Kening Zheng, et al.
- **发表**：ICML 2025
- **链接**：[Paper](https://arxiv.org/abs/2410.03577) · [Code](https://github.com/1zhou-Wang/MemVR)
- **收录日期**：2026-10-26

## TL;DR

- **动机**：MLLM 的幻觉常源于文本解码器在生成过程中逐渐“遗忘”视觉信息；VCD 等对比解码方法需要多次前向，推理慢且会损伤通用能力。
- **方法**：提出 MemVR，模仿人“记不清就再看一眼”：推理时监测各层的不确定性，当不确定性过高时，在中间触发层把视觉 token 作为 key-value 记忆经 FFN 重新注入（look-twice），不改模型、不需训练。
- **效果**：在 POPE、CHAIR、HallusionBench 等幻觉基准上显著降低幻觉，同时在 MME、MM-Vet 等通用基准上也有提升，推理开销与贪心解码几乎相同。

<a id="figure-1"></a>

## Figure 1

类型：[Teaser / 概念示意图](../gallery/teaser.md)

<img src="../figures/memvr-2025/fig1.png" width="800">

> 💡 左右对比 VCD 与 MemVR 两种范式：层堆叠示意 + 小柱状图表示输出分布，底部用“乌龟 / 飞机”图标对比推理速度，一眼看出差异。

<a id="figure-2"></a>

## Figure 2

类型：[实验结果图](../gallery/plot.md)

<img src="../figures/memvr-2025/fig2.png" width="800">

> 💡 两张雷达图分别展示多基准总分与 MME 子项，MemVR 用最外圈绿色粗线包住其他方法，轴上直接标数值。

<a id="figure-3"></a>

## Figure 3

类型：[可视化 / 定性结果](../gallery/visualization.md)

<img src="../figures/memvr-2025/fig3.png" width="800">

> 💡 原图 + 逐 token × 逐层不确定性热力图，用圆角框圈出高不确定性的 token，绿色单色渐变干净统一。

<a id="figure-4"></a>

## Figure 4

类型：[实验结果图](../gallery/plot.md)

<img src="../figures/memvr-2025/fig4.png" width="800">

> 💡 折线 + 柱状两个小图并排，实线 / 虚线区分 text / image 特征缩放，配色与图例简洁。

<a id="figure-5"></a>

## Figure 5

类型：[可视化 / 定性结果](../gallery/visualization.md)

<img src="../figures/memvr-2025/fig5.png" width="800">

> 💡 与 Fig 3 同一样式，展示“山竹”问题中不确定性在关键 token 上的跳变，适合作为“token × layer 热力图”的参考。

<a id="figure-6"></a>

## Figure 6

类型：[实验结果图](../gallery/plot.md)

<img src="../figures/memvr-2025/fig6.png" width="800">

> 💡 带误差棒和散点的柱状图 + 小提琴 / 箱线组合图，既给均值也展示分布。

<a id="figure-7"></a>

## Figure 7

类型：[实验结果图](../gallery/plot.md)

<img src="../figures/memvr-2025/fig7.png" width="800">

> 💡 双 y 轴的超参敏感性分析：左图柱 + 折线，右图面积 + 折线，虚线标出默认取值。

<a id="figure-8"></a>

## Figure 8

类型：[可视化 / 定性结果](../gallery/visualization.md)

<img src="../figures/memvr-2025/fig8.png" width="800">

> 💡 把各层不确定性画成一行数字格子，红框标出触发层，前后两行对比 MemVR 触发前后的变化，右侧图标标出答案对错。

<a id="figure-9"></a>

## Figure 9

类型：[可视化 / 定性结果](../gallery/visualization.md)

<img src="../figures/memvr-2025/fig9.png" width="800">

> 💡 长文本生成案例：左图右文，绿色 / 红色文字分别标正确与幻觉内容，带下划线的数值一目了然。

<a id="table-1"></a>

## Table 1

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab1.png" width="800">

> 💡 效率对比表，每个数值后附小号的相对倍数（×1.04），最优 / 次优用绿 / 蓝底色高亮。

<a id="table-2"></a>

## Table 2

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab2.png" width="800">

> 💡 方法特性对比表：隔行浅灰底 + 绿 ✓ / 红 ✗，把相关工作的差异总结得很清楚。

<a id="table-3"></a>

## Table 3

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab3.png" width="800">

> 💡 每个数字后跟彩色小箭头和增量（绿降红升），最优结果绿底高亮，本方法行用横线隔开。

<a id="table-4"></a>

## Table 4

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab4.png" width="800">

> 💡 多数据集 × 多设置的大表，用多级表头和分组，增量小字 + 绿底高亮保持整洁。

<a id="table-5"></a>

## Table 5

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab5.png" width="800">

> 💡 与 Table 3 同风格的小表，保持全文表格样式一致。

<a id="table-6"></a>

## Table 6

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab6.png" width="800">

> 💡 同一模板的 LLaVA-Bench 结果表。

<a id="table-7"></a>

## Table 7

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab7.png" width="800">

> 💡 同一模板的 MM-Vet 结果表。

<a id="table-8"></a>

## Table 8

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab8.png" width="800">

> 💡 多模型 × 多基准的综合表，多级表头 + 竖线分组，增量标注风格统一。

<a id="table-9"></a>

## Table 9

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab9.png" width="800">

> 💡 极简的变体对比小表。

<a id="table-10"></a>

## Table 10

类型：[表格](../gallery/table.md)

<img src="../figures/memvr-2025/tab10.png" width="800">

> 💡 策略消融小表，最优值绿底高亮。

