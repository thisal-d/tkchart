<div align="center">

# 📈 tkchart

[![Downloads](https://static.pepy.tech/badge/tkchart)](https://pepy.tech/project/tkchart) 
[![Downloads last 6 month](https://static.pepy.tech/personalized-badge/tkchart?period=total&units=international_system&left_color=grey&right_color=BLUE&left_text=downloads%20last%206%20month)](https://pepy.tech/project/tkchart) 
[![PyPI version](https://badge.fury.io/py/tkchart.svg)](https://pypi.org/project/tkchart/)
![PyPI - License](https://img.shields.io/badge/license-MIT-blue)
[![Language](https://img.shields.io/badge/Language-English-blue)](NEW_README.md)

**tkchart 是一个功能强大、高度可定制的 Python 库，用于在 tkinter 中创建实时更新的折线图。**

</div>

---

<div align="center">
  <video src="readme-assets/chart.mp4" width="800" controls autoplay loop></video>
</div>

---

## ✨ 核心特性

- ⚡ **实时更新**: 高性能地显示流式实时数据。
- 📉 **多条折线**: 支持在同一图表中绘制多条线，方便数据对比。
- 🎨 **高度自定义**: 轻松修改颜色、尺寸和字体，完美契合您的应用程序主题。
- 🎛️ **细粒度配置**: 提供清晰具体的配置方法（例如 `configure_color()`, `configure_width()` 等）。
- 🛠️ **跨平台**: 纯 Python 和 Tkinter 构建——没有任何繁重的外部依赖！

[**查看最新版本中的新变化！**](CHANGES_zh.md)

---

## 📦 导入与安装

使用 `pip` 安装:
```bash
pip install tkchart
```

在您的 Python 脚本中导入:
```python
import tkchart
```

---

## 🚀 简单指南

这是在应用程序中运行实时图表所需的最简代码示例。

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()

# 1. 创建折线图
chart = tkchart.LineChart(
    master=root,
    x_axis_values=("a", "b", "c", "d", "e", "f"),
    y_axis_values=(100, 900)
)
chart.pack(pady=20)

# 2. 创建折线
line = tkchart.Line(master=chart)

# 3. 显示数据（模拟实时数据流）
def loop():
    while True:
        random_data = random.choice(range(100, 900))
        chart.show_data(line=line, data=[random_data])
        time.sleep(1)

# 将循环放入后台线程运行
threading.Thread(target=loop, daemon=True).start()

root.mainloop()
```

---

## 💡 代码示例

<details>
<summary><b>1. 简单实时更新示例</b> (点击展开)</summary>

<br>
https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000)
)
line_chart.pack(pady=15)

line = tkchart.Line(master=line_chart)

def display_data():
    while True:
        random_data = [random.choice(range(0, 1000))]
        line_chart.show_data(line=line, data=random_data)
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```
</details>

<details>
<summary><b>2. 自定义样式 & 折线填充</b> (点击展开)</summary>

<br>
https://github.com/Thisal-D/ctkchart/assets/93121062/afe56452-68c3-44f0-9c67-2ab6f6910f6e

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000),
    y_axis_label_count=10
)
line_chart.pack(pady=15)

line = tkchart.Line(master=line_chart, size=2, fill="enabled")

def display_data():
    while True:
        random_data = [random.choice(range(0, 1000))]
        line_chart.show_data(line=line, data=random_data)
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```
</details>

<details>
<summary><b>3. 多条不同样式的折线</b> (点击展开)</summary>

<br>
https://github.com/Thisal-D/ctkchart/assets/93121062/6d568b70-2ceb-42d0-b93c-0096f2745134

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000),
    y_axis_label_count=10
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

<details>
<summary><b>4. 高级图表配置 (网格与刻度)</b> (点击展开)</summary>

<br>
https://github.com/Thisal-D/ctkchart/assets/93121062/c2838fd6-3a0f-45be-bb39-9953d007067d

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()
root.configure(bg="#0d1117")
root.geometry("720x430")

line_chart = tkchart.LineChart(
    master=root,
    x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),
    y_axis_values=(0, 1000),
    y_axis_label_count=10,
    y_axis_section_count=10,
    x_axis_section_count=10
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

## 📚 详细文档

探索 `tkchart` 的全部潜力，包括参数的详细说明和细粒度配置功能！

- 📖 [**英文文档**](documentation/DOCUMENTATION_en.md)
- 🇨🇳 [**中文文档**](documentation/DOCUMENTATION_zh.md)

---

## 👥 贡献者

- [<img src="https://github.com/childeyouyu.png?size=25" width="25"> youyu](https://github.com/childeyouyu)
