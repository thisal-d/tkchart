[![Language](https://img.shields.io/badge/Language-English-blue)](README.md)

<div align="center">

# tkchart

[![PyPI version](https://badge.fury.io/py/tkchart.svg)](https://pypi.org/project/tkchart/)

[![Downloads](https://static.pepy.tech/badge/tkchart)](https://pepy.tech/project/tkchart) ![Downloads last 6 month](https://static.pepy.tech/personalized-badge/tkchart?period=total&units=international_system&left_color=grey&right_color=BLUE&left_text=downloads%20last%206%20month) [![Downloads](https://static.pepy.tech/badge/tkchart/month)](https://pepy.tech/project/tkchart) [![Downloads](https://static.pepy.tech/badge/tkchart/week)](https://pepy.tech/project/tkchart)

![PyPI - License](https://img.shields.io/badge/license-MIT-blue)

</div>

**<li>tkchart 是一个用于在 tkinter 中创建实时更新折线图的 Python 库。</li>**

---

![Video 1](readme-assets/chart.mp4)

---

### 特性

- **实时更新**：通过折线图显示实时数据。
- **多条线**：支持在同一图表中绘制多条线，方便对比。
- **颜色自定义**：自定义颜色以匹配您的应用程序设计或数据表示。
- **字体自定义**：调整文本元素的字体以提高可读性。
- **尺寸自定义**：自定义图表的尺寸以适应不同的显示大小和布局。

[**查看最新变化 | 变更记录**](CHANGES_zh.md)

---

### 导入与安装

- **安装**

  ```
  pip install tkchart
  ```

- **导入**
  ```python
  import tkchart
  ```

---

### 简单指南

- **导入包**

  ```python
  import tkchart
  ```

- **创建折线图并放置图表**

  ```python
  chart = tkchart.LineChart(
      master=root,
      x_axis_values=("a", "b", "c", "d", "e", "f"),
      y_axis_values=(100, 900)
  )
  chart.place(x=10, y=10)
  ```

- **创建折线**

  ```python
  line = tkchart.Line(master=chart)
  ```

- **显示数据**
  使用循环显示数据

  ```python
  def loop():
      while True:
          random_data = random.choice(range(100, 900))
          chart.show_data(line=line, data=[random_data])
          time.sleep(1)

  # 作为线程调用循环
  theading.Thread(target=loop).start()
  ```

---

### 链接

- **文档 :** [文档](documentation)
  - [英文文档](documentation/DOCUMENTATION_en.md)
  - [中文文档](documentation/DOCUMENTATION_zh.md)
- **Python 官方 :** [tkchart](https://pypi.org/project/tkchart/)

---

### 您可以实现的功能

- **简单示例**

  https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9

  ```python
  import tkinter as tk  # 导入 tkinter 库
  import tkchart  # 导入 tkchart 模块来创建图表
  import random  # 导入 random 模块生成随机数据
  import threading  # 导入 threading 模块实现并发任务
  import time  # 导入 time 模块添加延时

  # 创建根窗口并配置
  root = tk.Tk()
  root.configure(bg="#0d1117")
  root.geometry("720x430+200+200")

  # 创建折线图控件
  line_chart = tkchart.LineChart(
      master=root,  # 设置根窗口为主控件
      x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴数据
      y_axis_values=(0, 1000)  # Y轴数据（范围）
  )

  line_chart.pack(pady=15)  # 将折线图控件打包到根窗口中

  # 创建折线
  line = tkchart.Line(master=line_chart)  # 设置折线图控件为父控件

  def display_data():
      """连续显示随机数据的函数。"""
      while True:
          random_data = [random.choice(range(0, 1000))]  # 生成0到1000之间的随机数据
          line_chart.show_data(line=line, data=random_data)  # 显示随机数据
          time.sleep(0.5)  # 每0.5秒更新一次数据

  # 作为线程调用 display_data 函数
  threading.Thread(target=display_data).start()

  # 启动主事件循环
  root.mainloop()
  ```

  ***

- **简单样式**

  https://github.com/Thisal-D/ctkchart/assets/93121062/afe56452-68c3-44f0-9c67-2ab6f6910f6e

  ```python
  import tkinter as tk  # 导入 tkinter 库
  import tkchart  # 导入 tkchart 模块来创建图表
  import random  # 导入 random 模块生成随机数据
  import threading  # 导入 threading 模块实现并发任务
  import time  # 导入 time 模块添加延时

  # 创建根窗口并配置
  root = tk.Tk()
  root.configure(bg="#0d1117")
  root.geometry("720x430+200+200")

  # 创建折线图控件
  line_chart = tkchart.LineChart(
      master=root,  # 设置根窗口为主控件
      x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴数据
      y_axis_values=(0, 1000),  # Y轴数据（范围）
      y_axis_label_count=10, # 设置Y轴标签数量为10
  )

  line_chart.pack(pady=15)  # 将折线图控件打包到根窗口中

  # 创建折线
  line = tkchart.Line(
      master=line_chart,  # 设置折线图控件为父控件
      size=2,  # 设置折线大小为2
      fill="enabled" # 启用折线填充
  )

  def display_data():
      """连续显示随机数据的函数。"""
      while True:
          random_data = [random.choice(range(0, 1000))]  # 生成0到1000之间的随机数据
          line_chart.show_data(line=line, data=random_data)  # 显示随机数据
          time.sleep(0.5)  # 每0.5秒更新一次数据

  # 作为线程调用 display_data 函数
  threading.Thread(target=display_data).start()

  # 启动主事件循环
  root.mainloop()
  ```

  ***

- **两条不同样式的折线**

  https://github.com/Thisal-D/ctkchart/assets/93121062/9bc35a39-a8ca-4942-9fc7-a1c89d1bd1bc

  ```python
  import tkinter as tk  # 导入 tkinter 库
  import tkchart  # 导入 tkchart 模块来创建图表
  import random  # 导入 random 模块生成随机数据
  import threading  # 导入 threading 模块实现并发任务
  import time  # 导入 time 模块添加延时

  # 创建根窗口并配置
  root = tk.Tk()
  root.configure(bg="#0d1117")
  root.geometry("720x430+200+200")

  # 创建折线图控件
  line_chart = tkchart.LineChart(
      master=root,  # 设置根窗口为主控件
      x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴数据
      y_axis_values=(0, 1000),  # Y轴数据（范围）
      y_axis_label_count=10, # 设置Y轴标签数量为10
  )

  line_chart.pack(pady=15)  # 将折线图控件打包到根窗口中

  # 创建折线1
  line1 = tkchart.Line(
      master=line_chart,  # 设置折线图控件为父控件
      size=2,  # 设置折线大小为2
      fill="enabled",  # 启用折线填充
      color="yellow"  # 设置颜色为黄色
  )

  # 创建折线2
  line2 = tkchart.Line(
      master=line_chart,  # 设置折线图控件为父控件
      size=2,  # 设置折线大小为2
      fill="disabled",  # 禁用折线填充
      color="red"  # 设置颜色为红色
  )

  def display_data():
      """连续显示随机数据的函数。"""
      while True:
          random_data = [random.choice(range(0, 1000))]  # 生成0到1000之间的随机数据
          line_chart.show_data(line=line1, data=random_data)  # 显示随机数据到第一条折线
          line_chart.show_data(line=line2, data=random_data)  # 显示随机数据到第二条折线
          time.sleep(0.5)  # 每0.5秒更新一次数据

  # 作为线程调用 display_data 函数
  threading.Thread(target=display_data).start()

  # 启动主事件循环
  root.mainloop()
  ```

- **3条具有不同线条样式的线**

  https://github.com/Thisal-D/ctkchart/assets/93121062/6d568b70-2ceb-42d0-b93c-0096f2745134

  ```python
  import tkinter as tk  # 导入 tkinter 库
  import tkchart  # 导入 tkchart 模块用于图表创建
  import random  # 导入 random 模块用于生成随机数据
  import threading  # 导入 threading 模块用于并发执行任务
  import time  # 导入 time 模块用于添加延迟

  # 创建根窗口并配置
  root = tk.Tk()
  root.configure(bg="#0d1117")
  root.geometry("720x430+200+200")

  # 创建折线图小部件
  line_chart = tkchart.LineChart(
      master=root,  # 设置根窗口为主控件
      x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴值
      y_axis_values=(0, 1000),  # Y轴值（范围）
      y_axis_label_count=10, # 设置Y轴标签计数为10
  )

  line_chart.pack(pady=15)  # 将折线图小部件放入根窗口

  # 创建第一条线
  line1 = tkchart.Line(
      master=line_chart,  # 设置主控件为折线图
      size=2,  # 设置线条大小为2
      fill="enabled" # 启用线条填充
  )

  line2 = tkchart.Line(
      master=line_chart,  # 设置主控件为折线图
      color="#5dffb6", # 设置颜色为绿色
      size=2,  # 设置线条大小为2
      style="dashed", # 设置样式为虚线
      style_type=(10, 5), # 设置虚线的宽度和间隔
  )

  line3 = tkchart.Line(
      master=line_chart,  # 设置主控件为折线图
      color="#FFBAD2", # 设置颜色为粉色
      size=2,  # 设置线条大小为2
      point_highlight="enabled", # 启用高亮点
      point_highlight_color="#FFBAD2", # 设置高亮点颜色
  )

  def display_data():
      """连续显示随机数据在折线图上。"""
      while True:
          random_data = random.choices(range(0, 1000),k=1)  # 生成0到1000之间的随机数据
          line_chart.show_data(line=line1, data=random_data)  # 在第一条线上显示随机数据
          random_data = random.choices(range(0, 1000),k=1) # 生成0到1000之间的随机数据
          line_chart.show_data(line=line2, data=random_data)  # 在第二条线上显示随机数据
          random_data = random.choices(range(0, 1000),k=1) # 生成0到1000之间的随机数据
          line_chart.show_data(line=line3, data=random_data)  # 在第三条线上显示随机数据
          time.sleep(0.5)  # 暂停0.5秒再进行下一次迭代

  # 在单独的线程中调用 display_data 函数
  threading.Thread(target=display_data).start()

  # 启动主事件循环
  root.mainloop()
  ```

  ***

- **高级**（实际上只是增加了两个属性）

  https://github.com/Thisal-D/ctkchart/assets/93121062/c2838fd6-3a0f-45be-bb39-9953d007067d

  ```python
  import tkinter as tk  # 导入 tkinter 库
  import tkchart  # 导入 tkchart 模块用于图表创建
  import random  # 导入 random 模块用于生成随机数据
  import threading  # 导入 threading 模块用于并发执行任务
  import time  # 导入 time 模块用于添加延迟

  # 创建根窗口并配置
  root = tk.Tk()
  root.configure(bg = "#0d1117")
  root.geometry("720x430+200+200")

  # 创建折线图小部件
  line_chart = tkchart.LineChart(
      master=root,  # 设置根窗口为主控件
      x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴值
      y_axis_values=(0, 1000),  # Y轴值（范围）
      y_axis_label_count=10, # 设置Y轴标签计数为1
      y_axis_section_count=10,
      x_axis_section_count=10,
  )

  line_chart.pack(pady=15)  # 将折线图小部件放入根窗口

  line1 = tkchart.Line(
      master=line_chart,  # 设置主控件为折线图
      color="#5dffb6", # 设置颜色为绿色
      size=2,  # 设置线条大小为2
      style="dashed", # 设置样式为虚线
      style_type=(10, 5), # 设置虚线的宽度和间隔
  )

  line2 = tkchart.Line(
      master=line_chart,  # 设置主控件为折线图
      color="#FFBAD2", # 设置颜色为粉色
      size=2,  # 设置线条大小为2
      point_highlight="enabled", # 启用高亮点
      point_highlight_color="#FFBAD2", # 设置高亮点颜色
  )

  def display_data():
      """连续显示随机数据在折线图上。"""
      while True:
          random_data = [random.choice(range(0, 1000))]  # 生成0到1000之间的随机数据
          line_chart.show_data(line=line1, data=random_data)  # 在第一条线上显示随机数据
          random_data = [random.choice(range(0, 1000))]  # 生成0到1000之间的随机数据
          line_chart.show_data(line=line2, data=random_data)  # 在第二条线上显示随机数据
          time.sleep(0.5)  # 暂停0.5秒再进行下一次迭代

  # 在单独的线程中调用 display_data 函数
  threading.Thread(target=display_data).start()

  # 启动主事件循环
  root.mainloop()
  ```

---

**探索可自定义的功能，如颜色、字体等，详细内容请参考文档。**

#### 请参考完整文档

- [**英文文档**](documentation/DOCUMENTATION_en.md)
- [**中文文档**](documentation/DOCUMENTATION_zh.md)

---

#### 贡献者

- [<img src="https://github.com/childeyouyu.png?size=25" width="25">](https://github.com/childeyouyu) [youyu](https://github.com/childeyouyu)
