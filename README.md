# Awesome Paper Figures

个人收藏：图画得好的论文，方便画图时找参考。

- 数据源：[`papers.yaml`](papers.yaml)，图片存放在 `figures/<paper-id>/`
- 修改后运行 `python3 scripts/build_readme.py` 重新生成本文件（请勿手动编辑 README）


共收录 **4** 篇论文，**22** 张图。

## 目录

- [按论文浏览](#按论文浏览)
- [Teaser / Figure 1](#teaser--figure-1) (3)
- [方法框架图 / Pipeline](#方法框架图--pipeline) (2)
- [概念示意图 / Motivation](#概念示意图--motivation) (5)
- [实验结果图](#实验结果图) (6)
- [可视化 / 定性结果](#可视化--定性结果) (6)
- [表格](#表格) (0)

## 按论文浏览

| 论文 | 作者 | 发表 | 链接 | 收录日期 |
|---|---|---|---|---|
| Rethinking Latent Visual Reasoning: Grounding Latent Reasoning in Visual Evidence | Xi Xiao, Tianchen Zhao, Youngeun Kim, et al. | Preprint 2026 | [Paper](https://arxiv.org/abs/2609.34563) | 2026-10-26 |
| Why 1 + 1 < 1 in Visual Token Pruning: Beyond Naïve Integration via Multi-Objective Balanced Covering | Yangfu Li, Hongjian Zhan, Tianyi Chen, Qi Liu, Yu-jie Xiong, Yue Lu | NeurIPS 2025 | [Paper](https://arxiv.org/abs/2505.10118) · [Code](https://github.com/YChenL/MoB) | 2026-10-26 |
| DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models | Yangfu Li, Hongjian Zhan, Jiawei Chen, Yuning Gong, Qi Liu, Yue Lu | CVPR 2026 | [Paper](https://arxiv.org/abs/2603.03857) | 2026-10-26 |
| Perceptual Flow Network for Visually Grounded Reasoning | Yangfu Li, Yuning Gong, Hongjian Zhan, Teng Li, Yuanhuiyi Lyu, et al. | ICML 2026 | [Paper](https://arxiv.org/abs/2605.02730) | 2026-10-26 |

## Teaser / Figure 1

### Rethinking Latent Visual Reasoning: Grounding Latent Reasoning in Visual Evidence — Figure 1

*Preprint 2026* · [Paper](https://arxiv.org/abs/2609.34563)

<img src="figures/realvr-2026/fig1.png" width="800">

> 💡 三栏 (a) 真实案例 + 红框放大细节、(b) LVR / ReaLVR 两行流程对比、(c) 横向条形量化证据，一张图讲完动机、方法与结论；蓝 / 粉两色分别对应 what / where，配色与正文呼应。

### Why 1 + 1 < 1 in Visual Token Pruning: Beyond Naïve Integration via Multi-Objective Balanced Covering — Figure 1

*NeurIPS 2025* · [Paper](https://arxiv.org/abs/2505.10118) · [Code](https://github.com/YChenL/MoB)

<img src="figures/mob-2025/fig1.png" width="800">

> 💡 (a) 正负双向柱状图 + 浅色背景分区标注好坏，(b) 绿 / 蓝两组密度直方图区分强弱耦合，(c) 三个预算下的雷达图并在每个轴上标注紫色相对提升，层层递进地支撑“1+1<1”的论点。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 1

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig1.png" width="800">

> 💡 左侧用“原图 → 黄金证据 → 扩展 → 专家标注”的递进裁剪示意精度并非越高越好，右侧两条折线配置信带给出量化证据；绿 ✓ / 红 ✗ 角标与金色 Golden Priors 高亮串联图文。

## 方法框架图 / Pipeline

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 3

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig3.png" width="800">

> 💡 整体框架图：底部编码器 → 中部 Perceptual Flow Network 长条渐变 → 顶部 Reward Model，右上角用花括号拆解多维奖励公式；token 用小色块编码并配完整图例，实线 / 虚线区分训练与推理。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 4

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig4.png" width="800">

> 💡 数据合成流水线：Random Expand → Annotation → VLMs Verify 三层渐变条带堆叠，右侧竖排图例与左侧流程一一对应，紫 / 蓝色块延续全文的 token 配色。

## 概念示意图 / Motivation

### DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models — Figure 1

*CVPR 2026* · [Paper](https://arxiv.org/abs/2603.03857)

<img src="figures/deepscan-2026/fig1.png" width="800">

> 💡 用同一张卡通海狸示例左右对比 coarse-to-fine 与 bottom-up 两条 pipeline，失败分支半透明淡化、✗ / ✓ 图标标出成败，手绘风插图比真实图片更干净易懂。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 2

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig2.png" width="800">

> 💡 把隐空间画成一张 3D 曲面，对比“被专家轨迹拉偏 (Biased)”与“在邻域内向最优输出靠拢 (Closer)”，金色 / 紫色轨迹 + 力的箭头把抽象优化目标变成直观的几何图景。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 11

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig11.png" width="800">

> 💡 三种范式对比：(a) Agentic、(b) Grounded RLVR、(c) PFlowNet，每行都是“输入 → VLM → 推理过程 → 结论”，右侧用 ⚠️ / 💡 卡片总结优缺点，底部统一图例，排版整齐。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 12

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig12.png" width="800">

> 💡 用带位置 ID 的注意力掩码网格解释并行计算：浅紫阴影为可见区域，黑框标出各项概率对应的 token 块，右侧箭头连到公式，把实现细节画得一目了然。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 13

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig13.png" width="800">

> 💡 与 Fig 12 同一视觉语言，用粗黑线把矩阵分成四个区块，展示效率奖励的并行计算，适合作为“讲清楚 attention mask”类插图的参考。

## 实验结果图

### DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models — Figure 2

*CVPR 2026* · [Paper](https://arxiv.org/abs/2603.03857)

<img src="figures/deepscan-2026/fig2.png" width="800">

> 💡 柱状图用深紫 / 浅紫 / 浅蓝区分 training-free / training-based / 通用模型，本方法加粗黑框突出，虚线箭头与灰色斜体注释说明“可扩展”和基座分组。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 5

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig5.png" width="800">

> 💡 环形图 + 堆叠柱状图 + 双 y 轴折线的组合，同一组紫色深浅表示 RoI 数量，柱顶标数值，信息完整且配色统一。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 6

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig6.png" width="800">

> 💡 共享横轴的上下镜像柱状图：上方是分数，下方是延迟和上下文长度，“下方面积越小代价越低”的读法一目了然；各方法用 logo 图标代替图例。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 7

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig7.png" width="800">

> 💡 四个小多图并排的 Pass@k 曲线，统一图例放在底部，灰 / 浅紫 / 深紫三色对比清晰，简洁克制。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 9

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig9.png" width="800">

> 💡 在 Fig 5 的样式基础上加入 after RFT 黑框柱和红色虚线箭头标注下降百分比，直观展示 RFT 前后输出长度的变化。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 10

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig10.png" width="800">

> 💡 2×4 训练曲线网格：上排对比不同正则方案，下排扫描 ε 与 λ，分别用紫色与蓝色渐变表示超参从小到大，色彩即图例。

## 可视化 / 定性结果

### Rethinking Latent Visual Reasoning: Grounding Latent Reasoning in Visual Evidence — Figure 3

*Preprint 2026* · [Paper](https://arxiv.org/abs/2609.34563)

<img src="figures/realvr-2026/fig3.png" width="800">

> 💡 两张注意力矩阵并排，用彩色括号标出 Visual / Question / Latent / Answer 分区，框线 + 箭头注释直接点出“弱读出 vs 强读出”，红蓝发散色标配合灰色因果掩码，信息密度高但不乱。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 8

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig8.png" width="800">

> 💡 定性对比：左侧原图上用白色弧形箭头画出感知路径，右侧三个浅色文本框分别展示各方法推理过程，红字标错、下划线标关键句，PFlowNet 用虚线框 + 渐变底色突出。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 14

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig14.png" width="800">

> 💡 按 benchmark 分组的大图拼贴，蓝框 / 红框分别表示 TreeVGR 与 PFlowNet 的 grounding 结果，并用白色虚线放大局部，直观呈现预测多样性的差异。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 15

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig15.png" width="800">

> 💡 失败案例分析：左图右文，Question 卡片 + 紫色 PFlowNet 标签卡片 + 思考过程卡片竖排，✓ / ✗ 图标精确标在出错的步骤上。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 16

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig16.png" width="800">

> 💡 三方法纵向对比的案例卡片：黑底标签标出 baseline、紫底标签标出本方法，红色斜体标注错误类型（Language Bias / Missing Evidence），左侧配对应的 grounding 结果图。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 17

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

<img src="figures/pflownet-2026/fig17.png" width="800">

> 💡 与 Fig 16 同一模板的地图案例，红色错误类型标签（Hallucination / Language Bias）与下划线关键推理句组合，可作为定性案例图的排版模板。

## 表格

_暂无_
