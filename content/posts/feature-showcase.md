---
title: "Flexiona 全功能展示"
date: 2025-07-18
draft: false
math: true
tags: ["showcase", "tutorial", "features"]
---

# 功能全展示 | Feature Showcase

这篇文章将展示 Flexiona (流域) 平台的全部功能特性，包括文字格式化、数学公式、图片、链接、动画和特殊样式等。

## 1. 文本格式化 | Text Formatting

基本文本样式包括：

- **粗体文本** 使用 `**粗体文本**`
- *斜体文本* 使用 `*斜体文本*`
- ***粗斜体文本*** 使用 `***粗斜体文本***`
- ~~删除线~~ 使用 `~~删除线~~`

### 1.1 引用和列表

> 这是一个引用文本。
> 
> 多行引用看起来是这样的。

有序列表：

1. 第一项
2. 第二项
   1. 嵌套项
   2. 另一个嵌套项
3. 第三项

无序列表：

- 项目一
- 项目二
  - 嵌套项目
  - 另一个嵌套项目
- 项目三

### 1.2 代码展示

行内代码：`print("Hello, Flexiona!")`

代码块：

```python
def fibonacci(n):
    """生成斐波那契数列的前n项"""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

# 生成并打印前10个斐波那契数
fib_numbers = fibonacci(10)
print(fib_numbers)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 2. 数学公式 | Mathematical Formulas

Flexiona 支持 $\LaTeX$ 数学公式渲染。

### 2.1 行内公式

爱因斯坦质能方程：$E = mc^2$

欧拉恒等式：$e^{i\pi} + 1 = 0$

### 2.2 独立公式

傅里叶变换：

$$F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t}dt$$

高斯分布概率密度函数：

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

复杂矩阵表达式：

$$
\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
=
\begin{pmatrix}
ax + by + cz \\
dx + ey + fz \\
gx + hy + iz
\end{pmatrix}
$$

## 3. 图片展示 | Images

### 3.1 本地图片

![示例图片](/images/test-post/example.jpg "示例图片")

### 3.2 远程图片

![数据可视化](https://images.unsplash.com/photo-1551288049-bebda4e38f71 "数据可视化")

## 4. 链接与跳转 | Links and Navigation

### 4.1 外部链接

访问 [Flexiona GitHub 仓库](https://github.com/Tsunami-kun/flexiona)。

### 4.2 内部链接

前往 [第一篇博客文章](/posts/first-post)。

### 4.3 锚点跳转

点击跳转到[数学公式部分](#2-数学公式--mathematical-formulas)。

## 5. GIF 动画 | Animations

以下是一个展示物理模拟的 GIF 动画：

![物理模拟动画](/images/test-post/physics-simulation.gif "物理波动模拟")

## 6. 特殊样式 | Custom Styling

### 6.1 自定义颜色文字

<span style="color:red">这是红色文字</span>

<span style="color:#00a0e9">这是蓝色文字</span>

<span style="color:green; font-weight:bold">这是绿色加粗文字</span>

### 6.2 高亮文本

<mark>这是高亮文本</mark>

### 6.3 自定义字体大小

<span style="font-size: 24px">大号文本</span>

<span style="font-size: 8px">小号文本</span>

## 7. 表格 | Tables

| 姓名 | 年龄 | 专业 |
|------|------|------|
| 张三 | 21 | 计算机科学 |
| 李四 | 23 | 人工智能 |
| 王五 | 22 | 数据科学 |

## 8. 注释与脚注

这里有一个脚注[^1]。

[^1]: 这是脚注内容。

## 9. 任务列表

- [x] 已完成任务
- [ ] 未完成任务
- [x] 另一项已完成任务

## 10. 水平线

---

## 总结 | Conclusion

本文展示了 Flexiona 平台支持的各种格式和功能，包括文本格式化、数学公式、图片、链接、GIF 动画和自定义样式等。通过这些功能，可以创建丰富多样的学术博客内容。

希望这篇功能展示能帮助您更好地使用 Flexiona 平台！