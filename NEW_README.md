[![Chinese](https://img.shields.io/badge/Language-中文-red)](README_zh.md)

<div align="center">

# tkchart

[![Downloads](https://static.pepy.tech/badge/tkchart)](https://pepy.tech/project/tkchart) ![Downloads last 6 month](https://static.pepy.tech/personalized-badge/tkchart?period=total&units=international_system&left_color=grey&right_color=BLUE&left_text=downloads%20last%206%20month) [![Downloads](https://static.pepy.tech/badge/tkchart/month)](https://pepy.tech/project/tkchart) [![Downloads](https://static.pepy.tech/badge/tkchart/week)](https://pepy.tech/project/tkchart)

![PyPI - License](https://img.shields.io/badge/license-MIT-blue)

</div>

**<li>tkchart is a Python library for creating live updating line charts in tkinter.</li>**

---

<div align="center">
  <video src="readme-assets/chart.mp4" width="800" controls autoplay loop></video>
</div>

---

## ✨ Key Features

- ⚡ **Live Updates**: Seamlessly display streaming live data with high performance.
- 📉 **Multiple Lines**: Plot multiple lines on the same chart for easy data comparison.
- 🎨 **Highly Customizable**: Easily change colors, dimensions, and fonts to match your application's theme.
- 🎛️ **Granular Configuration**: Use explicit configuration methods like `configure_color()`, `configure_width()`, etc.
- 🛠️ **Cross-Platform**: Built purely on Python and Tkinter—no heavy dependencies!

[**Check out what's new in the latest release!**](CHANGES_en.md)

---

## 📦 Installation & Import

Install via `pip`:

```bash
pip install tkchart
```

Import into your Python script:

```python
import tkchart
```

---

## 🚀 Quick Start

Here's the minimal code needed to get a live updating chart running in your application.

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()

# 1. Create Line Chart
chart = tkchart.LineChart(
    master=root,
    x_axis_values=("a", "b", "c", "d", "e", "f"),
    y_axis_values=(100, 900)
)
chart.pack(pady=20)

# 2. Create Line
line = tkchart.Line(master=chart)

# 3. Display Data (Simulated live stream)
def loop():
    while True:
        random_data = random.choice(range(100, 900))
        chart.show_data(line=line, data=[random_data])
        time.sleep(1)

# Start data loop in a background thread
threading.Thread(target=loop, daemon=True).start()

root.mainloop()
```

---

## 💡 Examples Showcase

<details>
<summary><b>1. Basic Continuous Updates</b> (Click to expand)</summary>

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
<summary><b>2. Custom Styling & Filled Lines</b> (Click to expand)</summary>

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
<summary><b>3. Multiple Lines & Styles</b> (Click to expand)</summary>

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
<summary><b>4. Advanced Chart Config (Sections & Spacing)</b> (Click to expand)</summary>

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

## 📚 Documentation

Explore the full potential of `tkchart`, including detailed breakdowns of parameters and granular configuration functions!

- 📖 [**English Documentation**](documentation/DOCUMENTATION_en.md)
- 🇨🇳 [**Chinese Documentation**](documentation/DOCUMENTATION_zh.md)

---

## 👥 Contributors

- [<img src="https://github.com/childeyouyu.png?size=25" width="25"> youyu](https://github.com/childeyouyu)
