[![Language](https://img.shields.io/badge/Language-English-blue)](CHANGES_en.md)

## v2.2.0

- ### 新方法添加到 `LineChart` 对象  
    | 方法名                        | 描述                                                        | 参数                                       | 返回类型      |  
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|  
    | `configure_width` | 配置折线图的宽度 | width: `int` | `None` |
    | `configure_height` | 配置折线图的高度 | height: `int` | `None` |
    | `configure_axis_size` | 配置坐标轴宽度 | axis_size: `int` | `None` |
    | `configure_bg_color` | 配置折线图的背景色 | bg_color: `str` | `None` |
    | `configure_fg_color` | 配置折线图的前景色 | fg_color: `str` | `None` |
    | `configure_axis_color` | 配置坐标轴轴颜色 | axis_color: `str` | `None` |
    | `configure_data_font_style` | 配置坐标轴名称的字体样式 | data_font_style: `Tuple[str, int, str]` | `None` |
    | `configure_axis_font_style` | 配置坐标轴文字的字体样式 | axis_font_style: `Tuple[str, int, str]` | `None` |
    | `configure_y_axis_values` | 配置 y 轴的最小值和最大值 | y_axis_values: `Tuple[int \| float, ...]` | `None` |
    | `configure_y_axis_precision` | 配置 y 轴值的精度 | y_axis_precision: `int` | `None` |
    | `configure_y_axis_font_color` | 配置 y 轴标签的字体颜色 | y_axis_font_color: `str` | `None` |
    | `configure_y_axis_data_font_color` | 配置 y_data 的字体颜色 | y_axis_data_font_color: `str` | `None` |
    | `configure_y_axis_label_count` | 配置 y 轴标签数量 | y_axis_label_count: `int` | `None` |
    | `configure_y_axis_data` | 配置 y_data 的值（y 坐标轴名称） | y_axis_data: `any` | `None` |
    | `configure_y_axis_data_position` | 配置 y_data 的排布方式 | y_axis_data_position: `str` | `None` |
    | `configure_y_axis_section_count` | 配置 y 轴上的网格线数 | y_axis_section_count: `int` | `None` |
    | `configure_y_axis_section_color` | 配置 y 轴上网格线的颜色 | y_axis_section_color: `str` | `None` |
    | `configure_y_axis_section_style` | 配置 y 轴上的网格线样式 | y_axis_section_style: `str` | `None` |
    | `configure_y_axis_section_style_type` | 配置 y 轴上网格线的实线与空白的尺寸 | y_axis_section_style_type: `Tuple[int, int]` | `None` |
    | `configure_y_space` | 配置 y 轴和图表区域之间的空间 | y_space: `int` | `None` |
    | `configure_x_axis_data` | 配置 x_data 的值（x 坐标轴名称） | x_axis_data: `str` | `None` |
    | `configure_x_axis_data_position` | 配置 x_data 的排布方式 | x_axis_data_position: `str` | `None` |
    | `configure_x_axis_font_color` | 配置 x 轴标签的字体颜色 | x_axis_font_color: `str` | `None` |
    | `configure_x_axis_data_font_color` | 配置 x_data 的字体颜色 | x_axis_data_font_color: `str` | `None` |
    | `configure_x_axis_label_count` | 配置 x 轴标签数量 | x_axis_label_count: `int` | `None` |
    | `configure_x_axis_section_count` | 配置 x 轴上的网格线数 | x_axis_section_count: `int` | `None` |
    | `configure_x_axis_section_color` | 配置 x 轴上网格线的颜色 | x_axis_section_color: `str` | `None` |
    | `configure_x_axis_section_style` | 配置 x 轴上的网格线样式 | x_axis_section_style: `str` | `None` |
    | `configure_x_axis_section_style_type` | 配置 x 轴上网格线的实线与空白的尺寸 | x_axis_section_style_type: `Tuple[int, int]` | `None` |
    | `configure_x_axis_display_values_indices` | 配置显示在 x 轴上的坐标值的索引 | x_axis_display_values_indices: `Tuple[int, ...]` | `None` |
    | `configure_x_axis_point_spacing` | 配置线条宽度 | x_axis_point_spacing: `int \| str` | `None` |
    | `configure_x_space` | 配置 x 轴和图表区域之间的空间 | x_space: `int` | `None` |
    | `configure_pointer_state` | 配置鼠标状态 | pointer_state: `str` | `None` |
    | `configure_pointer_color` | 配置鼠标颜色 | pointer_color: `str` | `None` |
    | `configure_pointer_size` | 配置鼠标显示线的宽度 | pointer_size: `int` | `None` |
    | `configure_pointer_lock` | 配置鼠标锁状态 | pointer_lock: `str` | `None` |
    | `configure_pointing_values_precision` | 配置指向值的精度 | pointing_values_precision: `int` | `None` |
    | `configure_pointing_callback_function` | 配置鼠标的回调函数 | pointing_callback_function: `callable` | `None` |

- ### 新方法添加到 `Line` 对象  
    | 方法名                        | 描述                                                        | 参数                                       | 返回类型      |  
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|  
    | `configure_color` | 配置折线颜色 | color: `str` | `None` |
    | `configure_size` | 配置折线大小 | size: `int` | `None` |
    | `configure_style` | 配置折线样式（普通、虚线、点线） | style: `str` | `None` |
    | `configure_style_type` | 配置实线与虚线尺寸 | style_type: `Tuple[int, int]` | `None` |
    | `configure_point_highlight` | 配置端点高亮状态 | point_highlight: `str` | `None` |
    | `configure_point_highlight_size` | 配置高亮点大小 | point_highlight_size: `int` | `None` |
    | `configure_point_highlight_color` | 配置高亮点颜色 | point_highlight_color: `str` | `None` |
    | `configure_fill` | 配置是否启用填充 | fill: `str` | `None` |
    | `configure_fill_color` | 配置填充颜色 | fill_color: `str` | `None` |

---
## v2.1.6  

- ### 新方法添加到 `LineChart` 对象  
    | 方法名                        | 描述                                                        | 参数                                       | 返回类型      |  
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|  
    | `get_lines_data`              | 获取指定范围内所有线条的数据点，可以选择步长值。           | start: `int` <br> end: `int` <br> step: `int` | `Dict[tkchart.Line, Tuple[int]]` |  
    | `get_line_data`               | 获取指定范围和步长值下某一条线的数据点。                   | line: `tkchart.Line` <br> start: `int` <br> end: `int`<br> step: `int` | `Tuple[int \| float]` |  
    | `get_x_axis_visible_point_count` | 获取X轴上可见数据点的最大数量。                              | -                                        | `int` |  
    | `get_lines_visible_data`      | 获取所有线条当前可见的数据点，基于最大数据长度和可见点数。 | -                                        | `Dict[tkchart.Line, Tuple[int \| float]]` |  
    | `get_line_visible_data`       | 获取某一条线当前可见的数据点。                             | line: `tkchart.Line`                  | `Tuple[int \| float]` |  

- ### 新方法添加到 `Line` 对象  
    | 方法名                        | 描述                                                        | 参数                                       | 返回类型      |  
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|  
    | `get_data`                   | 获取指定范围的数据点，可以选择步长值。如果没有提供参数，将返回所有可用数据。 | start: `int` <br> end: `int` <br> step: `int` | `Tuple[int \| float]` |  
    | `get_current_visible_data`    | 根据所有线条的最大数据长度和最大可见点数，返回当前可见的数据点。 | -                                        | `Tuple[int \| float]` |  
    | `get_x_axis_visible_point_count` | 获取X轴上可见数据点的最大数量。                              | -                                        | `int` |  


## v2.1.5

- ### 新增方法到 `LineChart` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`  | 清除图表中所有线的数据，确保只保留最新的可见数据点。如果数据点总数超过最大可见点，则会从每条线的数据中移除旧数据。此方法确保图表仅显示基于最大可见范围的相关数据部分。                                                           | -              | `None`    |  

- ### 新增方法到 `Line` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`     | 清除特定线的数据，确保只保留最新的可见数据点。如果线的数据超过最大可见点，则会修剪旧数据。此方法允许每条线独立清除其数据，确保它始终保持在可见范围内。                                                           | -              | `None`    | 

---

## v2.1.4

- ### 新增方法到 `LineChart` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `get_line_area`  | 获取特定线的区域大小                               | line: `tkchart.Line` | `float` | 
    | `get_lines_area` | 获取所有线的区域大小                                   | -                    | `float` | 

---

## v2.1.3

- ### 新增方法到 `LineChart` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | 销毁线图及其所有线               | -              | `None`      |

- ### 新增方法到 `Line` 对象
    | 方法名称      | 描述                                                | 参数     | 返回类型 |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | 销毁线对象                                    | -              | `None`      |

---

## v2.1.2

- ### 新增方法到 `Line` 对象

    | 方法名称      | 描述                                    | 参数                               | 返回类型 |
    |------------------|------------------------------------------------|------------------------------------------|-------------|
    | `cget`           | 获取指定参数的值       | attribute_name: `str \| "__all__"`       | `any`       |
    | `set_visible`    | 更改线的可见性              | state: `bool`                            | `None`      |
    | `get_visibility` | 获取线的可见性                 | -                                        | `bool`      |

- ### 新增方法到 `LineChart` 对象

    | 方法名称            | 描述                                    | 参数                                       | 返回类型 |
    |------------------------|------------------------------------------------|--------------------------------------------------|-------------|
    | `set_lines_visibility` | 更改所有线的可见性         | state: `bool`                                    | `None`      |
    | `set_line_visibility`  | 更改特定线的可见性       | line: `tkchart.Line`<br>state: `bool`            | `None`      |
    | `get_line_visibility`  | 获取特定线的可见性          | line: `tkchart.Line`                             | `bool`      |
    | `cget`                 | 获取指定参数的值       | attribute_name: `str \| "__all__"`               | `any`       |
    | `place_info`           | 获取位置相关信息                           | attribute_name: `str \| "__all__"`               | `any`       |
    | `pack_info`            | 获取打包相关信息                            | attribute_name: `str \| "__all__"`               | `any`       |
    | `grid_info`            | 获取网格相关信息                            | attribute_name: `str \| "__all__"`               | `any`       |

- ### 移除 `LineChart` 对象的方法

    | 方法名称 | 描述          | 参数                                   | 返回类型 |
    |-------------|----------------------|----------------------------------------------|-------------|
    | hide_all    | 隐藏所有的线   | state:  `bool`                             | None        |
    | hide        | 隐藏特定的线 | line:  `tkchart.Line`<br> state:  `bool` | None        |
