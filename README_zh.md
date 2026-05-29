[![Language](https://img.shields.io/badge/Language-English-blue)](README.md)

<div align="center">

# tkchart

[![PyPI version](https://badge.fury.io/py/tkchart.svg)](https://pypi.org/project/tkchart/)
[![Downloads](https://static.pepy.tech/badge/tkchart)](https://pepy.tech/project/tkchart)
![Downloads last 6 month](https://static.pepy.tech/personalized-badge/tkchart?period=total&units=international_system&left_color=grey&right_color=BLUE&left_text=downloads%20last%206%20month)
[![Downloads/Month](https://static.pepy.tech/badge/tkchart/month)](https://pepy.tech/project/tkchart)
[![Downloads/Week](https://static.pepy.tech/badge/tkchart/week)](https://pepy.tech/project/tkchart)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**用于在 Tkinter 中创建实时更新折线图的 Python 库。**

</div>

---

https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9

---

## ✨ 特性

| 特性 | 描述 |
|---|---|
| ⚡ **实时更新** | 持续流式显示实时数据 |
| 📉 **多条折线** | 在同一图表中绘制多条线，便于对比 |
| 🎨 **颜色自定义** | 根据应用程序设计自定义颜色 |
| 🔤 **字体自定义** | 调整文字字体以提高可读性 |
| 📐 **尺寸控制** | 调整图表大小以适应任何布局 |
| 🎛️ **细粒度配置** | 通过 `configure_*()` 方法精确控制（v2.2.0+） |

> 📋 [**查看最新版本的变更记录 →**](CHANGES_zh.md)

---

## 📦 安装

```bash
pip install tkchart
```

```python
import tkchart
```

---

## 🚀 快速开始

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()

# 1. 创建图表
chart = tkchart.LineChart(
    master=root,
    x_axis_values=("a", "b", "c", "d", "e", "f"),
    y_axis_values=(100, 900)
)
chart.place(x=10, y=10)

# 2. 创建折线
line = tkchart.Line(master=chart)

# 3. 在后台线程中持续推送数据
def loop():
    while True:
        chart.show_data(line=line, data=[random.choice(range(100, 900))])
        time.sleep(1)

threading.Thread(target=loop, daemon=True).start()
root.mainloop()
```

---

## 🎬 示例展示

### 1 — 简单示例

https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9

<details>
<summary>查看代码</summary>

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430+200+200")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000)
)
line_chart.pack(pady=15)

line = tkchart.Line(master=line_chart)

def display_data():
    while True:
        line_chart.show_data(line=line, data=[random.choice(range(0, 1000))])
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```
</details>

---

### 2 — 样式化与填充折线

https://github.com/Thisal-D/ctkchart/assets/93121062/afe56452-68c3-44f0-9c67-2ab6f6910f6e

<details>
<summary>查看代码</summary>

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430+200+200")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000),
    y_axis_label_count=10,
)
line_chart.pack(pady=15)

line = tkchart.Line(master=line_chart, size=2, fill="enabled")

def display_data():
    while True:
        line_chart.show_data(line=line, data=[random.choice(range(0, 1000))])
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```
</details>

---

### 3 — 两条不同样式的折线

https://github.com/Thisal-D/ctkchart/assets/93121062/9bc35a39-a8ca-4942-9fc7-a1c89d1bd1bc

<details>
<summary>查看代码</summary>

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430+200+200")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000),
    y_axis_label_count=10,
)
line_chart.pack(pady=15)

line1 = tkchart.Line(master=line_chart, color="#5dffb6", size=2, style="dashed", style_type=(10, 5))
line2 = tkchart.Line(master=line_chart, color="#FFBAD2", size=2, point_highlight="enabled", point_highlight_color="#FFBAD2")

def display_data():
    while True:
        line_chart.show_data(line=line1, data=[random.choice(range(0, 1000))])
        line_chart.show_data(line=line2, data=[random.choice(range(0, 1000))])
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```
</details>

---

### 4 — 三条不同样式的折线

https://github.com/Thisal-D/ctkchart/assets/93121062/6d568b70-2ceb-42d0-b93c-0096f2745134

<details>
<summary>查看代码</summary>

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430+200+200")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000),
    y_axis_label_count=10,
)
line_chart.pack(pady=15)

line1 = tkchart.Line(master=line_chart, size=2, fill="enabled")
line2 = tkchart.Line(master=line_chart, color="#5dffb6", size=2, style="dashed", style_type=(10, 5))
line3 = tkchart.Line(master=line_chart, color="#FFBAD2", size=2, point_highlight="enabled", point_highlight_color="#FFBAD2")

def display_data():
    while True:
        line_chart.show_data(line=line1, data=random.choices(range(0, 1000), k=1))
        line_chart.show_data(line=line2, data=random.choices(range(0, 1000), k=1))
        line_chart.show_data(line=line3, data=random.choices(range(0, 1000), k=1))
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```
</details>

---

### 5 — 带网格分区

https://github.com/Thisal-D/ctkchart/assets/93121062/c2838fd6-3a0f-45be-bb39-9953d007067d

<details>
<summary>查看代码</summary>

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430+200+200")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000),
    y_axis_label_count=10,
    y_axis_section_count=10,
    x_axis_section_count=10,
)
line_chart.pack(pady=15)

line1 = tkchart.Line(master=line_chart, color="#5dffb6", size=2, style="dashed", style_type=(10, 5))
line2 = tkchart.Line(master=line_chart, color="#FFBAD2", size=2, point_highlight="enabled", point_highlight_color="#FFBAD2")

def display_data():
    while True:
        line_chart.show_data(line=line1, data=[random.choice(range(0, 1000))])
        line_chart.show_data(line=line2, data=[random.choice(range(0, 1000))])
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```
</details>

---

## 📚 文档

探索所有参数、配置方法和高级用法：

- 📖 [**英文文档**](documentation/DOCUMENTATION_en.md)
- 🇨🇳 [**中文文档**](documentation/DOCUMENTATION_zh.md)
- 🐍 [**PyPI 页面**](https://pypi.org/project/tkchart/)

---

## 👥 贡献者

- [<img src="https://github.com/childeyouyu.png?size=25" width="25">](https://github.com/childeyouyu) [youyu](https://github.com/childeyouyu)
