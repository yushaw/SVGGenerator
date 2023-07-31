# SVGGenerator
[English](./README_en.md) | 简体中文

## 主要工作
1. 训练了一个LoRa，在 Stable Diffusion 生成图片时，微调为简单颜色和线条的图片；
2. 去除图片的背景；
3. 将png图片转换为svg。

## 当前的问题
1. LoRa的训练数据集质量需要改进；
2. 生成的图片的主题不够突出；
3. 图片的关键词需要调整（训练数据集的标记质量欠缺）；
4. diffusers 的图片生成流程需要优化，提升图片质量。

## 使用的库
- huggingface/diffusers
- visioncortex/vtracer
