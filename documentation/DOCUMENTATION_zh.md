<div id="top">

[![Language](https://img.shields.io/badge/Language-English-blue)](DOCUMENTATION_en.md)

</div>

---

<div id="howtouse"> 

<a href="#top">**回到顶部**</a> | <a href="#example">**例子**</a> | <a href="#parameter_explanation">**参数说明**</a> | <a href="../CHANGES_zh.md">**查看新功能**</a> 

### 安装和使用 
* 安装 
``` 
pip install tkchart 
``` 

* 使用 
``` python
import tkchart 
``` 

</div>

---

<div id="parameter_img"> 

### 参数概述 

<div align="center"> 

<picture> 
<source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1J4XKj5-cVWxUTeS7zHkJvewOmISLVU6Y&sz=w2500"> 
<img src="https://drive.google.com/thumbnail?id=1CqZ2NZsJrrLKUgyzyVgoEREQuuai6Yha&sz=w2500"> 
</picture> 

</div> 

</div> 

---

### 要使用 tkchart 显示数据，您需要执行以下三步： 
1. <a href="#create-line-chart">**创建折线图**</a> 
2. <a href="#create-line">**创建一条线**</a> 
3. <a href="#display-data">**数据显示**</a> 


---

<div id="create-line-chart"> 

## 1 . 创建折线图 
<a href="#create-line">**创建一条线**</a> | <a href="#display-data">**数据显示**</a> 

``` python
linechart = tkchart.LineChart() 
``` 

### 参数 

| 参数                                                          | 必备参数 / 可选参数 | 描述                 | 数据类型                            | 示例值                                 | 
|-------------------------------------------------------------|-------------|--------------------|---------------------------------|-------------------------------------| 
| master                                                      | ***必须***    | 折线图主体              | ``widget``                      | widget                              | 
| <a href="#x_y_axis_values">y_axis_values</a>                | ***必须***    | y 轴的最小值和最大值        | ``tuple[[int \| float], ...]``  | (-1000, 1000), ...                  | 
| <a href="#x_y_axis_values">x_axis_values</a>                | ***必须***    | x 轴的值              | ``tuple[any, ...]``             | (1, 2, 3, 4, 5), ...                | 
| width                                                       | ***可选***    | 折线图的宽度             | ``int``                         | 300, ...                            | 
| height                                                      | ***可选***    | 折线图的高度             | ``int``                         | 100, ...                            | 
| <a href="#parameter_img">axis_size</a>                      | ***可选***    | 坐标轴宽度              | ``int``                         | 1<=                                 | 
| <a href="#parameter_img">axis_color</a>                     | ***可选***    | 坐标轴轴颜色             | ``str``                         | "#2C2C2C" , "blue", ...             | 
| <a href="#parameter_img">bg_color</a>                       | ***可选***    | 折线图的背景色            | ``str``                         | "#191919", ...                      | 
| <a href="#parameter_img">fg_color</a>                       | ***可选***    | 折线图的前景色            | ``str``                         | "#191919", ...                      | 
| <a href="#x_y_data">data_font_style</a>                     | ***可选***    | 坐标轴名称的字体样式         | ``tuple[str, int, str]``        | ("arial", 9, "bold"), ...           | 
| <a href="#x_y_font_style">axis_font_style</a>               | ***可选***    | 坐标轴文字的字体样式         | ``tuple[str, int, str]``        | ("arial", 8, "normal"), ...         | 
| <a href="#x_y_data">x_axis_data</a>                         | ***可选***    | x_data 的值（x 坐标轴名称） | ``str``                         | "X", ...                            | 
| <a href="#x_y_data">y_axis_data</a>                         | ***可选***    | y_data 的值（y 坐标轴名称） | ``any``                         | "Y", ...                            | 
| <a href="#x_y_data">x_axis_data_font_color</a>              | ***可选***    | x_data 的字体颜色       | ``str``                         | "#707070", ...                      | 
| <a href="#x_y_data">y_axis_data_font_color</a>              | ***可选***    | y_data 的字体颜色       | ``str``                         | "#707070", ...                      | 
| <a href="#data_position">x_axis_data_position</a>           | ***可选***    | x_data 的排布方式       | ``str`` ("top", "side")         | "top"                               | 
| <a href="#data_position">y_axis_data_position</a>           | ***可选***    | y_data 的排布方式       | ``str`` ("top", "side")         | "top"                               | 
| <a href="#x_y_section">x_axis_section_count</a>             | ***可选***    | x 轴上的网格线数          | ``int``                         | 0<=                                 | 
| <a href="#x_y_section">y_axis_section_count</a>             | ***可选***    | y 轴上的网格线数          | ``int``                         | 0<=                                 | 
| <a href="#x_y_label_count">x_axis_label_count</a>           | ***可选***    | x 轴标签数量            | ``int``                         | 0<=                                 | 
| <a href="#x_y_label_count">y_axis_label_count</a>           | ***可选***    | y 轴标签数量            | ``int``                         | 1<=                                 | 
| <a href="#x_y_font_style">x_axis_font_color</a>             | ***可选***    | x 轴标签的字体颜色         | ``str``                         | "#606060", ...                      | 
| <a href="#x_y_font_style">y_axis_font_color</a>             | ***可选***    | y 轴标签的字体颜色         | ``str``                         | "#606060", ...                      | 
| <a href="#x_y_section_style">x_axis_section_style</a>       | ***可选***    | x 轴上的网格线样式         | ``str`` ("normal", "dashed")    | "normal"                            | 
| <a href="#x_y_section_style">y_axis_section_style</a>       | ***可选***    | y 轴上的网格线样式         | ``str`` ("normal", "dashed")    | "normal"                            | 
| <a href="#x_y_section_style">x_axis_section_style_type</a>  | ***可选***    | x 轴上网格线的实线与空白的尺寸   | ``tuple[int, int]``             | (100, 50) , (50,50), ...            | 
| <a href="#x_y_section_style">y_axis_section_style_type</a>  | ***可选***    | y 轴上网格线的实线与空白的尺寸   | ``tuple[int, int]``             | (100, 50)                           | 
| <a href="#x_y_section">x_axis_section_color</a>             | ***可选***    | x 轴上网格线的颜色         | ``str``                         | "#2C2C2C", ...                      | 
| <a href="#x_y_section">y_axis_section_color</a>             | ***可选***    | y 轴上网格线的颜色         | ``str``                         | "#2C2C2C"                           | 
| <a href="#y_precision">y_axis_precision</a>                 | ***可选***    | y 轴值的精度            | ``int``                         | 0<=                                 | 
| <a href="#indices_view">x_axis_display_values_indices</div> | ***可选***    | 显示在 x 轴上的坐标值的索引    | ``tuple[int, ...]``             | (0, 1, 2, 3, 4, 5), ...             | 
| <a href="#x_axis_point_spacing">x_axis_point_spacing</a>    | ***可选***    | 线条宽度               | ``int`` \| ``str`` "auto"       | "auto" <br> 1<=                     | 
| <a href="#parameter_img">x_space</a>                        | ***可选***    | x 轴和图表区域之间的空间      | ``int``                         | 0<=                                 | 
| <a href="#parameter_img">y_space</a>                        | ***可选***    | y 轴和图表区域之间的空间      | ``int``                         | 0<=                                 | 
| pointer_state                                               | ***可选***    | 鼠标状态               | ``str`` ("enabled", "disabled") | "disabled"                          | 
| pointing_callback_function                                  | ***可选***    | 鼠标的回调函数            | ``callable``                    | function(*args) <br> function(x, y) | 
| pointer_color                                               | ***可选***    | 鼠标颜色               | ``str``                         | "#606060", ...                      | 
| pointing_values_precision                                   | ***可选***    | 指向值的精度             | ``int``                         | 0<=                                 | 
| pointer_lock                                                | ***可选***    | 鼠标锁状态              | ``str`` ("enabled", "disabled") | "enabled"                           | 
| pointer_size                                                | ***可选***    | 鼠标显示线的宽度           | ``int``                         | 1<=                                 | 


---

### 方法 

| 方法                         | 描述                  | 支持的参数 / 必须的参数                                                                                                                    | 返回类型     | 
|----------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------|----------| 
| configure                  | 更改 LineChart（折线图）属性 | 所有属性，除了 master                                                                                                                   | ``None`` | 
| configure_width | 配置折线图的宽度 | width: `int` | `None` |
| configure_height | 配置折线图的高度 | height: `int` | `None` |
| configure_axis_size | 配置坐标轴宽度 | axis_size: `int` | `None` |
| configure_bg_color | 配置折线图的背景色 | bg_color: `str` | `None` |
| configure_fg_color | 配置折线图的前景色 | fg_color: `str` | `None` |
| configure_axis_color | 配置坐标轴轴颜色 | axis_color: `str` | `None` |
| configure_data_font_style | 配置坐标轴名称的字体样式 | data_font_style: `Tuple[str, int, str]` | `None` |
| configure_axis_font_style | 配置坐标轴文字的字体样式 | axis_font_style: `Tuple[str, int, str]` | `None` |
| configure_y_axis_values | 配置 y 轴的最小值和最大值 | y_axis_values: `Tuple[int \| float, ...]` | `None` |
| configure_y_axis_precision | 配置 y 轴值的精度 | y_axis_precision: `int` | `None` |
| configure_y_axis_font_color | 配置 y 轴标签的字体颜色 | y_axis_font_color: `str` | `None` |
| configure_y_axis_data_font_color | 配置 y_data 的字体颜色 | y_axis_data_font_color: `str` | `None` |
| configure_y_axis_label_count | 配置 y 轴标签数量 | y_axis_label_count: `int` | `None` |
| configure_y_axis_data | 配置 y_data 的值（y 坐标轴名称） | y_axis_data: `any` | `None` |
| configure_y_axis_data_position | 配置 y_data 的排布方式 | y_axis_data_position: `str` | `None` |
| configure_y_axis_section_count | 配置 y 轴上的网格线数 | y_axis_section_count: `int` | `None` |
| configure_y_axis_section_color | 配置 y 轴上网格线的颜色 | y_axis_section_color: `str` | `None` |
| configure_y_axis_section_style | 配置 y 轴上的网格线样式 | y_axis_section_style: `str` | `None` |
| configure_y_axis_section_style_type | 配置 y 轴上网格线的实线与空白的尺寸 | y_axis_section_style_type: `Tuple[int, int]` | `None` |
| configure_y_space | 配置 y 轴和图表区域之间的空间 | y_space: `int` | `None` |
| configure_x_axis_data | 配置 x_data 的值（x 坐标轴名称） | x_axis_data: `str` | `None` |
| configure_x_axis_data_position | 配置 x_data 的排布方式 | x_axis_data_position: `str` | `None` |
| configure_x_axis_font_color | 配置 x 轴标签的字体颜色 | x_axis_font_color: `str` | `None` |
| configure_x_axis_data_font_color | 配置 x_data 的字体颜色 | x_axis_data_font_color: `str` | `None` |
| configure_x_axis_label_count | 配置 x 轴标签数量 | x_axis_label_count: `int` | `None` |
| configure_x_axis_section_count | 配置 x 轴上的网格线数 | x_axis_section_count: `int` | `None` |
| configure_x_axis_section_color | 配置 x 轴上网格线的颜色 | x_axis_section_color: `str` | `None` |
| configure_x_axis_section_style | 配置 x 轴上的网格线样式 | x_axis_section_style: `str` | `None` |
| configure_x_axis_section_style_type | 配置 x 轴上网格线的实线与空白的尺寸 | x_axis_section_style_type: `Tuple[int, int]` | `None` |
| configure_x_axis_display_values_indices | 配置显示在 x 轴上的坐标值的索引 | x_axis_display_values_indices: `Tuple[int, ...]` | `None` |
| configure_x_axis_point_spacing | 配置线条宽度 | x_axis_point_spacing: `int \| str` | `None` |
| configure_x_space | 配置 x 轴和图表区域之间的空间 | x_space: `int` | `None` |
| configure_pointer_state | 配置鼠标状态 | pointer_state: `str` | `None` |
| configure_pointer_color | 配置鼠标颜色 | pointer_color: `str` | `None` |
| configure_pointer_size | 配置鼠标显示线的宽度 | pointer_size: `int` | `None` |
| configure_pointer_lock | 配置鼠标锁状态 | pointer_lock: `str` | `None` |
| configure_pointing_values_precision | 配置指向值的精度 | pointing_values_precision: `int` | `None` |
| configure_pointing_callback_function | 配置鼠标的回调函数 | pointing_callback_function: `callable` | `None` |
| [show_data](#display-data) | 显示数据                | data: ``list``<br> line: ``chart.Line``                                                                                          | ``None`` | 
| place                      | 放置 (place) 折线图      | x: ``int``<br>y: ``int``<br>rely: ``float or int``<br>relx: ``float or int``<br>anchor: ``str``                                  | ``None`` | 
| pack                       | 放置 (pack) 折线图       | pady: ``int``<br>padx: ``int``<br> before: ``widget``<br> after: ``widget``<br>side: ``str``<br>anchor: ``str``                  | ``None`` | 
| grid                       | 放置 (grid) 折线图       | column: ``int``<br>columnspan: ``int``<br>padx: ``int``<br>pady: ``int``<br> row: ``int``<br>rowspan: ``int``<br>sticky: ``str`` | ``None`` | 
| place_forget               | Place 忘编号           | -                                                                                                                                | ``None`` | 
| pack_forget                | Pack 忘编号            | -                                                                                                                                | ``None`` | 
| grid_forget                | Grid 忘编号            | -                                                                                                                                | ``None`` | 
| set_lines_visibility       | 更改所有线条的可见性          | state: ``bool``                                                                                                                  | ``None`` | 
| set_line_visibility        | 更改特定行的可见性           | line: ``tkchart.Line``<br> state: ``bool``                                                                                       | ``None`` | 
| get_line_visibility        | 获取特定生产线的可见性         | line: ``tkchart.Line``                                                                                                           | ``bool`` | 
| reset                      | 重置折线图               | -                                                                                                                                | ``None`` | 
| cget                       | 获取指定参数的值。           | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``  | 
| place_info                 | 获取地点信息              | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``  | 
| pack_info                  | 获取有关包装的信息           | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``  | 
| grid_info                  | 获取网格信息              | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``  | 
| get_line_area              | 获取特定线的面积         | line: `tkchart.Line` | `float`            |
| get_lines_area             | 获取所有线的面积         | -                  | `float`           |
| clear_data  | 清除图表中所有线的数据，确保只保留最新的可见数据点。如果数据点总数超过最大可见点，则会从每条线的数据中移除旧数据。此方法确保图表仅显示基于最大可见范围的相关数据部分。        | -              | ``None``    |  
| destroy                    | 销毁图表                | -                                                                                                                                | ``None`` | 
| get_lines_data              | 获取指定范围内所有线条的数据点，可以选择步长值。           | start: `int` <br> end: `int` <br> step: `int` | `Dict[tkchart.Line, Tuple[int]]` |  
| get_line_data               | 获取指定范围和步长值下某一条线的数据点。                   | line: `tkchart.Line` <br> start: `int` <br> end: `int`<br> step: `int` | `Tuple[int \| float]` |  
| get_x_axis_visible_point_count | 获取X轴上可见数据点的最大数量。                              | -                                        | `int` |  
| get_lines_visible_data      | 获取所有线条当前可见的数据点，基于最大数据长度和可见点数。 | -                                        | `Dict[tkchart.Line, Tuple[int \| float]]` |  
| get_line_visible_data       | 获取某一条线当前可见的数据点。                             | line: `tkchart.Line`                  | `Tuple[int \| float]` |  

</div> 

---

<div id="create-line"> 

## 2 . 创建一条线 

<a href="#create-line-chart">**创建折线图**</a> | <a href="#display-data">**数据显示**</a> 

``` python 
line = tkchart.Line() 
``` 

### 参数 

| 参数名称                                      | 必备参数 / 可选参数 | 描述             | 数据类型                                   | 示例值          | 
|-------------------------------------------|-------------|----------------|----------------------------------------|--------------| 
| master                                    | 必须          | 主控制器           | ``tkchart.Line``                       | LineChart 对象 | 
| [color](#line_color_size)                 | 可选          | 折线颜色           | ``str``                                | "#768df1"    | 
| [size](#line_color_size)                  | 可选          | 折线大小           | ``int``                                | 1<=          | 
| [style](#line_style)                      | 可选          | 折线样式（普通、虚线、点线） | ``str`` ("normal", "dashed", "dotted") | "normal"     | 
| [style_type](#line_style_type)            | 可选          | 实线与虚线尺寸        | ``tuple[int, int]``                    | (10, 5) 等    | 
| [point_highlight](#point_highlight)       | 可选          | 端点高亮状态         | ``str`` ("enabled", "disabled")        | "disabled"   | 
| [point_highlight_size](#point_highlight)  | 可选          | 高亮点大小          | ``int``                                | 1<=          | 
| [point_highlight_color](#point_highlight) | 可选          | 高亮点颜色          | ``str``                                | "#768df1"    | 
| [fill](#fill)                             | 可选          | 是否启用填充         | ``str`` ("enabled", "disabled")        | "disabled"   | 
| [fill_color](#fill)                       | 可选          | 填充颜色           | ``str``                                | "#5d6db6"    | 

--- 

### 方法 

| 方法             | 描述       | 支持的参数                                    | 返回类型     | 
|----------------|----------|------------------------------------------|----------| 
| configure      | 更改折线属性  | 所有属性，除了 master                           | ``None`` | 
| configure_color | 配置折线颜色 | color: `str` | `None` |
| configure_size | 配置折线大小 | size: `int` | `None` |
| configure_style | 配置折线样式（普通、虚线、点线） | style: `str` | `None` |
| configure_style_type | 配置实线与虚线尺寸 | style_type: `Tuple[int, int]` | `None` |
| configure_point_highlight | 配置端点高亮状态 | point_highlight: `str` | `None` |
| configure_point_highlight_size | 配置高亮点大小 | point_highlight_size: `int` | `None` |
| configure_point_highlight_color | 配置高亮点颜色 | point_highlight_color: `str` | `None` |
| configure_fill | 配置是否启用填充 | fill: `str` | `None` |
| configure_fill_color | 配置填充颜色 | fill_color: `str` | `None` |
| cget           | 获取指定参数的值 | attribute_name: ``str`` \| "\_\_all\_\_" | ``any``  | 
| reset          | 重置线对象    | -                                        | ``None`` | 
| set_visible    | 改变线条的可见度 | state: ``bool``                          | ``None`` | 
| get_visibility | 获得线路的可见度 | -                                        | ``bool`` | 
| clear_data     | 清除特定线的数据，确保只保留最新的可见数据点。如果线的数据超过最大可见点，则会修剪旧数据。此方法允许每条线独立清除其数据，确保它始终保持在可见范围内。                                                           | -              | ``None``    | 
| destroy        | 破坏线      | -                                        | ``None`` | 
| get_data                   | 获取指定范围的数据点，可以选择步长值。如果没有提供参数，将返回所有可用数据。 | start: `int` <br> end: `int` <br> step: `int` | `Tuple[int \| float]` |  
| get_current_visible_data    | 根据所有线条的最大数据长度和最大可见点数，返回当前可见的数据点。 | -                                        | `Tuple[int \| float]` |  
| get_x_axis_visible_point_count | 获取X轴上可见数据点的最大数量。                              | -                                        | `int` |   

</div> 

---

<div id="display-data"> 

## 3 . 数据显示 

<a href="#create-line-chart">**创建折线图**</a> | <a href="#create-line">**创建一条折线**</a> 


``` python 
import tkinter as tk 
import tkchart 
import random 

## root 
root = tk.Tk() 
root.configure(bg="#151515") 

## 创建折线图 
chart = tkchart.LineChart(
    master=root, 
    x_axis_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 
    y_axis_values = (-100,100)
) 
chart.pack() 

## 创建一条折线 
line = tkchart.Line(master=chart) 

data = [x for x in range(-100,101)] #values -100 to 100 
## 显示数据（随机） 
def loop(): 
    chart.show_data(line=line, data=random.choices(data, k=1)) 
    root.after(500, loop) 
loop() 

root.mainloop() 
``` 

<div align="center"> 

https://github.com/Thisal-D/tkchart/assets/93121062/64440c23-63e6-4093-b027-21b00a6f5518 

---

</div> 

</div> 


<div id="parameter_explanation"> 

<a href="#top">**返回顶部**</a> | <a href="#howtouse">**使用指南**</a> | <a href="#example">**例子**</a> | <a href="../CHANGES_zh.md">**查看新功能**</a> 

## 参数说明 

<div id="x_y_axis_values"> 

### LineChart 

- #### y_axis_values 
    y_axis_values 是一个包含两个数值的元组。第一个值（索引 0）表示 y 轴的起始值，第二个值（索引 1）表示 y 轴的结束值。该元组定义了折线图上沿 y 轴显示的值的范围。 

- #### x_axis_values 
    x_axis_values 是可以包含任何数据类型的值的集合。这些值被分配给 x 轴，从索引 0 开始一直到 x_axis_values 元组的最后一个索引。元组中的每个值对应于折线图中 x 轴上的一个点。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1GBmf8GaiQG_zJbsYBqfAW7jYgGh7oKCr&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=1UbyQEKDYhZjUI9VttKerpSVc6hZoEfi8&sz=w950" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget,
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100) 
    ) 
    ``` 

---

</div> 

<div id="x_y_data"> 

- #### x_axis_data 
    指折线图 x 轴上显示的值类型。 
    **注意："X"为默认值。** 

- #### y_axis_data 
    指折线图 y 轴上显示的值类型。 
    **注意："Y" 是默认值。** 

- #### x_axis_data_font_color 
    指应用于表示折线图 x_axis_data 的标签的字体颜色。 

- #### y_axis_data_font_color 
    指应用于表示折线图 y_axis_data 的标签的字体颜色。 

- #### data_font_style 
    指应用于代表折线图 x_axis_data 和 y_axis_data 的标签的字体样式。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1-F7IvqoT0Cl73_F2hvf9Gnbi9gM0I9cN&sz=w1000"> 
    <img src="https://drive.google.com/thumbnail?id=1m2kBnDRycSviMXO3uTHIzL6Y7S7u1rsC&sz=w1000" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        y_axis_data="Y data" , 
        x_axis_data="X data", 
        x_axis_data_font_color="#ff0000", 
        y_axis_data_font_color="#00ff00", 
        data_font_style=("arial", 15, "underline") 
    ) 
    ``` 

---

</div> 

<div id="x_y_label_count"> 

- #### x_axis_label_count 
    当您有一组 x_value（例如从 2018 年到 2025 年）时，通常会显示所有这些标签。但有时为了更清晰起见，您可能只想显示其中的几个。 <br> 
    例如，如果您将 x_axis_label_count 设置为 4，则意味着您只想显示 4 个标签，而不是全部 8 个。因此，折线图将自动跳过一些标签以适合您指定的数量。 <br> 
    **注意：len(<a href="#x_y_axis_values">x_axis_values</a>) 是默认值。**<br> 
    换句话说，调整 x_axis_label_count 可以让您控制 x 轴上显示的标签数量，使您的可视化更清晰、更易于理解。 
    <br> 
    -**如果有 9 个标签，您可以将其限制为：3、1。** 
    -**如果有 20 个标签，您可以将其限制为：10, 5, 4, 2, 1。** 
    -**如果有 15 个标签，您可以将其限制为：5、3、1。** 

    #### 在某些情况下，使用 x_axis_label_count 参数可能不足以满足您的需求。在这种情况下，您可以利用 <a href="#indices_view">x_axis_display_values_indices</a> 参数来精确控制 x 轴上显示的值。 

- #### y_axis_label_count 
    默认情况下，如果将 y 轴值设置为 -100 到 100 范围，则 y 轴上将仅显示极值（-100 和 100 两个数字）。但是，您可以选择使用 y_axis_label_count 参数调整显示的标签数量。<br> 
    例如，如果将 y_axis_label_count 设置为 3，系统会将 y 轴范围（-100 到 100）划分为相等的间隔，并按这些间隔显示标签。因此，对于本例，标签计数为 3，您可能会看到 -100、0 和 100 处的标签。<br> 
    总之，调整 y_axis_label_count 参数允许您控制 y 轴上显示的标签数量，从而可以根据您的偏好和要求灵活地自定义可视化效果。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1mecucNsfolJPIAiGU4oX2idc_-tc2yPB&sz=w1000"> 
    <img src="https://drive.google.com/thumbnail?id=1mHgbpbaWQeQE-ykFwIizd_vIdLVSXc5w&sz=w1000" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget,
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_label_count=4, 
        y_axis_label_count=10
    ) 
    ``` 

---

</div> 

<div id="indices_view"> 

- #### x_axis_display_values_indices 
    假设您有一组代表从 2018 年到 2025 年的 x 轴值：(2018、2019、2020、2021、2022、2023、2024、2025)。通常，所有这些值都会显示在 x 轴上。<br> 
    但是，在某些情况下，您可能只想显示特定年份而不是全部。在这种情况下，您可以使用 x_axis_display_values_indices 参数来控制在 x 轴上显示哪些值。<br> 
    例如，如果您只想显示 2019 年、2022 年和 2025 年，则可以在 x_axis_display_values_indices 参数中指定它们的索引。因此，如果 2019 年的索引为 1、2022 年为 4、2025 年为 7（假设基于 0 的索引），则您可以将 x_axis_display_values_indices 设置为 (1, 4, 7)。<br> 
    这样，通过设置要显示的值的索引，您可以精确控制可视化中 X 轴上显示的值，从而允许您根据您的特定要求对其进行定制。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=122KUh1KoOSXx3Eb7U_QINSkdKvgoEiJ_&sz=w800"> 
    <img src="https://drive.google.com/thumbnail?id=1gN_DhzFPzs-7LTG7-EfeZzjisWDTFYSn&sz=w800" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_display_values_indices=(1, 4, 7)
    ) 
    ``` 

---

</div> 

<div id="data_position"> 

- #### x_axis_data_position 
    x_axis_data_position 参数确定 x_axis_data 的文字布局。
    
    它有两个支持的值：
    - "top"
    - "side"

    **注意：“top”是默认位置** 

- #### y_axis_data_position 
    y_axis_data_position 参数确定 y_axis_data 的文字布局。

    它有两个支持的值：
    - "top"
    - "side"

    **注意：“top”是默认位置**

    <br> 

    在"top"、"side"之间进行选择分别确定 x/y_axis_data 是水平放置在数据点上方还是垂直放置在数据点旁边。此参数允许您根据您的喜好和可用空间自定义折线图的布局。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=15QCDaKjOQP83AeqaWuoFxiAbL8XCW4bg&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=18W70YdLf8f6n1K69GhKP_Es69JF-Va3L&sz=w950" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_data_position="side", 
        y_axis_data_position="top" 
    ) 
    ``` 

---

</div> 

<div id="y_precision"> 

- #### y_axis_precision 
    y_axis_ precision 参数控制 y 轴上的值显示的小数位数。<br> 
    **注意：1 是默认精度**<br> 
    例如： 
    - 如果将 y_axis_precision 设置为 0，则 y 轴上的值将显示为整数。<br> 
    - 如果将 y_axis_precision 设置为 1，则 y 轴上的值将显示一位小数。<br> 
    - 如果将 y_axis_precision 设置为 2，则 y 轴上的值将显示两位小数。 
    <br> 

    此外 : 
    - **调整 y_axis_ precision 参数允许您控制折线图中 y 轴值的精度级别。当处理需要特定精度的数据或当您想要通过减少显示的小数位数来提高折线图的可读性时，此参数特别有用。** 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=10j8-iuQ4URQcHNKX3f-eCqxW8Sl0Dn9i&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=1B6e3yf6cPBuQvqpoleIR8syR0_WLmB1x&sz=w950" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        y_axis_label_count=12, 
        y_axis_precision=4, 
    ) 
    ``` 

---

</div> 

<div id="x_y_font_style"> 

- #### axis_font_style 
    指 x 和 y 轴值的字体样式 

- #### x_axis_font_color 
    指 x 轴值的颜色 

- #### y_axis_font_color 
    指 y 轴值的颜色 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1qFDqT8Vb9sxAozyKuNyEj7YWDo-wDzZv&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=19kfPmQxP9AuDNJuFlM2F3YrDhuF3OnAs&sz=w950" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_font_color="#00FF00", 
        y_axis_font_color="#FF0000", 
        axis_font_style=("arial", 13, "bold") 
    ) 
    ``` 

---

</div> 

<div id="x_y_section"> 

<div id="x_axis_section_count"> 

- #### x_axis_section_count 
    x_axis_section_count 参数定义折线图中 x 轴范围将划分为的部分或间隔的数量。<br> 
    **这里有更清晰的细分：** 
    - 假设 x 轴上有一系列值，例如从 2018 年到 2025 年。默认情况下，此范围可能表示为连续线，没有标记任何特定部分或间隔。 
    - 但是，如果将 x_axis_section_count 设置为一个值，例如 8，则意味着您想要将此 x 轴范围划分为等间距的部分或间隔。每个部分将代表总 x 轴范围的一个子集。 
    - 调整 x_axis_section_count 参数允许您控制折线图中 x 轴的粒度，使查看者更容易解释数据并识别特定间隔内的趋势。 

</div> 

- #### y_axis_section_count 
    y_axis_section_count 参数定义折线图中 y 轴范围将划分为的部分或间隔的数量。<br> 
    **请参阅：<a href="#x_axis_section_count">x_axis_section_count**</a> 了解更多... 

- #### x_axis_section_color 
    指 y 轴网格线的颜色 

- #### y_axis_section_color 
    指 x 轴网格线的颜色 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=11h3KM6OhL2rzRQijHSU4damLgN3_EeWN&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1GoduMuhlvwayY55QvjEwjwrk8np-8ULL&sz=w1050" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_section_count=8, 
        y_axis_section_count=5, 
        x_axis_section_color="#2C2C2C", 
        y_axis_section_color="#2C2C2C" 
    ) 
    ``` 

---

</div> 

<div id="x_y_section_style"> 

<div id="x_section_style"> 

- #### x_axis_section_style 
    x_axis_section_style 参数允许您定义折线图中沿 x 轴的部分的视觉样式。 

    - 支持的样式： 
        - "dashed": 当您将 x_axis_section_style 设置为“dashed”时，沿 x 轴的剖面将使用虚线显示。 
        - "normal": 相反，当 x_axis_section_style 设置为“正常”时，沿 x 轴的截面将使用实线显示。
        <br>

    **注意："normal"是默认样式。** 

</div> 

- #### y_axis_section_style 
    与 x_axis_section_style 工作方式相同， 
    有关更多信息，请参阅 <a href="#x_section_style"> x_axis_section_style </a> 

<div id="x_section_style_type"> 

- #### x_axis_section_style_type 
    x_axis_section_style_type 参数是一个包含两个整数值的元组，指定当 x_axis_section_style 设置为“dashed”时使用的破折号样式。<br> 
    例如:<br> 
    - 如果将 x_axis_section_style_type 设置为 (20, 10)，则意味着： 
        - 每个破折号的宽度为 20 像素。 
        - 破折号之间的间距为 10 
        <br>


    这些值确定用于表示沿 x 轴的部分的虚线或标记的视觉外观。通过调整这些值，您可以根据您的偏好或可视化要求自定义虚线部分的外观。 

</div> 

- #### y_axis_section_style_type 
    与 x_axis_section_style_type 工作相同， 
    请参阅 <a href="#x_section_style_type"> x_axis_section_style_type </a> 了解更多信息 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1TJjAsXkcEk84DPZxUMn_kH10Pc0Yc3PH&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1SOieJLRtMLbIqgqlt-ATRAYRSuOwbrEK&sz=w1050" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_section_count=8, 
        y_axis_section_count=5, 
        x_axis_section_style="dashed", 
        x_axis_section_style_type=(20,10), 
        y_axis_section_style="dashed", 
        y_axis_section_style_type=(20,10), 
    ) 
    ``` 

---

</div> 


<div id="x_axis_point_spacing"> 

- #### x_axis_point_spacing 
    x_axis_point_spacing 参数允许您手动设置 x 轴上点之间的间距，通常以像素为单位测量。但是，如果您不手动设置该参数，则会根据 x_axis_values 的长度自动计算。
    <br> 
    **注意："auto"是默认值。** 
    <br> 

    - 将特定值配置为 x_axis_point_spacing 后，您可以通过将其配置为"auto"来重置值以设置默认值。 
    <br> 
        ``` python 
        chart.configure(
            x_axis_point_spacing="auto"
        ) 
        ``` 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=11oRyaQRFOFFbFTQH6lSsZiLdbLUndweY&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1YZeyRNvsgUKZuLfr8NbqdlKFMWAL9EMf&sz=w1050" > 
    </picture> 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_point_spacing="auto" 
    ) 
    ``` 

    x_axis_point_spacing 参数是根据 x_axis_values 元组的长度自动计算的。这意味着 x 轴上点之间的间距是通过将折线图的宽度除以 x_axis_values 列表的长度来确定的。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1LC0SkXUmKS9N5mx52GE2_ZoafRObrtNv&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1SJvjLOJrfMRcnAwEaPm_yveIhu3gbFS6&sz=w1050" > 
    </picture> 

    当您将 x_axis_point_spacing 参数设置为特定值（例如 40）时，这意味着您已手动将 x 轴上的点之间的间距指定为 40 个单位（例如像素）。在这种情况下，无论 x_axis_values 元组的长度如何，折线图都将在 x 轴上的每个点之间使用用户定义的 40 个单位的间距。 

    ``` python 
    chart = tkchart.LineChart(
        master=any_widget, 
        x_axis_point_spacing=40 
    ) 
    ``` 

---

</div> 

### Line 

<div id="line_color_size"> 

- #### color 
    指的是线条的颜色。 

- #### size 
    指线条的尺寸（粗细）。<br> 
    **注：1 为默认尺寸** 
    <br> 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1pAa1fA9Xp63VB-aCvcoHLyY_Hpa-oRfq&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1iFTyIyVJ2C1HhbaYHOyVx9H_F1UHCW8l&sz=w1050" > 
    </picture> 

    ``` python
    line = tkchart.Line(
        master=chart, 
        color="#30ACC7", 
        size=5 
    ) 
    ``` 

---

</div> 

<div id="line_style"> 

- #### style 
    style 参数允许您定义线条的视觉样式。 
    <br> 
    - 支持的样式： 
        - "dashed": 当样式设置为"dashed"时，折线条显示为虚线。 
        - "dotted": 当样式设置为"dotted"时，折线显示为点虚线。 
        - "normal": 当样式设置为"normal"时，线条显示为实线。
        <br> 
    **注意："normal"是默认样式。** 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1JmL02oCW0iWuXcCMBYlwqs4zlk37ptqp&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1FRATeOC2GRsv4l5nchVopvtUSmUqR-hW&sz=w1050" > 
    </picture> 

    ``` python 
    line = tkchart.Line(
        master=chart, 
        line_style="dashed" 
    ) 
    ``` 

---

</div> 

<div id="line_style_type"> 

- #### style_type 
    style_type 参数是一个包含两个整数值的元组，指定样式设置为"dashed"或"dotted"时使用的破折号和点的样式。 

    例如: 
    - 如果将 style_type 设置为 (20, 10)，则意味着： 
        - 每个破折号的宽度或每个点的大小为 20 像素。 
        - 破折号或点之间的间距为 10 个像素。 

    **注意 在"dotted"风格下 , size 参数无关紧要，因为点的大小是由 style_type 元组确定的固定大小。**<br> 
    **注意 在"normal"风格下，style_type 参数无效。** 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1V3bEduu9-5IZDJR6ONxep2SIKBe_gYGp&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1AK70nKWqZ04frfx90YB6wqzYjEmQoZqF&sz=w1050" > 
    </picture> 

    ``` python 
    line = tkchart.Line(
        master=chart, 
        line_style="dashed", 
        line_style_type=(10,2) 
    ) 
    ``` 

---

</div> 

<div id="point_highlight"> 

- #### point_highlight 
    point_highlight 参数用于控制点高亮。 
    <br> 
    - 支持的值： 
        - "enabled": 启用点高亮显示。 
        - "disabled": 禁用点高亮显示。 

- #### point_highlight_size 
    point_highlight_size 用于设置高亮点的大小。 

- #### point_highlight_color 
    高亮点的颜色。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1HJHapDIDYKstmGKekFHEA4-xxw5Ez-Vi&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1WmHPyqtt6W1DQVtmM0beYE6S800x_Hfh&sz=w1050" > 
    </picture> 

    ``` python 
    line = tkchart.Line(
        master=chart, 
        point_highlight="enabled", 
        point_highlight_color="#80CCFF", 
        point_highlight_size=8 
    ) 
    ``` 

---

</div> 

<div id="fill"> 

- #### fill 
    fill 参数用于控制是否启用或禁用行填充。 
    <br> 
    - 支持的值： 
        - "enabled": 启用线条填充。 
        - "disabled": 禁用线条填充。
    
- #### fill_color 
    fill_color 参数用于指定填充的颜色。 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1j7tjTNZSqr7frhbuUPpc_gktl_7Fp7cg&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=1Un5x0Aetoq0LUE6piGPjsCoJt1mpjxCE&sz=w950" > 
    </picture> 

    ``` python 
    line = tkchart.Line(
        master=chart, 
        fill="enabled", 
        fill_color="#5D6DB6" 
    ) 
    ``` 

</div> 

---

<div id="example"> 

<a href="#top">**回到顶部**</a> | <a href="#howtouse">**使用指南**</a> | <a href="#parameter_explanation">**参数说明**</a> | <a href="../CHANGES_zh.md">**查看新功能**</a> 

## [例子](https://github.com/Thisal-D/tkchart/tree/main/template(s))

<div align="center"> 

<img src="https://drive.google.com/thumbnail?id=1PoDTZqd2SZG7mNVBJgmpVBHGLaG-vH7K&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1BhX8vEuLFysgFh8jyfWuWX-bYLb_qqfS&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1rA4Fe9fog7ny841IBnJNedScY936EoQT&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1-BOYqyb8ixX2VbpseDkJOpKBABnGAJZf&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1AknbWhYCDYZ03M--zKaJhNcCoTOyhL9K&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=17flH38q_0Z9S3Gep20dqZi-tCUO79L62&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1EK8GKI-_E9pkQwgLdywWMm9uqJoEl_FO&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1ex0cdh_Ml4duZ8taYOB04rsX8CLl88i9&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1ghuhCoz7srDme8_2b3DFUfxnxVsd8-hP&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1WFunUzibiEopRqZjaJD9DLsoln9YAa8B&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1NwTavf0nuUAjR0qJfIzo3dfBoNKSsQ8S&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1oMUERN5WDApzRlnNul00VUrbd-Ty7fPW&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1hgssGvZLUGkZ_knFtcf82f-TS7seeHZm&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1JsI0L4BmbyPGihnnZ2s3mpYOcmkpIaJU&sz=w720" style="width: 50%"> 

</div> 

</div> 
    
---

## 链接 

**PyPi.org** : <a href="https://pypi.org/project/tkchart" target="_blank" ><i>tkchart</i></a> 

**GitHub.com** : <a href="https://github.com/Thisal-D/tkchart" target="_blank" ><i>tkchart</i></a> 

---

### 翻译贡献 

**翻译支持** : [有语](https://github.com/childeyouyu) 

**Translation by** : [youyu](https://github.com/childeyouyu) 