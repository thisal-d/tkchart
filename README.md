[![Chinese](https://img.shields.io/badge/Language-中文-red)](README_zh.md)

<div align="center">

# tkchart

[![PyPI version](https://badge.fury.io/py/tkchart.svg)](https://pypi.org/project/tkchart/)

[![Downloads](https://static.pepy.tech/badge/tkchart)](https://pepy.tech/project/tkchart) ![Downloads last 6 month](https://static.pepy.tech/personalized-badge/tkchart?period=total&units=international_system&left_color=grey&right_color=BLUE&left_text=downloads%20last%206%20month) [![Downloads/Month](https://static.pepy.tech/badge/tkchart/month)](https://pepy.tech/project/tkchart) [![Downloads/Week](https://static.pepy.tech/badge/tkchart/week)](https://pepy.tech/project/tkchart)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**A Python library for creating live-updating line charts in Tkinter.**

</div>

---

https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9

---

## ✨ Features

| Feature                    | Description                                                |
| -------------------------- | ---------------------------------------------------------- |
| ⚡ **Live Updates**        | Stream and display real-time data continuously             |
| 📉 **Multiple Lines**      | Plot several lines on the same chart for easy comparison   |
| 🎨 **Color Customization** | Tailor colors to match your app's design                   |
| 🔤 **Font Customization**  | Adjust text fonts for better readability                   |
| 📐 **Dimension Control**   | Resize charts to fit any layout                            |
| 🎛️ **Granular Config**     | Fine-grained control via `configure_*()` methods (v2.2.0+) |

> 📋 [**See what's new in the latest release →**](CHANGES_en.md)

---

## 📦 Installation

```bash
pip install tkchart
```

```python
import tkchart
```

---

## 🚀 Quick Start

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()

# 1. Create the chart
chart = tkchart.LineChart(
    master=root,
    x_axis_values=("a", "b", "c", "d", "e", "f"),
    y_axis_values=(100, 900)
)
chart.place(x=10, y=10)

# 2. Create a line
line = tkchart.Line(master=chart)

# 3. Stream data in a background thread
def loop():
    while True:
        chart.show_data(line=line, data=[random.choice(range(100, 900))])
        time.sleep(1)

threading.Thread(target=loop, daemon=True).start()
root.mainloop()
```

---

## 🎬 Live Examples

### 1 — Simple

https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9

<details>
<summary>View code</summary>

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

### 2 — Styled & Filled Line

https://github.com/Thisal-D/ctkchart/assets/93121062/afe56452-68c3-44f0-9c67-2ab6f6910f6e

<details>
<summary>View code</summary>

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

line = tkchart.Line(
    master=line_chart,
    size=2,
    fill="enabled"
)

def display_data():
    while True:
        line_chart.show_data(line=line, data=[random.choice(range(0, 1000))])
        time.sleep(0.5)

threading.Thread(target=display_data, daemon=True).start()
root.mainloop()
```

</details>

---

### 3 — 2 Lines with Different Styles

https://github.com/Thisal-D/ctkchart/assets/93121062/9bc35a39-a8ca-4942-9fc7-a1c89d1bd1bc

<details>
<summary>View code</summary>

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

line1 = tkchart.Line(
    master=line_chart,
    color="#5dffb6",
    size=2,
    style="dashed",
    style_type=(10, 5),
)

line2 = tkchart.Line(
    master=line_chart,
    color="#FFBAD2",
    size=2,
    point_highlight="enabled",
    point_highlight_color="#FFBAD2",
)

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

### 4 — 3 Lines with Different Styles

https://github.com/Thisal-D/ctkchart/assets/93121062/6d568b70-2ceb-42d0-b93c-0096f2745134

<details>
<summary>View code</summary>

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

line2 = tkchart.Line(
    master=line_chart,
    color="#5dffb6",
    size=2,
    style="dashed",
    style_type=(10, 5),
)

line3 = tkchart.Line(
    master=line_chart,
    color="#FFBAD2",
    size=2,
    point_highlight="enabled",
    point_highlight_color="#FFBAD2",
)

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

### 5 — With Grid Sections

https://github.com/Thisal-D/ctkchart/assets/93121062/c2838fd6-3a0f-45be-bb39-9953d007067d

<details>
<summary>View code</summary>

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

line1 = tkchart.Line(
    master=line_chart,
    color="#5dffb6",
    size=2,
    style="dashed",
    style_type=(10, 5),
)

line2 = tkchart.Line(
    master=line_chart,
    color="#FFBAD2",
    size=2,
    point_highlight="enabled",
    point_highlight_color="#FFBAD2",
)

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

## 📚 Documentation

Explore all parameters, configuration methods, and advanced usage:

- 📖 [**English Documentation**](documentation/DOCUMENTATION_en.md)
- 🇨🇳 [**Chinese Documentation**](documentation/DOCUMENTATION_zh.md)
- 🐍 [**PyPI Package**](https://pypi.org/project/tkchart/)

---

## 👥 Contributors

- [<img src="https://github.com/childeyouyu.png?size=25" width="25">](https://github.com/childeyouyu) [youyu](https://github.com/childeyouyu)
