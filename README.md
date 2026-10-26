# Awesome Paper Figures

个人收藏：图画得好的论文，方便画图时找参考。

- 数据源：[`papers.yaml`](papers.yaml)，图片存放在 `figures/<paper-id>/`
- 修改后运行 `python3 scripts/build_readme.py` 重新生成本文件（请勿手动编辑 README）


共收录 **4** 篇论文，**7** 张图。

## 目录

- [按论文浏览](#按论文浏览)
- [Teaser / Figure 1](#teaser--figure-1) (2)
- [方法框架图 / Pipeline](#方法框架图--pipeline) (0)
- [概念示意图 / Motivation](#概念示意图--motivation) (2)
- [实验结果图](#实验结果图) (2)
- [可视化 / 定性结果](#可视化--定性结果) (1)
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

📷 _截图待补_

> 💡 (a)(b)(c) 三栏依次给出真实案例、训练思路（what / where）和量化证据，一张图讲完动机、方法和结论。

### Why 1 + 1 < 1 in Visual Token Pruning: Beyond Naïve Integration via Multi-Objective Balanced Covering — Figure 1

*NeurIPS 2025* · [Paper](https://arxiv.org/abs/2505.10118) · [Code](https://github.com/YChenL/MoB)

📷 _截图待补_

> 💡 相对性能对比、prompt-visual 耦合分布和多预算雷达图组合在一起，把“问题现象 → 关键观察 → 方法收益”串成一条线。

## 方法框架图 / Pipeline

_暂无_

## 概念示意图 / Motivation

### DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models — Figure 1

*CVPR 2026* · [Paper](https://arxiv.org/abs/2603.03857)

📷 _截图待补_

> 💡 用同一个问题左右对比 coarse-to-fine 和 bottom-up 两种 pipeline，自上而下与自下而上的流程差异直观。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 2

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

📷 _截图待补_

> 💡 在潜空间中画出可行区域，对比“模仿专家轨迹”与“推理导向 + 邻域几何约束”两种优化方向，把抽象的目标函数可视化。

## 实验结果图

### DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models — Figure 2

*CVPR 2026* · [Paper](https://arxiv.org/abs/2603.03857)

📷 _截图待补_

> 💡 V* 上与各类 LVLM / grounded reasoning 方法的性能对比，并标出可扩展到更大模型。

### Perceptual Flow Network for Visually Grounded Reasoning — Figure 6

*ICML 2026* · [Paper](https://arxiv.org/abs/2605.02730)

📷 _截图待补_

> 💡 用 Score / Latency / Context 三轴图同时比较性能与开销，面积越小代价越低，读图规则简单。

## 可视化 / 定性结果

### Rethinking Latent Visual Reasoning: Grounding Latent Reasoning in Visual Evidence — Figure 3

*Preprint 2026* · [Paper](https://arxiv.org/abs/2609.34563)

📷 _截图待补_

> 💡 LVR 与 ReaLVR 的注意力矩阵并排对比，用框线标出关键读出区域，配合因果掩码的灰色三角，差异一目了然。

## 表格

_暂无_
