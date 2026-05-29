[![Chinese](https://img.shields.io/badge/Language-中文-red)](CHANGES_zh.md)


## v2.2.0

- ### New Methods Added to `LineChart` Object
    | Method Name                  | Description                                                | Parameters                               | Return Type      |
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|
    | `configure_width` | Configure the width of the chart | width: `int` | `None` |
    | `configure_height` | Configure the height of the chart | height: `int` | `None` |
    | `configure_axis_size` | Configure the size of the axis | axis_size: `int` | `None` |
    | `configure_bg_color` | Configure the background color of the chart | bg_color: `str` | `None` |
    | `configure_fg_color` | Configure the foreground color of the chart | fg_color: `str` | `None` |
    | `configure_axis_color` | Configure the color of the axis | axis_color: `str` | `None` |
    | `configure_data_font_style` | Configure the font style for data labels | data_font_style: `Tuple[str, int, str]` | `None` |
    | `configure_axis_font_style` | Configure the font style for axis labels | axis_font_style: `Tuple[str, int, str]` | `None` |
    | `configure_y_axis_values` | Configure the minimum and maximum values for y-axis | y_axis_values: `Tuple[int \| float, ...]` | `None` |
    | `configure_y_axis_precision` | Configure the precision for y-axis values | y_axis_precision: `int` | `None` |
    | `configure_y_axis_font_color` | Configure the font color for y-axis labels | y_axis_font_color: `str` | `None` |
    | `configure_y_axis_data_font_color` | Configure the font color for y-axis data label | y_axis_data_font_color: `str` | `None` |
    | `configure_y_axis_label_count` | Configure the number of y-axis labels | y_axis_label_count: `int` | `None` |
    | `configure_y_axis_data` | Configure the value for y-axis data label | y_axis_data: `any` | `None` |
    | `configure_y_axis_data_position` | Configure the position of y-axis data label | y_axis_data_position: `str` | `None` |
    | `configure_y_axis_section_count` | Configure the number of sections on the y-axis | y_axis_section_count: `int` | `None` |
    | `configure_y_axis_section_color` | Configure the color of sections on the y-axis | y_axis_section_color: `str` | `None` |
    | `configure_y_axis_section_style` | Configure the style of sections on the y-axis | y_axis_section_style: `str` | `None` |
    | `configure_y_axis_section_style_type` | Configure the style type for sections on the y-axis | y_axis_section_style_type: `Tuple[int, int]` | `None` |
    | `configure_y_space` | Configure the space between y-axis and chart area | y_space: `int` | `None` |
    | `configure_x_axis_data` | Configure the data label for x-axis | x_axis_data: `str` | `None` |
    | `configure_x_axis_data_position` | Configure the position of x-axis data label | x_axis_data_position: `str` | `None` |
    | `configure_x_axis_font_color` | Configure the font color for x-axis labels | x_axis_font_color: `str` | `None` |
    | `configure_x_axis_data_font_color` | Configure the font color for x-axis data label | x_axis_data_font_color: `str` | `None` |
    | `configure_x_axis_label_count` | Configure the number of x-axis labels | x_axis_label_count: `int` | `None` |
    | `configure_x_axis_section_count` | Configure the number of sections on the x-axis | x_axis_section_count: `int` | `None` |
    | `configure_x_axis_section_color` | Configure the color of sections on the x-axis | x_axis_section_color: `str` | `None` |
    | `configure_x_axis_section_style` | Configure the style of sections on the x-axis | x_axis_section_style: `str` | `None` |
    | `configure_x_axis_section_style_type` | Configure the style type for sections on the x-axis | x_axis_section_style_type: `Tuple[int, int]` | `None` |
    | `configure_x_axis_display_values_indices` | Configure the indices of values to display on the x-axis | x_axis_display_values_indices: `Tuple[int, ...]` | `None` |
    | `configure_x_axis_point_spacing` | Configure the spacing between points on the x-axis | x_axis_point_spacing: `int \| str` | `None` |
    | `configure_x_space` | Configure the space between x-axis and chart area | x_space: `int` | `None` |
    | `configure_pointer_state` | Configure the state of the pointer | pointer_state: `str` | `None` |
    | `configure_pointer_color` | Configure the color of the pointer | pointer_color: `str` | `None` |
    | `configure_pointer_size` | Configure the size of the pointer | pointer_size: `int` | `None` |
    | `configure_pointer_lock` | Configure the state of pointer lock | pointer_lock: `str` | `None` |
    | `configure_pointing_values_precision` | Configure the precision for pointing values | pointing_values_precision: `int` | `None` |
    | `configure_pointing_callback_function` | Configure the callback function for pointer | pointing_callback_function: `callable` | `None` |

- ### New Methods Added to `Line` Object
    | Method Name                  | Description                                                | Parameters                               | Return Type      |
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|
    | `configure_color` | Configure the color of the line | color: `str` | `None` |
    | `configure_size` | Configure the size of the line | size: `int` | `None` |
    | `configure_style` | Configure the style of the line | style: `str` | `None` |
    | `configure_style_type` | Configure the style type for the line | style_type: `Tuple[int, int]` | `None` |
    | `configure_point_highlight` | Configure the state of point highlighting | point_highlight: `str` | `None` |
    | `configure_point_highlight_size` | Configure the size of the highlighted point | point_highlight_size: `int` | `None` |
    | `configure_point_highlight_color` | Configure the color of the highlighted point | point_highlight_color: `str` | `None` |
    | `configure_fill` | Configure the state of filling | fill: `str` | `None` |
    | `configure_fill_color` | Configure the color of the fill | fill_color: `str` | `None` |

---
## v2.1.6 

- ### New Methods Added to `LineChart` Object  
    | Method Name                  | Description                                                | Parameters                               | Return Type      |  
    |------------------------------|------------------------------------------------------------|------------------------------------------|-----------------|  
    | `get_lines_data`              | Retrieves data points for all lines within a specified range with an optional step value. | start: `int` <br> end: `int` <br> step: `int` | `Dict[tkchart.Line, Tuple[int]]` |  
     `get_line_data`               | Retrieves data points for a specific line within a specified range and step. | line: `tkchart.Line` <br> start: `int` <br> end: `int`<br> step: `int` | `Tuple[int \| float]` |  
    | `get_x_axis_visible_point_count` | Retrieves the maximum number of data points that can be visible along the X-axis. | -                                       | `int` |  
    | `get_lines_visible_data`      | Retrieves currently visible data points for all lines based on the maximum data length and visible points. | -                                       | `Dict[tkchart.Line, Tuple[int \| float]]` |  
    | `get_line_visible_data`       | Retrieves currently visible data points for a specific line. | line: `tkchart.Line`                          | `Tuple[int \| float]` |  



- ### New Methods Added to `Line` Object  
    | Method Name                  | Description                                                | Parameters          | Return Type      |  
    |------------------------------|------------------------------------------------------------|---------------------|-----------------|  
    | `get_data`                   | Retrieves data points from a specified range with an optional step value. If no parameters are given, it returns all available data. | start: `int` <br> end: `int` <br> step: `int` | `Tuple[int \| float]` |  
    | `get_current_visible_data`    | Returns the currently visible data points based on the maximum data length across all lines and the maximum number of visible points. | -                   | `Tuple[int \| float]` |  
    | `get_x_axis_visible_point_count` | Retrieves the maximum number of data points that can be visible along the X-axis. | -                   | `int` |  


## v2.1.5

- ### New Method Added to `LineChart` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`  | Clears the data for all lines within the chart, ensuring that only the most recent visible data points are retained. If the total data points exceed the maximum visible points, the older data is removed from each line's data. This method ensures that the chart displays only the relevant portion of data based on the maximum visible range.                                                           | -              | ``None``    |  

- ### New Method Added to `Line` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `clear_data`     | Clears the data for a specific line, ensuring that only the most recent visible data points are retained. If the line's data exceeds the maximum visible points, the older data is trimmed. This method allows each line to independently clean its data, ensuring it remains within the visible range.                                                           | -              | ``None``    | 

---

## v2.1.4

- ### New Methods Added to `LineChart` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `get_line_area`  | Get the are of specific line                               | line: `tkchart.Line` | ``float`` | 
    | `get_lines_area` | Get the are of all lines                                   | -                    | ``float`` | 

---

## v2.1.3

- ### New Method Added to `LineChart` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | Destroy the line chart, along with its lines               | -              | `None`      |

- ### New Method Added to `Line` Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | Destroy the line object                                    | -              | `None`      |

---

## v2.1.2

- ### New Method Added to `Line` Object

    | Method Name      | Description                                    | Parameters                               | Return Type |
    |------------------|------------------------------------------------|------------------------------------------|-------------|
    | `cget`           | Get the value of the specified parameter       | attribute_name: `str \| "__all__"`       | `any`       |
    | `set_visible`    | Change the visibility of the line              | state: `bool`                            | `None`      |
    | `get_visibility` | Get the visibility of the line                 | -                                        | `bool`      |

- ### New Methods Added to `LineChart` Object

    | Method Name            | Description                                    | Parameters                                       | Return Type |
    |------------------------|------------------------------------------------|--------------------------------------------------|-------------|
    | `set_lines_visibility` | Change the visibility of all the lines         | state: `bool`                                    | `None`      |
    | `set_line_visibility`  | Change the visibility of a specific line       | line: `tkchart.Line`<br>state: `bool`            | `None`      |
    | `get_line_visibility`  | Get the visibility of a specific line          | line: `tkchart.Line`                             | `bool`      |
    | `cget`                 | Get the value of the specified parameter       | attribute_name: `str \| "__all__"`               | `any`       |
    | `place_info`           | Get info about place                           | attribute_name: `str \| "__all__"`               | `any`       |
    | `pack_info`            | Get info about pack                            | attribute_name: `str \| "__all__"`               | `any`       |
    | `grid_info`            | Get info about grid                            | attribute_name: `str \| "__all__"`               | `any`       |

- ### Removed Methods in `LineChart` Object

    | Method Name | Description          | Parameters                                   | Return Type |
    |-------------|----------------------|----------------------------------------------|-------------|
    | hide_all    | Hide all the lines   | state:  ``bool``                             | None        |
    | hide        | hide a specific line | line:  ``tkchart.Line``<br> state:  ``bool`` | None        |