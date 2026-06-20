import tkinter
from typing import Union, List, Tuple, Literal, Any, Callable, Dict
from .Utils import Utils
from .Line import Line
from .Validate import Validate


class LineChart:
    def __init__(
        self,
        master: Any = None,
        width: int = 700,
        height: int = 400,
        axis_size: int = 1,
        
        axis_color: str = "#2C2C2C",
        bg_color: str = "#191919",
        fg_color: str = "#191919",
        data_font_style: Tuple[str, int, str] = ("arial", 9, "bold"),
        axis_font_style: Tuple[str, int, str] = ("arial", 8, "normal"),
        
        y_axis_precision: int = 0,
        y_axis_data: Any = "Y",
        y_axis_label_count: int = 1,
        y_axis_values: Tuple[Union[int, float], Union[int, float]] = (None, None),
        y_axis_font_color: str = "#606060",
        y_axis_data_font_color: str = "#707070",
        y_axis_data_position: Literal["top", "side"] = "top",
        y_axis_section_count: int = 0,
        y_axis_section_style: Literal["normal", "dashed"] = "normal",
        y_axis_section_style_type: Tuple[int, int] = (100, 50),
        y_axis_section_color: str = "#2C2C2C",
        
        x_axis_data: str = "X",
        x_axis_label_count: int = None,
        x_axis_values: Tuple[Any, ...] = (None, "None", None, "None"),
        x_axis_display_values_indices: Tuple[int, ...] = None,
        x_axis_font_color: str = "#606060",
        x_axis_data_font_color: str = "#707070",
        x_axis_data_position: Literal["top", "side"] = "top",
        x_axis_section_count: int = 0,
        x_axis_section_style: Literal["normal", "dashed"] = "normal",
        x_axis_section_style_type: Tuple[int, int] = (100, 50),
        x_axis_section_color: str = "#2C2C2C",
        
        x_axis_point_spacing: Union[int, Literal["auto"]] = "auto",
        y_space: int = 0,
        x_space: int = 0,
        
        pointer_state: Literal["enabled", "disabled"] = "disabled",
        pointing_callback_function: Callable = None,
        pointer_color: str = "#606060",
        pointing_values_precision: int = 1,
        pointer_lock: Literal["enabled", "disabled"] = "disabled",
        pointer_size: int = 1,
        *args: Any,
    ) -> None:
        """
        Initialize a LineChart object.

        Args:
            master (Any): The master object.
            width (int): Width of the LineChart widget.
            height (int): Height of the LineChart widget.
            axis_size (int): Size/thickness of the axis lines.

            axis_color (str): Color of the axis lines.
            bg_color (str): Background color of the LineChart widget.
            fg_color (str): Foreground color of the LineChart widget.
            data_font_style (Tuple[str, int, str]): Font style for data labels.
            axis_font_style (Tuple[str, int, str]): Font style for axis labels.

            y_axis_precision (int): Precision for y-axis values.
            y_axis_data (Any): Data label for the y-axis.
            y_axis_label_count (int): Number of y-axis labels.
            y_axis_values (Tuple[Union[int, float], Union[int, float]]): Range of y-axis values.
            y_axis_font_color (str): Font color for y-axis labels.
            y_axis_data_font_color (str): Font color for y-axis data label.
            y_axis_data_position (str): Position of y-axis data label.
            y_axis_section_count (int): Number of sections in the y-axis.
            y_axis_section_style (str): Style of the y-axis sections.
            y_axis_section_style_type (Tuple[int, int]): Style type for y-axis sections.
            y_axis_section_color (str): Color of the y-axis sections.

            x_axis_data (str): Data label for the x-axis.
            x_axis_label_count (int): Number of x-axis labels.
            x_axis_values (Tuple[Any, ...]): Values for x-axis labels.
            x_axis_display_values_indices (Tuple[int, ...]): Indices of x-axis values to display.
            x_axis_font_color (str): Font color for x-axis labels.
            x_axis_data_font_color (str): Font color for x-axis data label.
            x_axis_data_position (str): Position of x-axis data label.
            x_axis_section_count (int): Number of sections in the x-axis.
            x_axis_section_style (str): Style of the x-axis sections.
            x_axis_section_style_type (Tuple[int, int]): Style type for x-axis sections.
            x_axis_section_color (str): Color of the x-axis sections.

            x_axis_point_spacing (Union[int, str]): Spacing between x-axis points.
            y_space (int): Space between y-axis and LineChart.
            x_space (int): Space between x-axis and LineChart.

            pointer_state (str): State of pointer (enabled/disabled).
            pointing_callback_function (callable): Callback function for pointing.
            pointer_color (str): Color of the pointer.
            pointing_values_precision (int): Precision for pointer values.
            pointer_lock (str): Lock state of the pointer (enabled/disabled).
            pointer_size (int): Size of the pointer.
            
        Raises:
            TypeError: If any of the parameters are of incorrect type.
            ValueError: If any of the parameters have invalid values.
        """
        Validate._is_int(height, "height")
        Validate._is_int(width, "width")
        Validate._is_int(axis_size, "axis_size")
        Validate._is_int(y_space, "y_space")
        Validate._is_int(x_space, "x_space")
        Validate._is_int(y_axis_precision, "y_axis_precision")
        Validate._is_int(y_axis_label_count, "y_axis_label_count")
        Validate._is_int(y_axis_section_count, "y_axis_section_count")
        Validate._is_int(x_axis_section_count, "x_axis_section_count")
        Validate._is_int(pointing_values_precision, "pointing_values_precision")
        Validate._is_int(pointer_size, "pointer_size")
        Validate._is_valid_x_axis_values(x_axis_values, "x_axis_values")
        Validate._is_valid_y_axis_values(y_axis_values, "y_axis_values")
        Validate._is_valid_color(y_axis_section_color, "y_axis_section_color")
        Validate._is_valid_color(x_axis_section_color, "x_axis_section_color")
        Validate._is_valid_color(axis_color, "axis_color")
        Validate._is_valid_color(bg_color, "bg_color")
        Validate._is_valid_color(fg_color, "fg_color")
        Validate._is_valid_color(y_axis_font_color, "y_axis_font_color")
        Validate._is_valid_color(x_axis_font_color, "x_axis_font_color")
        Validate._is_valid_color(y_axis_data_font_color, "y_axis_data_font_color")
        Validate._is_valid_color(x_axis_data_font_color, "x_axis_data_font_color")
        Validate._is_valid_color(pointer_color, "pointer_color")
        Validate._is_valid_font(data_font_style, "data_font_style")
        Validate._is_valid_font(axis_font_style, "axis_font_style")
        Validate._is_valid_data_position(y_axis_data_position, "y_axis_data_position")
        Validate._is_valid_data_position(x_axis_data_position, "x_axis_data_position")
        Validate._is_valid_style_type(y_axis_section_style_type, "y_axis_section_style_type")
        Validate._is_valid_style_type(x_axis_section_style_type, "x_axis_section_style_type")
        Validate._is_valid_section_style(y_axis_section_style, "y_axis_section_style")
        Validate._is_valid_section_style(x_axis_section_style, "x_axis_section_style")
        Validate._is_valid_x_axis_point_spacing(x_axis_point_spacing, "x_axis_point_spacing")
        Validate._is_valid_pointer_state_lock(pointer_state, "pointer_state")
        Validate._is_valid_pointer_state_lock(pointer_lock, "pointer_lock")
        Validate._is_valid_function(pointing_callback_function, "pointing_callback_function")
        Validate._is_valid_x_axis_indices(x_axis_values, x_axis_display_values_indices, "x_axis_display_values_indices")
        Validate._is_valid_x_axis_label_count(x_axis_label_count, "x_axis_label_count")

        if master is not None:
            self.__master = master
        elif len(args) != 0:
            self.__master = args[0]
        else:
            self.__master = master

        self.__height: int = height
        self.__width: int = width
        self.__axis_size: int = axis_size
        self.__axis_color: str = axis_color
        self.__x_axis_point_spacing: Union[int, float, Literal["auto"]] = x_axis_point_spacing
        self.__x_axis_point_spacing_handle_by: str = "auto"
        self.__data_font_style: Tuple[str, int, str] = data_font_style
        self.__axis_font_style: Tuple[str, int, str] = axis_font_style
        self.__lines: List[Line] = []
        self.__bg_color: str = bg_color
        self.__fg_color: str = fg_color
        self.__y_axis_font_color: str = y_axis_font_color
        self.__y_axis_data_font_color: str = y_axis_data_font_color
        self.__y_axis_section_color: str = y_axis_section_color
        self.__y_axis_section_style: Literal["normal", "dashed"] = y_axis_section_style
        self.__y_axis_section_style_type: Tuple[int, int] = y_axis_section_style_type
        self.__y_axis_section_count: int = y_axis_section_count
        self.__y_axis_label_count: int = y_axis_label_count
        self.__y_axis_data = str(y_axis_data)
        self.__y_axis_data_position: Literal["top", "side"] = y_axis_data_position
        self.__y_axis_values: Tuple[Union[int, float], Union[int, float]] = y_axis_values
        self.__y_axis_min_value: Union[int, float] = y_axis_values[0]
        self.__y_axis_max_value: Union[int, float] = y_axis_values[1]
        self.__y_axis_precision: int = y_axis_precision
        self.__y_space: int = y_space
        self.__x_axis_font_color: str = x_axis_font_color
        self.__x_axis_data_font_color: str = x_axis_data_font_color
        self.__x_axis_section_color: str = x_axis_section_color
        self.__x_axis_section_style: Literal["normal", "dashed"] = x_axis_section_style
        self.__x_axis_section_style_type: Tuple[int, int] = x_axis_section_style_type
        self.__x_axis_section_count: int = x_axis_section_count
        self.__x_axis_label_count: int = x_axis_label_count
        self.__x_axis_display_values_indices: Tuple[int, ...] = x_axis_display_values_indices
        self.__x_labels_values_index_change: int = 1
        self.__x_axis_data: str = str(x_axis_data)
        self.__x_axis_data_position: Literal["top", "side"] = x_axis_data_position
        self.__x_axis_values: Tuple[Any, ...] = x_axis_values
        self.__x_axis_values_handle_by: str = "label_count"
        self.__x_space: int = x_space
        self.__pointer_state: Literal["enabled", 'disabled'] = pointer_state
        self.__pointing_callback_function: Callable = pointing_callback_function
        self.__pointing_values_precision: int = pointing_values_precision
        self.__pointer_lock: Literal["enabled", 'disabled'] = pointer_lock
        self.__pointer_size: int = pointer_size
        self.__pointer_color: str = pointer_color
        self.__x_values_frame_place_req: bool = True
        self.__y_values_frame_place_req: bool = True

        self.__place_x: int = 0
        self.__real_height: int = 0
        self.__real_width: int = 0
        self.__const_real_height: int = 0
        self.__const_real_width: int = 0
        self.__visibility: bool = True

        self.__place_info_x: Union[int, None] = None
        self.__place_info_y: Union[int, None] = None
        self.__place_info_rely: Union[int, float, None] = None
        self.__place_info_relx: Union[int, float, None] = None
        self.__place_info_anchor: Literal["n", "e", "s", "w", "ne", "nw", "se", "sw", "center", None] = None

        self.__pack_info_pady: Union[int, None] = None
        self.__pack_info_padx: Union[int, None] = None
        self.__pack_info_before: Any = None
        self.__pack_info_after: Any = None
        self.__pack_info_side: Literal["top", "bottom", "left", "right", None] = None
        self.__pack_info_anchor: Literal["n", "e", "s", "w", "ne", "nw", "se", "sw", "center", None] = None

        self.__grid_info_column: Union[int, None] = None
        self.__grid_info_columnspan: Union[int, None] = None
        self.__grid_info_padx: Union[int, None] = None
        self.__grid_info_pady: Union[int, None] = None
        self.__grid_info_row: Union[int, None] = None
        self.__grid_info_rowspan: Union[int, None] = None
        self.__grid_info_sticky: Literal["n", "e", "s", "w", "ne", "nw", "se", "sw", None] = None

        if self.__x_axis_point_spacing == "auto":
            self.__x_axis_point_spacing_handle_by = "auto"
        else:
            self.__x_axis_point_spacing_handle_by = "manual"

        if self.__x_axis_display_values_indices is not None:
            self.__x_axis_display_values_indices = Utils._sort_tuple(self.__x_axis_display_values_indices)
            self.__x_axis_values_handle_by = "label_indices"
        else:
            self.__x_axis_values_handle_by = "label_count"

        self.__create_widgets()
        self.__configure_required_widget_size()
        self.__configure_x_axis_labels_info()
        self.__configure_x_axis_point_spacing()
        self.__create_x_axis_labels()
        self.__set_x_axis_values()
        self.__create_y_axis_labels()
        self.__set_y_axis_values()
        self.__create_y_axis_sections()
        self.__create_x_axis_sections()
        self.__set_x_y_axis_data_texts()
        self.__set_pointer_state()
        self.__set_pointer_size()
        self.__set_widgets_fonts()
        self.__set_widgets_colors()
        self.__place_widgets()
        self.__reset_chart_info()

    def __create_widgets(self) -> None:
        """
        Create widgets for the LineChart.

        This method initializes the main frame along with frames for the y-axis, x-axis,
        y-axis values, x-axis values, y-axis data label, x-axis data label, output frame,
        output canvas, and pointer.
        """
        self.__main_frame = tkinter.Frame(master=self.__master)
        self.__x_axis_values_frame = tkinter.Frame(master=self.__main_frame)
        self.__y_axis_values_frame = tkinter.Frame(master=self.__main_frame)
        self.__y_axis_data_label = tkinter.Label(master=self.__main_frame)
        self.__x_axis_data_label = tkinter.Label(master=self.__main_frame)
        self.__output_frame = tkinter.Frame(master=self.__main_frame)
        self.__output_canvas = tkinter.Canvas(master=self.__output_frame, highlightthickness=0)
        self.__y_axis_frame = tkinter.Frame(master=self.__main_frame)
        self.__x_axis_frame = tkinter.Frame(master=self.__main_frame)
        self.__pointer = tkinter.Frame(master=self.__output_canvas)

    def __set_pointer_state(self) -> None:
        """
        Set the state of the pointer.

        This method configures the behavior of the pointer based on its state (enabled or disabled).
        If the pointer is enabled, it binds events for mouse movement to display pointed values.
        If the pointer is disabled, it unbinds those events.
        """
        if self.__pointer_state == "enabled":
            self.__output_canvas.bind("<Leave>", self.__hide_pointer)
            self.__output_canvas.bind("<Motion>", self.__return_pointed_values)
        elif self.__pointer_state == "disabled":
            self.__output_canvas.unbind("<Leave>")
            self.__output_canvas.unbind("<Motion>")

    def __set_widgets_colors(self) -> None:
        """
        Set the colors for LineChart widgets.

        This method configures the background and foreground colors for various widgets in the LineChart,
        including the frames for y-axis, x-axis, y-axis values, x-axis values, main frame, output frame,
        output canvas, y-axis data label, x-axis data label, and pointer.
        """
        self.__y_axis_frame.configure(bg=self.__axis_color)
        self.__x_axis_frame.configure(bg=self.__axis_color)
        self.__y_axis_values_frame.configure(bg=self.__bg_color)
        self.__x_axis_values_frame.configure(bg=self.__bg_color)

        self.__main_frame.configure(bg=self.__bg_color)
        self.__output_frame.configure(bg=self.__fg_color)
        self.__output_canvas.configure(bg=self.__fg_color)

        self.__y_axis_data_label.configure(bg=self.__bg_color, fg=self.__y_axis_data_font_color)
        for label in self.__x_axis_values_frame.winfo_children():
            if type(label) is tkinter.Label:
                label.configure(bg=self.__bg_color, fg=self.__x_axis_font_color)

        self.__x_axis_data_label.configure(bg=self.__bg_color, fg=self.__x_axis_data_font_color)
        for label in self.__y_axis_values_frame.winfo_children():
            if type(label) is tkinter.Label:
                label.configure(bg=self.__bg_color, fg=self.__y_axis_font_color)

        self.__pointer.configure(bg=self.__pointer_color)

    def __set_widgets_fonts(self) -> None:
        """
        Set the fonts for LineChart widgets.

        This method configures the font styles for various widgets in the LineChart,
        including the y-axis data label, x-axis data label, y-axis values labels,
        and x-axis values labels, using the specified data font style and axis font style.
        """
        self.__y_axis_data_label.configure(font=self.__data_font_style)
        self.__x_axis_data_label.configure(font=self.__data_font_style)

        for label in self.__y_axis_values_frame.winfo_children():
            if type(label) is tkinter.Label:
                label.configure(font=self.__axis_font_style)

        for label in self.__x_axis_values_frame.winfo_children():
            if type(label) is tkinter.Label:
                label.configure(font=self.__axis_font_style)

    def __set_pointer_size(self) -> None:
        """
        Set the size of the pointer.

        This method adjusts the width and height of the pointer widget based on the specified pointer size.
        """
        self.__pointer.configure(width=self.__pointer_size)
        self.__pointer.config(height=self.__const_real_height)

    def __place_widgets(self) -> None:
        """
        Place widgets within the LineChart.

        This method handles the placement of various widgets within the LineChart, including the main frame,
        y-axis frame, x-axis frame, output frame, output canvas, y-axis values frame, and x-axis values frame,
        based on the specified dimensions and positions.
        """
        self.__main_frame.configure(width=self.__width, height=self.__height)

        self.__y_axis_data_label.place_forget()
        self.__x_axis_data_label.place_forget()

        if self.__y_axis_data != "":
            if self.__y_axis_data_position == "top":
                self.__y_axis_data_label.place(x=0, y=0)
            else:
                self.__y_axis_data_label.place(
                    x=0,
                    y=self.__y_space + self.__y_special_height_space + self.__real_height / 2,
                    anchor="w"
                )

        if self.__x_axis_data != "":
            if self.__x_axis_data_position == "top":
                self.__x_axis_data_label.place(
                    relx=1,
                    x=-self.__x_axis_data_req_width,
                    y=self.__height - self.__x_axis_data_req_height
                )
            else:
                self.__x_axis_data_label.place(
                    rely=1,
                    y=-self.__x_axis_data_req_height, relx=0, anchor="n",
                    x=(
                            self.__const_real_width / 2 + self.__y_axis_data_req_width_space_side +
                            self.__y_value_req_width_space + self.__axis_size + self.__x_axis_data_req_width_space_top +
                            self.__x_special_width_space
                    )
                )

        self.__y_axis_frame.configure(width=self.__axis_size)
        self.__x_axis_frame.configure(height=self.__axis_size)

        self.__y_axis_frame.place(
            x=self.__y_value_req_width_space + self.__y_axis_data_req_width_space_side,
            y=float(
                self.__y_axis_data_req_height_space_top +
                (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space
            ),
            height=self.__const_real_height + self.__y_space + self.__axis_size
        )
        self.__x_axis_frame.place(
            x=self.__y_value_req_width_space + self.__y_axis_data_req_width_space_side,
            y=(self.__height - self.__axis_size + -self.__x_value_req_height_space +
               -self.__x_axis_data_req_height_space_side),
            width=self.__const_real_width + self.__axis_size + self.__x_space
        )

        self.__output_frame.place(
            x=self.__y_value_req_width_space + self.__axis_size + self.__y_axis_data_req_width_space_side,
            width=self.__const_real_width,
            height=self.__const_real_height,
            y=float(
                self.__y_axis_data_req_height_space_top + (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space + self.__y_space
            )
        )

        self.__output_canvas.place(y=0, x=0, height=self.__const_real_height, width=self.__const_real_width)

        if self.__y_values_frame_place_req:
            self.__y_axis_values_frame.place(
                x=self.__y_axis_data_req_width_space_side,
                width=self.__y_value_req_width_space,
                height=self.__height
            )
        else:
            self.__y_axis_values_frame.place_forget()

        if self.__x_values_frame_place_req:
            self.__x_axis_values_frame.place(
                x=0,
                y=self.__height - self.__x_value_req_height_space + -self.__x_axis_data_req_height_space_side,
                height=self.__x_value_req_height_space,
                width=self.__width
            )
        else:
            self.__x_axis_values_frame.place_forget()

    def __configure_x_axis_point_spacing(self) -> None:
        """
        Configure the spacing between points on the x-axis.

        This method calculates and sets the spacing between points on the x-axis based on the
        specified handle method. If the spacing is handled automatically, it calculates the spacing
        based on the real width of the LineChart and the number of x-axis values. If handled manually,
        it uses the specified x-axis point spacing value.
        """
        if self.__x_axis_point_spacing_handle_by == "auto":
            self.__x_axis_point_spacing = (self.__const_real_width / len(self.__x_axis_values))
        elif self.__x_axis_point_spacing_handle_by == "manual":
            self.__x_axis_point_spacing = self.__x_axis_point_spacing

    def __configure_required_widget_size(self) -> None:
        """
        Configure the required sizes of the LineChart's widgets.

        This method calculates and sets the required sizes for various widgets in the LineChart,
        such as axis labels, based on the provided data and styling options. It determines the
        necessary space for displaying the data labels, axis values, and adjusts the real width
        and height of the LineChart accordingly.
        """
        self.__x_axis_data_req_width_space_top = 0
        self.__x_axis_data_req_height_space_side = 0
        self.__x_special_width_space = 0
        self.__x_axis_data_req_height = 0
        self.__x_axis_data_req_width = 0
        if self.__x_axis_data != "":
            self.__x_axis_data_req_height = Utils._required_height(text=self.__x_axis_data, font=self.__data_font_style)
            self.__x_axis_data_req_width = Utils._required_width(text=self.__x_axis_data, font=self.__data_font_style)
            if self.__x_axis_data_position == "top":
                self.__x_special_width_space = 15
                self.__x_axis_data_req_width_space_top = Utils._required_width(
                    text=self.__x_axis_data, font=self.__data_font_style
                )
            else:
                self.__x_axis_data_req_height_space_side = Utils._required_height(
                    text=self.__x_axis_data, font=self.__data_font_style
                )

        self.__y_axis_data_req_height_space_top = 0
        self.__y_axis_data_req_width_space_side = 0
        self.__y_special_height_space = 0

        self.__y_values_frame_place_req = True
        self.__x_values_frame_place_req = True
        # self.__y_axis_data_req_height = Utils._required_height(text=self.__y_axis_data, font=self.__data_font_style)
        # self.__y_axis_data_req_width = Utils._required_width(text=self.__y_axis_data, font=self.__data_font_style)
        if self.__y_axis_data != "":
            if self.__y_axis_data_position == "top":
                self.__y_special_height_space = 15
                self.__y_axis_data_req_height_space_top = Utils._required_height(
                    text=self.__y_axis_data, font=self.__data_font_style
                )
            else:
                self.__y_axis_data_req_width_space_side = Utils._required_width(
                    text=self.__y_axis_data[0], font=self.__data_font_style
                )

        if self.__y_axis_label_count == 0:
            self.__y_value_req_height_space = 0
            self.__y_value_req_width_space = 0
            self.__y_values_frame_place_req = False
        else:
            if (len(Utils._format_float_with_precision(self.__y_axis_max_value, self.__y_axis_precision)) >
                    len(Utils._format_float_with_precision(self.__y_axis_min_value, self.__y_axis_precision))):
                y_value_temp = self.__y_axis_max_value
            else:
                y_value_temp = self.__y_axis_min_value
            self.__y_value_req_height_space = Utils._required_height(
                text=Utils._format_float_with_precision(y_value_temp, self.__y_axis_precision),
                font=self.__axis_font_style
            )
            self.__y_value_req_width_space = Utils._required_width(
                text=Utils._format_float_with_precision(y_value_temp, self.__y_axis_precision),
                font=self.__axis_font_style
            )

        self.__x_value_req_width_space = 0
        self.__x_value_req_height_space = 0
        if self.__x_axis_label_count == 0 and self.__x_axis_values_handle_by == "label_count":
            self.__x_values_frame_place_req = False
        elif self.__x_axis_values_handle_by == "label_indices" and (len(self.__x_axis_display_values_indices) == 0):
            self.__x_values_frame_place_req = False
        else:
            self.__x_value_req_height_space = Utils._required_height(
                text=self.__x_axis_values[0], font=self.__axis_font_style
            )
            # self.__x_value_req_width_space = RequiredWidth(text=format_float_with_precision(self.__x_axis_data_max,
            # self.__x_values_decimals), font=self.__axis_font_style)
            self.__x_value_req_width_space = Utils._get_max_required_label_width(
                data=self.__x_axis_values, font=self.__axis_font_style
            )

        if self.__y_value_req_height_space / 2 > self.__x_value_req_height_space:
            self.__x_value_req_height_space = self.__y_value_req_height_space / 2

        self.__real_width = self.__width - (
                self.__y_value_req_width_space + self.__axis_size + self.__x_axis_data_req_width_space_top +
                self.__y_axis_data_req_width_space_side + (self.__x_value_req_width_space / 2) +
                self.__x_special_width_space + self.__x_space
        )

        self.__const_real_width = self.__real_width
        self.__real_height = self.__height - (
                self.__y_axis_data_req_height_space_top + self.__axis_size + self.__x_value_req_height_space +
                self.__x_axis_data_req_height_space_side + (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space + self.__y_space
        )
        self.__real_height = self.__real_height

        self.__const_real_height = int(self.__real_height)

        self.__y_axis_values_gap = abs(self.__y_axis_max_value - self.__y_axis_min_value)

    def __set_x_y_axis_data_texts(self) -> None:
        """
        Set the text for the x and y axis data labels.

        This method sets the text for the y-axis data label based on its position. If the position
        is 'top', the label text is set to the provided y-axis data. Otherwise, if the position is
        'side', the label text is set as a newline-separated string of the y-axis data elements.

        The text for the x-axis data label is set directly to the provided x-axis data.
        """
        if self.__y_axis_data_position == "top":
            self.__y_axis_data_label.configure(text=self.__y_axis_data)
        else:
            self.__y_axis_data_label.configure(text="\n".join(self.__y_axis_data))
        self.__x_axis_data_label.configure(text=self.__x_axis_data)

    def __set_y_axis_values(self) -> None:
        """
        Set the values for the y-axis labels.

        This method sets the values for the y-axis labels based on the specified label count and the
        range of values between the maximum and minimum y-axis values. If the y-axis label count is greater
        than 0, it iterates over the y-axis labels and calculates the value for each label using the
        formula: maximum y-axis value - ((y-axis value range) / y-axis label count) * index. If the minimum
        y-axis value is 0 and the index is equal to the y-axis label count, the value is set to 0. The values
        are formatted with the specified precision before being assigned to the labels.
        """
        if self.__y_axis_label_count > 0:
            for i, label in enumerate(self.__y_axis_values_frame.winfo_children()):
                value = (self.__y_axis_max_value - (self.__y_axis_values_gap / self.__y_axis_label_count) * i)
                if self.__y_axis_min_value == 0 and i == self.__y_axis_label_count:
                    value = 0
                value = Utils._format_float_with_precision(value, self.__y_axis_precision)
                label.configure(text=value)

    def __create_y_axis_labels(self) -> None:
        """
        Create the y-axis labels.

        This method creates the y-axis labels based on the specified label count. If the y-axis label count is
        greater than 0, it iterates over the range of label count and creates a tkinter Label for each label.
        The labels are placed vertically with equal spacing between them. The y-coordinate for each label is
        calculated based on the initial y-position, the height of each label, additional spacing, and the total
        height of the plot area divided by the number of labels.
        """
        if self.__y_axis_label_count > 0:
            y = self.__y_axis_data_req_height_space_top + (
                    self.__y_value_req_height_space / 2) + self.__y_special_height_space + self.__y_space
            for i in range(self.__y_axis_label_count + 1):
                tkinter.Label(
                    master=self.__y_axis_values_frame,
                    justify="right"
                ).place(
                    y=y,
                    x=0,
                    anchor="w",
                    width=self.__y_value_req_width_space
                )
                y += self.__real_height / self.__y_axis_label_count

    def __destroy_y_axis_labels(self) -> None:
        """
        Destroy the y-axis labels.

        This method removes and destroys all existing y-axis labels. It iterates over the children of the
        y-axis values frame, which contain the y-axis labels, and calls the place_forget() and destroy() methods
        for each label to remove them from the GUI and release system resources.
        """
        for y_value in self.__y_axis_values_frame.winfo_children():
            y_value.place_forget()
            y_value.destroy()

    def __set_x_axis_values_using_label_count(self) -> None:
        """
        Set the x-axis values using the label count.

        This method sets the x-axis values using the label count. It iterates over the children of the
        x-axis values frame, which contain the x-axis labels, and assigns values to each label from the
        provided x-axis values list in reverse order. The index is decremented by the value of
        x_labels_values_index_change for each iteration.
        """
        index = -1
        for label in (self.__x_axis_values_frame.winfo_children()):
            value = self.__x_axis_values[index]
            index -= self.__x_labels_values_index_change
            label.configure(text=value)

    def __set_x_axis_values_using_indices(self) -> None:
        """
        Set the x-axis values using the specified display indices.

        This method sets the x-axis values using the specified display indices. It iterates over the children of the
        x-axis values frame, which contain the x-axis labels, and assigns values to each label from the
        provided x-axis values list based on the display indices provided.
        """
        index = -1
        for label in (self.__x_axis_values_frame.winfo_children()):
            value = self.__x_axis_values[self.__x_axis_display_values_indices[index]]
            index -= 1
            label.configure(text=value)

    def __create_x_axis_labels_using_label_count(self) -> None:
        """
        Create x-axis labels using the specified label count.

        This method creates x-axis labels using the specified label count. It iterates over the range of the label count
        and places labels inside the x-axis values frame. The labels are evenly spaced across the x-axis based on the
        provided label count.
        """
        x = self.__width - self.__x_axis_data_req_width_space_top - (
                self.__x_value_req_width_space / 2) - self.__x_special_width_space - self.__x_space
        for i in range(self.__x_axis_label_count):
            tkinter.Label(master=self.__x_axis_values_frame).place(
                rely=1,
                y=-self.__x_value_req_height_space,
                x=x,
                anchor="n"
            )
            x -= self.__const_real_width / self.__x_axis_label_count

    def __create_x_axis_labels_using_indices(self) -> None:
        """
        Create x-axis labels using the specified display indices.

        This method creates x-axis labels using the specified display indices. It iterates over the range of
        the label count and places labels inside the x-axis values frame. The labels are placed at positions
        corresponding to the indices specified for display.
        """
        x = self.__width - self.__x_axis_data_req_width_space_top - (
                self.__x_value_req_width_space / 2) - self.__x_special_width_space - self.__x_space
        for i in range(self.__x_axis_label_count):
            if (self.__x_axis_label_count - (i + 1)) in self.__x_axis_display_values_indices:
                tkinter.Label(master=self.__x_axis_values_frame).place(
                    rely=1,
                    y=-self.__x_value_req_height_space,
                    x=x,
                    anchor="n"
                )
            x -= self.__const_real_width / self.__x_axis_label_count

    def __create_x_axis_labels(self) -> None:
        """
        Create x-axis labels based on the method specified for handling x-axis values.

        This method creates x-axis labels based on the method specified for handling x-axis values. If the values are
        to be displayed using label indices, it calls the __create_x_axis_labels_using_indices method.
        Otherwise, it calls the __create_x_axis_labels_using_label_count method.
        """
        if self.__x_axis_values_handle_by == "label_indices":
            self.__create_x_axis_labels_using_indices()
        else:
            self.__create_x_axis_labels_using_label_count()

    def __set_x_axis_values(self) -> None:
        """
        Set x-axis values based on the method specified for handling x-axis values.

        This method sets x-axis values based on the method specified for handling x-axis values. If the values are to be
        set using label indices, it calls the __set_x_axis_values_using_indices method. Otherwise, it calls the
        __set_x_axis_values_using_label_count method.
        """
        if self.__x_axis_values_handle_by == "label_indices":
            self.__set_x_axis_values_using_indices()
        else:
            self.__set_x_axis_values_using_label_count()

    def __destroy_x_axis_labels(self) -> None:
        """
        Destroy x-axis labels.

        This method destroys all the x-axis labels by iterating through the children of the x-axis values frame,
        forgetting their placement, and then destroying them.
        """
        for x_value in self.__x_axis_values_frame.winfo_children():
            x_value.place_forget()
            x_value.destroy()

    def __configure_x_axis_labels_info(self) -> None:
        """
        Configure information for x-axis labels.

        This method determines the count and index change for x-axis labels based on the method used to provide
        x-axis values. If x-axis values are provided using label indices, it sets the label count to the length
        of the x-axis values. If x-axis values are handled automatically or by label count, it adjusts the label
        count and index change accordingly to ensure proper spacing and distribution of labels.
        """
        if self.__x_axis_values_handle_by == "label_indices":
            self.__x_axis_label_count = len(self.__x_axis_values)

        elif self.__x_axis_values_handle_by == "label_count":
            if self.__x_axis_label_count == 0:
                return
            if self.__x_axis_label_count is None:
                self.__x_axis_label_count = len(self.__x_axis_values)
            x_axis_real_label_count = len(self.__x_axis_values)
            if self.__x_axis_label_count > x_axis_real_label_count:
                self.__x_axis_label_count = x_axis_real_label_count
            else:
                while x_axis_real_label_count % self.__x_axis_label_count != 0:
                    self.__x_axis_label_count += 1
            self.__x_labels_values_index_change = int(x_axis_real_label_count / self.__x_axis_label_count)

    def __create_y_axis_sections(self) -> None:
        """
        Create sections on the y-axis.

        This method creates sections on the y-axis based on the specified section style.
        If the section style is 'normal', it creates evenly spaced sections. If the section style is 'dashed',
        it creates sections with custom width and spacing as specified in the style type tuple.
        """
        y = 0
        if self.__y_axis_section_style == "normal":
            for i in range(self.__y_axis_section_count):
                tkinter.Frame(
                    master=self.__output_frame,
                    height=1,
                    width=self.__const_real_width,
                    bg=self.__y_axis_section_color
                ).place(y=y, anchor="w")
                y += self.__real_height / self.__y_axis_section_count
        else:
            width_ = self.__y_axis_section_style_type[0]
            space_ = self.__y_axis_section_style_type[1]
            for i in range(self.__y_axis_section_count):
                x_ = self.__const_real_width - width_
                while x_ > -(width_ + space_):
                    tkinter.Frame(
                        master=self.__output_frame,
                        height=1,
                        width=width_,
                        bg=self.__y_axis_section_color
                    ).place(y=y, anchor="w", x=x_)
                    x_ -= width_ + space_
                y += self.__real_height / self.__y_axis_section_count

    def __create_x_axis_sections(self) -> None:
        """
        Create sections on the x-axis.

        This method creates sections on the x-axis based on the specified section style.
        If the section style is 'normal',it creates evenly spaced sections. If the section style is 'dashed',
        it creates sections with custom height and spacing is specified in the style type tuple.
        """
        x = self.__const_real_width - 1
        if self.__x_axis_section_style == "normal":
            for i in range(self.__x_axis_section_count):
                tkinter.Frame(
                    master=self.__output_frame,
                    height=self.__const_real_height,
                    width=1,
                    bg=self.__x_axis_section_color
                ).place(x=x, anchor="n")
                x -= (self.__const_real_width / self.__x_axis_section_count)
        else:
            height_ = self.__x_axis_section_style_type[0]
            space_ = self.__x_axis_section_style_type[1]
            for i in range(self.__x_axis_section_count):
                y_ = 0
                while y_ < self.__const_real_height:
                    tkinter.Frame(
                        master=self.__output_frame,
                        height=height_,
                        width=1,
                        bg=self.__x_axis_section_color
                    ).place(x=x, anchor="n", y=y_)
                    y_ += height_ + space_
                x -= (self.__const_real_width / self.__x_axis_section_count)

    def __destroy_x_y_sections(self) -> None:
        """
        Destroy all x-axis and y-axis sections.

        This method destroys all sections created on both the x-axis and y-axis by removing them from the output frame.
        """
        for widget in self.__output_frame.winfo_children():
            if type(widget) is tkinter.Frame:
                widget.place_forget()
                widget.destroy()

    def configure(
            self,
            width: int = None,
            height: int = None,
            axis_size: int = None,
            x_axis_point_spacing: Union[int, Literal["auto"]] = None,

            bg_color: str = None,
            axis_color: str = None,
            fg_color: str = None,
            data_font_style: Tuple[str, int, str] = None,
            axis_font_style: Tuple[str, int, str] = None,

            y_axis_values: Union[int, float] = None,
            y_axis_precision: int = None,
            y_axis_font_color: str = None,
            y_axis_data_font_color: str = None,
            y_axis_section_count: int = None,
            y_axis_section_color: str = None,
            y_axis_section_style: Literal["normal", "dashed"] = None,
            y_axis_section_style_type: Tuple[int, int] = None,
            y_axis_label_count: int = None,
            y_axis_data: Any = None,
            y_axis_data_position: Literal["top", "side"] = None,
            y_space: int = None,

            x_axis_values: Tuple[Any, ...] = None,
            x_axis_data: Any = None,
            x_axis_font_color: str = None,
            x_axis_data_font_color: str = None,
            x_axis_label_count: int = None,
            x_axis_section_count: int = None,
            x_axis_section_style: Literal["normal", "dashed"] = None,
            x_axis_section_style_type: Tuple[int, int] = None,
            x_axis_section_color: str = None,
            x_axis_display_values_indices: Tuple[int, ...] = None,
            x_axis_data_position: Literal["top", "side"] = None,
            x_space: int = None,

            pointer_state: Literal["enabled", "disabled"] = None,
            pointing_values_precision: int = None,
            pointer_color: str = None,
            pointer_lock: Literal["enabled", "disabled"] = None,
            pointing_callback_function: callable = None,
            pointer_size: int = None) -> None:
        """
        Configures the properties of the chart widget based on the provided arguments.

        Args:
            width (int): The width of the chart widget.
            height (int): The height of the chart widget.
            axis_size (int): The size of the axis lines.
            x_axis_point_spacing (Union[int, str]): The spacing between x-axis points.

            bg_color (str): The background color of the chart.
            axis_color (str): The color of the axis lines.
            fg_color (str): The foreground color of the chart.
            data_font_style (Tuple[str, int, str]): The font style for data labels.
            axis_font_style (Tuple[str, int, str]): The font style for axis labels.

            y_axis_values (Union[int, float]): The range of values for the y-axis.
            y_axis_precision (int): The precision of values on the y-axis.
            y_axis_font_color (str): The font color of y-axis labels.
            y_axis_data_font_color (str): The font color of y-axis data labels.
            y_axis_section_count (int): The number of sections on the y-axis.
            y_axis_section_color (str): The color of sections on the y-axis.
            y_axis_section_style (str): The style of sections on the y-axis.
            y_axis_section_style_type (Tuple[int, int]): The type of style for sections on the y-axis.
            y_axis_label_count (int): The count of labels on the y-axis.
            y_axis_data (Any): The data for y-axis labels.
            y_axis_data_position (str): The position of y-axis data labels.
            y_space (int): The space between y-axis and the chart.

            x_axis_values (Tuple[Any, ...]): The values for the x-axis.
            x_axis_data (Any): The data for x-axis labels.
            x_axis_font_color (str): The font color of x-axis labels.
            x_axis_data_font_color (str): The font color of x-axis data labels.
            x_axis_label_count (int): The count of labels on the x-axis.
            x_axis_section_count (int): The number of sections on the x-axis.
            x_axis_section_style (str): The style of sections on the x-axis.
            x_axis_section_style_type (Tuple[int, int]): The type of style for sections on the x-axis.
            x_axis_section_color (str): The color of sections on the x-axis.
            x_axis_display_values_indices (Tuple[int, ...]): The indices of displayed x-axis values.
            x_axis_data_position (str): The position of x-axis data labels.
            x_space (int): The space between the x-axis and the chart.

            pointer_state (str): The state of the pointer. Possible values are "enabled" or "disabled".
            pointing_values_precision (int): The precision of values displayed by the pointer.
            pointer_color (str): The color of the pointer.
            pointer_lock (str): The state of the pointer lock. Possible values are "enable" or "disable".
            pointing_callback_function (callable): A callback function triggered when the pointer is clicked or moved.
            pointer_size (int): The size of the pointer.
            
        Raises:
            ValueError: If any of the provided values are invalid or do not meet the expected criteria.
            TypeError: If the provided values are of incorrect types.
        """
        chart_reset_req: bool = False
        widget_color_change_req: bool = False
        widget_size_change_req: bool = False
        widget_font_change_req: bool = False
        chart_x_values_change_req: bool = False
        chart_sections_change_req: bool = False
        chart_sections_color_change_req: bool = False
        chart_x_labels_change_req: bool = False
        chart_y_labels_change_req: bool = False
        pointer_state_change_req: bool = False
        pointer_size_change_req: bool = False
        reshow_data_req: bool = False

        if width is not None:
            Validate._is_int(width, "width")
            if width != self.__width:
                self.__width = width
                chart_reset_req = True

        if height is not None:
            Validate._is_int(height, "height")
            if height != self.__height:
                self.__height = height
                chart_reset_req = True

        if y_space is not None:
            Validate._is_int(y_space, "y_space")
            if y_space != self.__y_space:
                self.__y_space = y_space
                chart_reset_req = True

        if x_space is not None:
            Validate._is_int(x_space, "x_space")
            if x_space != self.__x_space:
                self.__x_space = x_space
                chart_reset_req = True

        if y_axis_values is not None:
            Validate._is_valid_y_axis_values(y_axis_values, "y_axis_values")
            if y_axis_values != self.__y_axis_values:
                self.__y_axis_values = y_axis_values
                self.__y_axis_min_value = y_axis_values[0]
                self.__y_axis_max_value = y_axis_values[1]
                chart_reset_req = True

        if axis_size is not None:
            Validate._is_int(axis_size, "axis_size")
            if axis_size != self.__axis_size:
                self.__axis_size = axis_size
                chart_reset_req = True

        if y_axis_precision is not None:
            Validate._is_int(y_axis_precision, "y_axis_precision")
            if y_axis_precision != self.__y_axis_precision:
                self.__y_axis_precision = y_axis_precision
                chart_reset_req = True

        if x_axis_data is not None:
            if x_axis_data != self.__x_axis_data:
                self.__x_axis_data = x_axis_data
                chart_reset_req = True

        if data_font_style is not None:
            Validate._is_valid_font(data_font_style, "data_font_style")
            if data_font_style != self.__data_font_style:
                self.__data_font_style = data_font_style
                chart_reset_req = True

        if axis_font_style is not None:
            Validate._is_valid_font(axis_font_style, "axis_font_style")
            if axis_font_style != self.__axis_font_style:
                self.__axis_font_style = axis_font_style
                chart_reset_req = True

        if bg_color is not None:
            Validate._is_valid_color(bg_color, "bg_color")
            if bg_color != self.__bg_color:
                self.__bg_color = bg_color
                widget_color_change_req = True

        if axis_color is not None:
            Validate._is_valid_color(axis_color, "axis_color")
            if axis_color != self.__axis_color:
                self.__axis_color = axis_color
                widget_color_change_req = True

        if fg_color is not None:
            Validate._is_valid_color(fg_color, "fg_color")
            if fg_color != self.__fg_color:
                self.__fg_color = fg_color
                widget_color_change_req = True

        if y_axis_font_color is not None:
            Validate._is_valid_color(y_axis_font_color, "y_axis_font_color")
            if y_axis_font_color != self.__y_axis_font_color:
                self.__y_axis_font_color = y_axis_font_color
                widget_color_change_req = True

        if x_axis_font_color is not None:
            Validate._is_valid_color(x_axis_font_color, "x_axis_font_color")
            if x_axis_font_color != self.__x_axis_font_color:
                self.__x_axis_font_color = x_axis_font_color
                widget_color_change_req = True

        if y_axis_data_font_color is not None:
            Validate._is_valid_color(y_axis_data_font_color, "y_axis_data_font_color")
            if y_axis_data_font_color != self.__y_axis_data_font_color:
                self.__y_axis_data_font_color = y_axis_data_font_color
                widget_color_change_req = True

        if x_axis_data_font_color is not None:
            Validate._is_valid_color(x_axis_data_font_color, "x_axis_data_font_color")
            if x_axis_data_font_color != self.__x_axis_data_font_color:
                self.__x_axis_data_font_color = x_axis_data_font_color
                widget_color_change_req = True

        if x_axis_section_color is not None:
            Validate._is_valid_color(x_axis_section_color, "x_axis_section_color")
            if x_axis_section_color != self.__x_axis_section_color:
                self.__x_axis_section_color = x_axis_section_color
                chart_sections_color_change_req = True

        if y_axis_section_color is not None:
            Validate._is_valid_color(y_axis_section_color, "y_axis_section_color")
            if y_axis_section_color != self.__y_axis_section_color:
                self.__y_axis_section_color = y_axis_section_color
                chart_sections_color_change_req = True

        if y_axis_section_style is not None:
            Validate._is_valid_section_style(y_axis_section_style, "y_axis_section_style")
            if y_axis_section_style != self.__y_axis_section_style:
                self.__y_axis_section_style = y_axis_section_style
                chart_sections_change_req = True

        if x_axis_section_style is not None:
            Validate._is_valid_section_style(x_axis_section_style, "x_axis_section_style")
            if x_axis_section_style != self.__x_axis_section_style:
                self.__x_axis_section_style = x_axis_section_style
                chart_sections_change_req = True

        if y_axis_section_style_type is not None:
            Validate._is_valid_style_type(y_axis_section_style_type, "y_axis_section_style_type")
            if y_axis_section_style_type != self.__y_axis_section_style_type:
                self.__y_axis_section_style_type = y_axis_section_style_type
                chart_sections_change_req = True

        if x_axis_section_style_type is not None:
            Validate._is_valid_style_type(x_axis_section_style_type, "x_axis_section_style_type")
            if x_axis_section_style_type != self.__x_axis_section_style_type:
                self.__x_axis_section_style_type = x_axis_section_style_type
                chart_sections_change_req = True

        if y_axis_label_count is not None:
            Validate._is_int(y_axis_label_count, "y_axis_label_count")
            if y_axis_label_count != self.__y_axis_label_count:
                if y_axis_label_count == 0 or self.__y_axis_label_count == 0:
                    chart_reset_req = True
                self.__y_axis_label_count = y_axis_label_count
                chart_y_labels_change_req = True
                widget_color_change_req = True

        if x_axis_section_count is not None:
            Validate._is_int(x_axis_section_count, "x_axis_section_count")
            if x_axis_section_count != self.__x_axis_section_count:
                self.__x_axis_section_count = x_axis_section_count
                chart_sections_change_req = True

        if y_axis_section_count is not None:
            Validate._is_int(y_axis_section_count, "y_axis_section_count")
            if y_axis_section_count != self.__y_axis_section_count:
                self.__y_axis_section_count = y_axis_section_count
                chart_sections_change_req = True

        if x_axis_data_position is not None:
            Validate._is_valid_data_position(x_axis_data_position, "x_axis_data_position")
            if x_axis_data_position != self.__x_axis_data_position:
                self.__x_axis_data_position = x_axis_data_position
                chart_reset_req = True

        if y_axis_data_position is not None:
            Validate._is_valid_data_position(y_axis_data_position, "y_axis_data_position")
            if y_axis_data_position != self.__y_axis_data_position:
                self.__y_axis_data_position = y_axis_data_position
                chart_reset_req = True

        if y_axis_data is not None:
            if y_axis_data != self.__y_axis_data:
                self.__y_axis_data = y_axis_data
                chart_reset_req = True

        if x_axis_values is not None:
            if x_axis_values != self.__x_axis_values:
                Validate._is_valid_x_axis_values(x_axis_values, "x_axis_values")
                if self.__x_axis_values_handle_by == "label_indices":
                    if x_axis_display_values_indices is not None:
                        Validate._is_valid_x_axis_indices(
                            x_axis_values,
                            x_axis_display_values_indices,
                            "x_axis_display_values_indices"
                        )
                    else:
                        Validate._is_valid_x_axis_indices(
                            x_axis_values,
                            self.__x_axis_display_values_indices,
                            "x_axis_display_values_indices"
                        )
                if len(x_axis_values) != len(self.__x_axis_values):
                    chart_reset_req = True
                elif Utils._get_max_required_label_width(
                        x_axis_values, self.__axis_font_style
                ) != self.__x_value_req_width_space:
                    chart_reset_req = True
                else:
                    chart_x_values_change_req = True
                self.__x_axis_values = x_axis_values

        if x_axis_display_values_indices is not None:
            if x_axis_values is None:
                Validate._is_valid_x_axis_indices(
                    self.__x_axis_values,
                    x_axis_display_values_indices,
                    "x_axis_display_values_indices"
                )
            self.__x_axis_values_handle_by = "label_indices"
            x_axis_display_values_indices = Utils._sort_tuple(x_axis_display_values_indices)
            if x_axis_display_values_indices != self.__x_axis_display_values_indices:
                self.__x_axis_display_values_indices = x_axis_display_values_indices
                chart_x_labels_change_req = True
                widget_color_change_req = True
                widget_font_change_req = True

        elif x_axis_label_count is not None:
            Validate._is_valid_x_axis_label_count(x_axis_label_count, "x_axis_label_count")
            self.__x_axis_values_handle_by = "label_count"
            if x_axis_label_count != self.__x_axis_label_count:
                if x_axis_label_count == 0 or self.__x_axis_label_count == 0:
                    chart_reset_req = True
                self.__x_axis_label_count = x_axis_label_count
                chart_x_labels_change_req = True
                widget_color_change_req = True
                widget_font_change_req = True

        if pointer_color is not None:
            Validate._is_valid_color(pointer_color, "pointer_color")
            self.__pointer_color = pointer_color
            widget_color_change_req = True

        if pointing_callback_function is not None:
            Validate._is_valid_function(pointing_callback_function, "pointing_callback_function")
            self.__pointing_callback_function = pointing_callback_function

        if pointing_values_precision is not None:
            Validate._is_int(pointing_values_precision, "pointing_values_precision")
            self.__pointing_values_precision = pointing_values_precision

        if pointer_lock is not None:
            Validate._is_valid_pointer_state_lock(pointer_lock, "pointer_lock")
            self.__pointer_lock = pointer_lock

        if pointer_state is not None:
            Validate._is_valid_pointer_state_lock(pointer_state, "pointer_state")
            self.__pointer_state = pointer_state
            pointer_state_change_req = True

        if pointer_size is not None:
            Validate._is_int(pointer_size, "pointer_size")
            self.__pointer_size = pointer_size
            pointer_size_change_req = True

        if x_axis_point_spacing is not None:
            Validate._is_valid_x_axis_point_spacing(x_axis_point_spacing, "x_axis_point_spacing")
            if x_axis_point_spacing == "auto":
                if self.__x_axis_point_spacing_handle_by != "auto":
                    self.__x_axis_point_spacing_handle_by = "auto"
                    reshow_data_req = True
            elif self.__x_axis_point_spacing != x_axis_point_spacing:
                self.__x_axis_point_spacing_handle_by = "manual"
                self.__x_axis_point_spacing = x_axis_point_spacing
                reshow_data_req = True

        if chart_reset_req:
            self.__destroy_x_axis_labels()
            self.__destroy_y_axis_labels()
            self.__destroy_x_y_sections()
            self.__configure_required_widget_size()
            self.__configure_x_axis_point_spacing()
            self.__configure_x_axis_labels_info()
            self.__create_x_axis_labels()
            self.__set_x_axis_values()
            self.__create_y_axis_labels()
            self.__set_y_axis_values()
            self.__create_y_axis_sections()
            self.__create_x_axis_sections()
            self.__set_x_y_axis_data_texts()
            self.__set_pointer_state()
            self.__set_pointer_size()
            self.__set_widgets_fonts()
            self.__set_widgets_colors()
            self.__place_widgets()
            self.__reset_chart_info()
            self.__reshow_data()

        if chart_x_labels_change_req:
            self.__configure_x_axis_labels_info()
            self.__destroy_x_axis_labels()
            self.__create_x_axis_labels()
            self.__set_x_axis_values()

        elif chart_y_labels_change_req:
            self.__destroy_y_axis_labels()
            self.__create_y_axis_labels()
            self.__set_y_axis_values()

        if chart_x_values_change_req:
            self.__set_x_axis_values()

        if chart_sections_change_req or chart_sections_color_change_req:
            self.__destroy_x_y_sections()
            self.__create_y_axis_sections()
            self.__create_x_axis_sections()

        if widget_color_change_req:
            self.__set_widgets_colors()

        if widget_size_change_req:
            self.__set_pointer_size()

        if reshow_data_req:
            self.__configure_x_axis_point_spacing()
            self.__reshow_data()

        if pointer_size_change_req:
            self.__set_pointer_size()

        if pointer_state_change_req:
            self.__set_pointer_state()

        if widget_font_change_req:
            self.__set_widgets_fonts()

    def __reset_chart_info(self) -> None:
        """
        Reset the chart information and clear the canvas.

        This method deletes all items on the canvas and recalculates the real width and real height of the chart.
        """
        self.__output_canvas.delete("all")
        self.__real_width = self.__width - (
                self.__y_value_req_width_space + self.__axis_size + self.__x_axis_data_req_width_space_top +
                self.__y_axis_data_req_width_space_side + (self.__x_value_req_width_space / 2) +
                self.__x_special_width_space + self.__x_space
        )

        self.__const_real_width = self.__real_width
        self.__real_height = self.__height - (
                self.__y_axis_data_req_height_space_top + self.__axis_size + self.__x_value_req_height_space +
                self.__x_axis_data_req_height_space_side + (self.__y_value_req_height_space / 2) +
                self.__y_special_height_space + self.__y_space
        )
        self.__real_height = self.__real_height

        self.__const_real_height = self.__real_height

        self.__output_canvas.place(y=0, x=0, height=self.__const_real_height, width=self.__const_real_width)
        self.__place_x = 0

    def __reset_lines_info(self) -> None:
        """
        Reset the information for all lines in the chart.

        This method calls the __reset() method for each line object stored in the __lines list.
        """
        for line in self.__lines:
            line._Line__reset()
            
    def __get_max_visible_data_points(self) -> int:
        """
        Calculate the maximum number of data points that can be displayed 
        on the chart at the current resolution and axis spacing.

        Returns:
            int: The maximum number of data points visible on the x-axis.
        """
        # Determine the maximum number of data points based on the available width
        # and spacing between points on the x-axis.
        max_visible_points = int(self.__const_real_width / self.__x_axis_point_spacing) + 1
        return max_visible_points

    def __get_max_data_length_across_lines(self) -> int:
        """
        Determine the maximum number of data points in any line within the chart.
        
        This is useful for determining how much data is present in the most 
        populated data series.

        Returns:
            int: The maximum length of data in any line.
        """
        if len(self.__lines) > 0:
            # Retrieve the number of data points in each line
            lines_values = [len(line._Line__data) for line in self.__lines]
            
            # Find and return the maximum length among all lines
            max_data_length = max(lines_values)
            return max_data_length
        return 0

    def __reshow_data(self) -> None:
        """
        Re-shows data on the chart.

        This method recalculates the chart info, ensures that the chart can support the maximum amount of data to be
        shown, resets each line with the latest data, and then displays the data for each line.
        """
        self.__reset_chart_info()

        maximum_data = self.__get_max_data_length_across_lines()
        max_visible_points = self.__get_max_visible_data_points()

        for line in self.__lines:
            if maximum_data > max_visible_points:
                line._Line__temp_data = line._Line__data[maximum_data - max_visible_points::]
                line._Line__data = line._Line__data[:maximum_data - max_visible_points:]
            else:
                line._Line__temp_data = line._Line__data
                line._Line__data = []
            line._Line__reset_positions()

        for line in self.__lines:
            self.show_data(line=line, data=line._Line__temp_data)

    def show_data(self, line: Line, data: List[Union[int, float]]) -> None:
        """
        Show data on the chart for the given line.

        Args:
            line (Line): The line object to which the data belongs.
            data (List[Union[int, float]]): The list of data points to be displayed.

        Raises:
            ValueError: If the provided line object is not valid or not found in the chart.
            TypeError: If the provided data is not a list or contains invalid types.
            TypeError: If the line object is not an instance of the Line class.

        This method adds the provided data to the line's existing data, adjusts the display of the chart accordingly,
        and shows the data points on the chart. It also handles various styles for displaying the data points,
        such as dashed or dotted lines, and highlights for individual data points.
        """
        Validate._is_valid_line(line, "line")
        Validate._is_valid_data(data, "data")

        re_show_data = False
        if line not in self.__lines:
            Validate._invalid_line(line)

        line._Line__data += data

        if line._Line__visibility:

            for d in data:

                x_start = line._Line__x_end
                y_start = line._Line__y_end

                line._Line__x_end += self.__x_axis_point_spacing

                if d >= 0:
                    d = d - self.__y_axis_min_value
                    line._Line__y_end = self.__const_real_height - (
                            d / self.__y_axis_values_gap * self.__const_real_height)
                else:
                    d = abs(d) + self.__y_axis_max_value
                    line._Line__y_end = (d / self.__y_axis_values_gap * self.__const_real_height)
                line._Line__y_end += (line._Line__size / 2)

                if round(line._Line__x_end) >= round(self.__real_width) and self.__real_width <= self.__width * 5:
                    self.__place_x -= self.__x_axis_point_spacing

                    self.__output_canvas.place(
                        x=self.__place_x,
                        width=self.__real_width + self.__x_axis_point_spacing
                    )

                    self.__real_width += self.__x_axis_point_spacing

                elif self.__real_width > self.__width * 5:
                    re_show_data = True
                    break

                if line._Line__fill == "enabled":
                    points_of_polygon = [
                        x_start, y_start,
                        line._Line__x_end, line._Line__y_end,
                        line._Line__x_end, self.__const_real_height,
                        x_start, self.__const_real_height
                    ]
                    self.__output_canvas.create_polygon(
                        points_of_polygon, fill=line._Line__fill_color
                    )

                if line._Line__style == "dashed":
                    dash_width = line._Line__style_type[0]
                    space_width = line._Line__style_type[1]
                    total_width = dash_width + space_width
                    real_x_axis_point_spacing = ((abs(y_start - line._Line__y_end) ** 2) + (
                            self.__x_axis_point_spacing ** 2)) ** (1 / 2)
                    dash_count = real_x_axis_point_spacing / (dash_width + space_width)
                    total_change_x = (line._Line__x_end - x_start)
                    total_change_y = (line._Line__y_end - y_start)
                    dash_change_percentage = dash_width / total_width
                    space_change_percentage = space_width / total_width
                    change_x = (total_change_x / dash_count)
                    change_y = (total_change_y / dash_count)
                    dash_change_x = change_x * dash_change_percentage
                    dash_change_y = change_y * dash_change_percentage
                    space_change_x = change_x * space_change_percentage
                    space_change_y = change_y * space_change_percentage
                    dashed_x_start = x_start
                    dashed_y_start = y_start
                    if y_start > line._Line__y_end:
                        line_going = "to_up"
                    else:
                        line_going = "to_down"
                    while line._Line__x_end > dashed_x_start:
                        dashed_x_end = dashed_x_start + dash_change_x
                        dashed_y_end = dashed_y_start + dash_change_y
                        if dashed_x_end > line._Line__x_end:
                            dashed_x_end = dashed_x_end - (dashed_x_end - line._Line__x_end)
                        if dashed_y_end <= line._Line__y_end and line_going == "to_up":
                            dashed_y_end = dashed_y_end - (dashed_y_end - line._Line__y_end)
                        if dashed_y_end > line._Line__y_end and line_going == "to_down":
                            dashed_y_end = dashed_y_end - (dashed_y_end - line._Line__y_end)
                        self.__output_canvas.create_line(
                            dashed_x_start, dashed_y_start,
                            dashed_x_end, dashed_y_end,
                            fill=line._Line__color, width=line._Line__size
                        )
                        dashed_x_start += dash_change_x + space_change_x
                        dashed_y_start += dash_change_y + space_change_y

                elif line._Line__style == "dotted":
                    circle_size = line._Line__style_type[0]
                    space_width = line._Line__style_type[1]
                    total_width = circle_size + space_width
                    real_x_axis_point_spacing = ((abs(y_start - line._Line__y_end) ** 2) + (
                            self.__x_axis_point_spacing ** 2)) ** (1 / 2)
                    circle_count = real_x_axis_point_spacing / (circle_size + space_width)
                    total_change_x = (line._Line__x_end - x_start)
                    total_change_y = (line._Line__y_end - y_start)
                    circle_change_percentage = circle_size / total_width * 100
                    space_change_percentage = space_width / total_width * 100
                    circle_change_x = (total_change_x / circle_count) / 100 * circle_change_percentage
                    circle_change_y = (total_change_y / circle_count) / 100 * circle_change_percentage
                    space_change_x = (total_change_x / circle_count) / 100 * space_change_percentage
                    space_change_y = (total_change_y / circle_count) / 100 * space_change_percentage
                    dotted_x_start = x_start
                    dotted_y_start = y_start

                    while line._Line__x_end > dotted_x_start:
                        self.__output_canvas.create_oval(
                            dotted_x_start - circle_size / 2,
                            dotted_y_start - circle_size / 2,
                            dotted_x_start + circle_size - circle_size / 2,
                            dotted_y_start + circle_size - circle_size / 2,
                            fill=line._Line__color, outline=line._Line__color
                        )
                        dotted_x_start += circle_change_x + space_change_x
                        dotted_y_start += circle_change_y + space_change_y

                elif line._Line__style == "normal":
                    self.__output_canvas.create_line(
                        x_start, y_start,
                        line._Line__x_end, line._Line__y_end,
                        fill=line._Line__color, width=line._Line__size
                    )

                if line._Line__point_highlight == "enabled" and line._Line__point_highlight_size > 0:
                    highlight_size = line._Line__point_highlight_size / 2
                    self.__output_canvas.create_oval(
                        line._Line__x_end - highlight_size,
                        line._Line__y_end - highlight_size,
                        line._Line__x_end + highlight_size,
                        line._Line__y_end + highlight_size,
                        fill=line._Line__point_highlight_color,
                        outline=line._Line__point_highlight_color
                    )

                    self.__output_canvas.create_oval(
                        x_start - highlight_size,
                        y_start - highlight_size,
                        x_start + highlight_size,
                        y_start + highlight_size,
                        fill=line._Line__point_highlight_color,
                        outline=line._Line__point_highlight_color
                    )

            if re_show_data:
                self.__reshow_data()

    def __hide_pointer(self, event_: tkinter.Event) -> None:
        """
        Hides the pointer widget from the GUI canvas.

        Args:
            event_ (tkinter.Event): The event_ triggering the pointer hiding.
        """
        self.__pointer.place_forget()

    def __return_pointed_values(self, event_: tkinter.Event) -> None:
        """
        Returns the values pointed by the user's mouse cursor.

        Args:
            event_ (tkinter.Event): The mouse event_ containing cursor position.
        """

        def round_x(x) -> Union[int, float]:
            """
            Rounds the x-coordinate to the nearest x-axis point spacing.

            Args:
                x (float): The x-coordinate to be rounded.

            Returns:
                float: The rounded x-coordinate.
            """
            x_: Union[int, float] = (x // self.__x_axis_point_spacing) * self.__x_axis_point_spacing
            if x % self.__x_axis_point_spacing >= self.__x_axis_point_spacing / 2:
                x_ += self.__x_axis_point_spacing
            return x_

        max_view = self.__get_max_visible_data_points()
        max_sup = max_view - 1
        values = []
        max_data = self.__get_max_data_length_across_lines()
        
        try:
            if self.__pointer_lock == "enabled":
                event_x = round_x(event_.x)
            else:
                event_x = event_.x
            if self.__const_real_width >= self.__real_width:
                event_x_converted = event_x
            else:
                event_x_converted = event_x - (self.__x_axis_point_spacing * (max_data - max_view))
            width_x = self.__const_real_width - (self.__const_real_width - (self.__x_axis_point_spacing * max_sup))
            index_float = ((event_x_converted / width_x) * max_sup)
            index_round_float = round(index_float)
            if event_x == self.__real_width:
                self.__pointer.place(x=((event_x - self.__pointer_size / 2) - 2), y=0)
            else:
                self.__pointer.place(x=((event_x - self.__pointer_size / 2) + 1), y=0)
            index_int = int(index_float)
            x_index = index_int
            if index_float != 0 and index_float == index_int:
                x_index -= 1
            for line in self.__lines:
                line._Line__ret_data = line._Line__data + (max_data - len(line._Line__data)) * [None]
                line._Line__ret_data = line._Line__ret_data[-int(max_view)::]
                line._Line__ret_data = line._Line__ret_data + (int(max_view) - len(line._Line__ret_data)) * [None]
            for line in self.__lines:
                try:
                    if self.__pointer_lock == "enabled":
                        value = line._Line__ret_data[int(index_round_float)]
                    else:
                        if index_float == index_int:
                            value = line._Line__ret_data[index_int]
                        else:
                            value = line._Line__ret_data[index_int]
                            value = value + (
                                ((line._Line__ret_data[index_int + 1] - value) * (index_float - index_int)))
                    values.append(Utils._format_float_with_precision(float(value), self.__pointing_values_precision))
                except:
                    values.append("null")
            if self.__pointing_callback_function is not None:
                try:
                    self.__pointing_callback_function(self.__x_axis_values[x_index], values)
                except:
                    self.__pointing_callback_function("null", values)
        except:
            pass
        
    def clear_data(self) -> None:
        """
        Clears the data of all lines within the LineChart object, ensuring the data fits the 
        maximum visible points allowed for the chart.

        This method calculates the maximum number of data points across all lines and the maximum
        number of visible data points allowed. If the total data exceeds the visible points limit, 
        it trims each line's data to retain only the most recent visible data points.

        The method checks the length of the data across all lines and compares it with the maximum 
        visible data points. If necessary, each line's data is cropped by removing earlier data 
        points, retaining only the most recent data within the visible limit.

        Attributes:
            self.__lines: A list of line objects representing each individual line on the chart.
        
        Returns:
            None: This method modifies the internal state of each line's data but does not return any value.
        """
        maximum_data = self.__get_max_data_length_across_lines()
        max_visible_points = self.__get_max_visible_data_points()
        
        for line in self.__lines:
            if maximum_data > max_visible_points:
                line._Line__data = line._Line__data[maximum_data - max_visible_points::]

    def get_lines_data(self, start: int = None, end: int = None, step: int = None) -> Dict[Line, Tuple[int]]:
        """
        Retrieve data points for all lines within a specified range and step.

        Args:
            start (int, optional): The starting index for slicing the data. Defaults to None.
            end (int, optional): The ending index for slicing the data. Defaults to None.
            step (int, optional): The step size for slicing the data. Defaults to None.

        Returns:
            Dict[Line, Tuple[int]]: A dictionary where the key is the line object and the value is a tuple of data points
                sliced from the line's data.
        """
        lines_data = {}
        for line in self.__lines:
            lines_data[line] = tuple(line._Line__data[start: end: step])

        return lines_data
    
    def get_line_data(self, line: Line, start: int = None, end: int = None, step: int = None) -> Tuple[int | float]:
        """
        Retrieve data points for a specific line within a specified range and step.

        Args:
            line (Line): The line object whose data should be retrieved.
            start (int, optional): The starting index for slicing the data. Defaults to None.
            end (int, optional): The ending index for slicing the data. Defaults to None.
            step (int, optional): The step size for slicing the data. Defaults to None.

        Returns:
            Tuple[int | float]: A tuple containing the sliced data points of the specified line.

        Raises:
            ValueError: If the provided line is not valid or does not exist in `self.__lines`.
            TypeError: If the provided line is not an instance of the Line class.
        """
        Validate._is_valid_line(line, "line")
        if line in self.__lines:
            return line.get_data(start=start, end=end, step=step)
        else:
            Validate._invalid_line(line)
    
    def get_x_axis_visible_point_count(self) -> int:
        """
        Get the maximum number of data points that can be visible along the X-axis.

        Returns:
            int: The maximum number of visible data points on the X-axis.
        """
        return self.__get_max_visible_data_points()
    
    def get_lines_visible_data(self) -> Dict[Line, Tuple[int | float]]:
        """
        Retrieve currently visible data points for all lines.

        Determines the visible data points based on the maximum data length across all lines
        and the maximum number of visible points.

        Returns:
            Dict[Line, Tuple[int | float]]: A dictionary where the key is the line object 
                and the value is a tuple of visible data points.
                If no data is visible, the value is an empty tuple.
        """
        maximum_data = self.__get_max_data_length_across_lines()
        max_visible_points = self.__get_max_visible_data_points()
        
        lines_data = {}
        
        for line in self.__lines:
            if maximum_data > max_visible_points:
                lines_data[line] = tuple(line._Line__data[maximum_data - max_visible_points::])
            else:
                lines_data[line] = tuple(line._Line__data)
        return lines_data
    
    def get_line_visible_data(self, line: Line) -> Tuple[int | float]:
        """
        Retrieve currently visible data points for a specific line.

        Args:
            line (Line): The line object whose visible data should be retrieved.

        Returns:
            Tuple[int | float]: A tuple containing the visible data points of the specified line.

        Raises:
            ValueError: If the provided line is not valid or does not exist in `self.__lines`.
            TypeError: If the provided line is not an instance of the Line class.
        """
        Validate._is_valid_line(line, "line")
        if line in self.__lines:
            return line.get_current_visible_data()
        else:
            Validate._invalid_line(line)
            
    def place(
            self,
            x: int = None,
            y: int = None,
            rely: Union[int, float] = None,
            relx: Union[int, float] = None,
            anchor: Literal[
                "n", "e", "s", "w", "ne", "nw", "se", "sw", "center"
            ] = None
    ) -> None:
        """
        Place the widget at a specific position within its parent widget.

        Args:
            x (int): The x-coordinate of the upper-left corner of the widget.
            y (int): The y-coordinate of the upper-left corner of the widget.
            rely (Union[int, float]): The vertical relative position of the widget, ranging from 0 to 1.
            relx (Union[int, float]): The horizontal relative position of the widget, ranging from 0 to 1.
            anchor (str): Specifies which part of the widget is to be placed at the given coordinates.
        """
        self.__main_frame.place(x=x, y=y, rely=rely, relx=relx, anchor=anchor)
        self.__place_info_x = x
        self.__place_info_y = y
        self.__place_info_rely = rely
        self.__place_info_relx = relx
        self.__place_info_anchor = anchor

    def pack(
            self,
            pady: int = None,
            padx: int = None,
            before: Any = None,
            after: Any = None,
            side: Literal["top", "bottom", "left", "right"] = None,
            anchor: Literal[
                "n", "e", "s", "w", "ne", "nw", "se", "sw", "center"
            ] = None
    ) -> None:
        """
        Pack the widget into its parent widget.

        Args:
            pady (int): Vertical padding.
            padx (int): Horizontal padding.
            before (Any): Widget before which this widget will be packed.
            after (Any): Widget after which this widget will be packed.
            side (str): Specifies which side of the parent widget to pack against.
            anchor (str): Specifies where the widget will be placed if the available area is larger than the widget's 
                requested size.
        """
        self.__main_frame.pack(
            pady=pady, padx=padx, before=before,
            after=after, side=side, anchor=anchor
        )
        self.__pack_info_pady = pady
        self.__pack_info_padx = padx
        self.__pack_info_before = before
        self.__pack_info_after = after
        self.__pack_info_side = side
        self.__pack_info_anchor = anchor

    def grid(
        self,
        column: int = None,
        columnspan: int = None,
        padx: int = None,
        pady: int = None,
        row: int = None,
        rowspan: int = None,
        sticky: Literal[
            "n", "e", "s", "w", "ne", "nw", "se", "sw"
        ] = None
    ) -> None:
        """
        Place the widget in a grid layout inside its parent widget.

        All parameters are optional; if not specified, existing grid options are retained.

        Args:
            column (int): The column index to place the widget.
            columnspan (int): The number of columns the widget spans.
            padx (int): Horizontal padding (in pixels).
            pady (int): Vertical padding (in pixels).
            row (int): The row index to place the widget.
            rowspan (int): The number of rows the widget spans.
            sticky (str): How the widget expands to fill the grid cell.
                Can be any combination of 'n', 'e', 's', 'w' representing
                north, east, south, and west directions.
        """
        self.__main_frame.grid(
            column=column, columnspan=columnspan,
            padx=padx, pady=pady, row=row,
            rowspan=rowspan, sticky=sticky
        )
        self.__grid_info_column = column
        self.__grid_info_columnspan = columnspan
        self.__grid_info_padx = padx
        self.__grid_info_pady = pady
        self.__grid_info_row = row
        self.__grid_info_rowspan = rowspan
        self.__grid_info_sticky = sticky

    def place_forget(self) -> None:
        """
        Remove the widget from the grid.
        """
        self.__main_frame.place_forget()
        self.__place_info_x = None
        self.__place_info_y = None
        self.__place_info_rely = None
        self.__place_info_relx = None
        self.__place_info_anchor = None

    def pack_forget(self) -> None:
        """
        Remove the widget from the pack.
        """
        self.__main_frame.pack_forget()
        self.__pack_info_pady = None
        self.__pack_info_padx = None
        self.__pack_info_before = None
        self.__pack_info_after = None
        self.__pack_info_side = None
        self.__pack_info_anchor = None

    def grid_forget(self) -> None:
        """
        Remove the widget from the grid.
        """
        self.__main_frame.grid_forget()
        self.__grid_info_column = None
        self.__grid_info_columnspan = None
        self.__grid_info_padx = None
        self.__grid_info_pady = None
        self.__grid_info_row = None
        self.__grid_info_rowspan = None
        self.__grid_info_sticky = None

    def set_line_visibility(self, line: Line, state: bool) -> None:
        """
        Show or hide a specific line on the chart.

        Args:
            line (Line): The line object to show or hide.
            state (bool): True to show the line, False to hide it.

        Raises:
            ValueError: If the provided line is invalid or not part of the chart.
            TypeError: If the state is not a boolean.
        """
        Validate._is_valid_line(line, "line")
        Validate._is_bool(state, "state")
        if line._Line__visibility != state or self.__visibility != state:
            line._Line__visibility = state
            self.__reshow_data()

    def set_lines_visibility(self, state: bool) -> None:
        """
        Hide or show all lines.

        Args:
            state (bool): The hide/show state of all lines.
        
        Raises:
            TypeError: If the provided state is not a boolean value.
        """
        Validate._is_bool(state, "state")
        self.__visibility = state
        if state is False:
            self.__output_canvas.place_forget()
        for line in self.__lines:
            line._Line__visibility = state
        self.__reshow_data()

    def reset(self) -> None:
        """
        Reset the chart and lines to their initial state.
        """
        self.__reset_chart_info()
        self.__reset_lines_info()

    def __apply_line_configuration(self) -> None:
        """
        Apply changes to the lines and redraw the chart.
        """
        self.__reshow_data()

    def cget(
        self,
        attribute_name: Literal[
            "width", "height", "axis_color", "bg_color", "fg_color",
            "data_font_style", "axis_font_style", "y_axis_precision",
            "y_axis_data", "y_axis_label_count", "y_axis_values",
            "y_axis_font_color", "y_axis_data_font_color",
            "y_axis_data_position", "y_axis_section_count",
            "y_axis_section_style", "y_axis_section_style_type",
            "y_axis_section_color", "x_axis_data", "x_axis_label_count",
            "x_axis_values", "x_axis_display_values_indices",
            "x_axis_font_color", "x_axis_data_font_color",
            "x_axis_data_position", "x_axis_section_count",
            "x_axis_section_style", "x_axis_section_style_type",
            "x_axis_section_color", "x_axis_point_spacing",
            "y_space", "x_space", "pointer_state",
            "pointing_callback_function", "pointer_color",
            "pointing_values_precision", "pointer_lock",
            "pointer_size", "__all__"
        ] = "__all__"
    ) -> Any:
        """
        Retrieve the value of a specific configuration attribute.

        Args:
            attribute_name (str): The name of the attribute to retrieve.
                Pass "__all__" to retrieve a dictionary of all configurable attributes
                and their current values.

        Returns:
            Any: The value of the requested attribute, or a dictionary of all
                attributes if "__all__" is passed.

        Raises:
            ValueError: If the given attribute name is not recognized.
        """
        if attribute_name == "width":
            return self.__width
        elif attribute_name == "height":
            return self.__height
        elif attribute_name == "axis_color":
            return self.__axis_color
        elif attribute_name == "bg_color":
            return self.__bg_color
        elif attribute_name == "fg_color":
            return self.__fg_color
        elif attribute_name == "data_font_style":
            return self.__data_font_style
        elif attribute_name == "axis_font_style":
            return self.__axis_font_style
        elif attribute_name == "y_axis_precision":
            return self.__y_axis_precision
        elif attribute_name == "y_axis_data":
            return self.__y_axis_data
        elif attribute_name == "y_axis_label_count":
            return self.__y_axis_label_count
        elif attribute_name == "y_axis_values":
            return self.__y_axis_values
        elif attribute_name == "y_axis_font_color":
            return self.__y_axis_font_color
        elif attribute_name == "y_axis_data_font_color":
            return self.__y_axis_data_font_color
        elif attribute_name == "y_axis_data_position":
            return self.__y_axis_data_position
        elif attribute_name == "y_axis_section_count":
            return self.__y_axis_section_count
        elif attribute_name == "y_axis_section_style":
            return self.__y_axis_section_style
        elif attribute_name == "y_axis_section_style_type":
            return self.__y_axis_section_style_type
        elif attribute_name == "y_axis_section_color":
            return self.__y_axis_section_color
        elif attribute_name == "x_axis_data":
            return self.__x_axis_data
        elif attribute_name == "x_axis_label_count":
            return self.__x_axis_label_count
        elif attribute_name == "x_axis_values":
            return self.__x_axis_values
        elif attribute_name == "x_axis_display_values_indices":
            return self.__x_axis_display_values_indices
        elif attribute_name == "x_axis_font_color":
            return self.__x_axis_font_color
        elif attribute_name == "x_axis_data_font_color":
            return self.__x_axis_data_font_color
        elif attribute_name == "x_axis_data_position":
            return self.__x_axis_data_position
        elif attribute_name == "x_axis_section_count":
            return self.__x_axis_section_count
        elif attribute_name == "x_axis_section_style":
            return self.__x_axis_section_style
        elif attribute_name == "x_axis_section_style_type":
            return self.__x_axis_section_style_type
        elif attribute_name == "x_axis_section_color":
            return self.__x_axis_section_color
        elif attribute_name == "x_axis_point_spacing":
            return self.__x_axis_point_spacing
        elif attribute_name == "y_space":
            return self.__y_space
        elif attribute_name == "x_space":
            return self.__x_space
        elif attribute_name == "pointer_state":
            return self.__pointer_state
        elif attribute_name == "pointing_callback_function":
            return self.__pointing_callback_function
        elif attribute_name == "pointer_color":
            return self.__pointer_color
        elif attribute_name == "pointing_values_precision":
            return self.__pointing_values_precision
        elif attribute_name == "pointer_lock":
            return self.__pointer_lock
        elif attribute_name == "pointer_size":
            return self.__pointer_size
        elif attribute_name == "__all__":
            return {
                "width": self.__width,
                "height": self.__height,
                "axis_color": self.__axis_color,
                "bg_color": self.__bg_color,
                "fg_color": self.__fg_color,
                "data_font_style": self.__data_font_style,
                "axis_font_style": self.__axis_font_style,
                "y_axis_precision": self.__y_axis_precision,
                "y_axis_data": self.__y_axis_data,
                "y_axis_label_count": self.__y_axis_label_count,
                "y_axis_values": self.__y_axis_values,
                "y_axis_font_color": self.__y_axis_font_color,
                "y_axis_data_font_color": self.__y_axis_data_font_color,
                "y_axis_data_position": self.__y_axis_data_position,
                "y_axis_section_count": self.__y_axis_section_count,
                "y_axis_section_style": self.__y_axis_section_style,
                "y_axis_section_style_type": self.__y_axis_section_style_type,
                "y_axis_section_color": self.__y_axis_section_color,
                "x_axis_data": self.__x_axis_data,
                "x_axis_label_count": self.__x_axis_label_count,
                "x_axis_values": self.__x_axis_values,
                "x_axis_display_values_indices": self.__x_axis_display_values_indices,
                "x_axis_font_color": self.__x_axis_font_color,
                "x_axis_data_font_color": self.__x_axis_data_font_color,
                "x_axis_data_position": self.__x_axis_data_position,
                "x_axis_section_count": self.__x_axis_section_count,
                "x_axis_section_style": self.__x_axis_section_style,
                "x_axis_section_style_type": self.__x_axis_section_style_type,
                "x_axis_section_color": self.__x_axis_section_color,
                "x_axis_point_spacing": self.__x_axis_point_spacing,
                "y_space": self.__y_space,
                "x_space": self.__x_space,
                "pointer_state": self.__pointer_state,
                "pointing_callback_function": self.__pointing_callback_function,
                "pointer_color": self.__pointer_color,
                "pointing_values_precision": self.__pointing_values_precision,
                "pointer_lock": self.__pointer_lock,
                "pointer_size": self.__pointer_size
            }
        else:
            Validate._invalid_cget(attribute_name)

    def get_line_visibility(self, line: Line):
        """
        Get the visibility state of a specific line.

        Args:
            line (Line): The Line object for which visibility is queried.

        Returns:
            bool: True if the line is visible, False otherwise.

        Raises:
            TypeError: If the provided line is not an instance of CTkLine.
            ValueError: If the provided line object is not valid or not found in the chart.
        """
        Validate._is_valid_line(line, "line")
        if line in self.__lines:
            return line._Line__visibility
        else:
            Validate._invalid_line(line)
            
    def get_lines_area(self):
        """
        Get the area of all lines.

        Returns:
            float: The area of the lines.
        """
        total_area = 0
        for line in self.__lines:
            total_area += self.get_line_area(line)
        return total_area
            
    def get_line_area(self, line: Line):
        """
        Get the area of a specific line.

        Args:
            line (Line): The Line object for which the area is queried.

        Returns:
            float: The area of the line.

        Raises:
            ValueError: If the provided line object is not valid or not found in the chart.
        """
        Validate._is_valid_line(line, "line")
        if line not in self.__lines:
            Validate._invalid_line(line)

        maximum_data = self.__get_max_data_length_across_lines()
        max_visible_points = self.__get_max_visible_data_points()
        
        if maximum_data > max_visible_points:
            line._Line__temp_data = line._Line__data[maximum_data - max_visible_points::]
        else:
            line._Line__temp_data = line._Line__data
                
        # print(self.__x_axis_point_spacing)
        total_area = 0
        for i, data in enumerate(line._Line__temp_data[0: -1]):
            area = ((data - self.__y_axis_min_value)  + (line._Line__temp_data[i+1] - self.__y_axis_min_value)) * self.__x_axis_point_spacing * 1/2
            # print("-" * 20)
            # print(f"(({data - self.__y_axis_min_value}) + ({line._Line__temp_data[i+1] - self.__y_axis_min_value})) * { self.__x_axis_point_spacing} * 1/2 = {area}")
            total_area += area
        
        return total_area

    def place_info(
            self,
            attribute_name: Literal[
                "x", "y", "relx", "rely", "anchor", "__all__"
            ] = "__all__"
    ) -> Any:
        """
        Get the value of the specified place info.

        Args:
            attribute_name (str): The name of the attribute to get.

        Returns:
            Any: The value of the specified attribute.
            
        Raises:
            ValueError: If the given attribute name is not recognized.
        """
        if attribute_name == "x":
            return self.__place_info_x
        elif attribute_name == "y":
            return self.__place_info_y
        elif attribute_name == "relx":
            return self.__place_info_relx
        elif attribute_name == "rely":
            return self.__place_info_rely
        elif attribute_name == "anchor":
            return self.__place_info_anchor
        elif attribute_name == "__all__":
            return {
                "x": self.__place_info_x,
                "y": self.__place_info_y,
                "relx": self.__place_info_relx,
                "rely": self.__place_info_rely,
                "anchor": self.__place_info_anchor
            }
        else:
            Validate._invalid_cget(attribute_name)

    def pack_info(
            self,
            attribute_name: Literal[
                "padx", "pady", "before", "after",
                "side", "anchor", "__all__"
            ] = "__all__"
    ) -> Any:
        """
        Get the value of the specified pack info.

        Args:
            attribute_name (str): The name of the attribute to get.

        Returns:
            Any: The value of the specified attribute.
            
        Raises:
            ValueError: If the given attribute name is not recognized.
        """
        if attribute_name == "padx":
            return self.__pack_info_padx
        elif attribute_name == "pady":
            return self.__pack_info_pady
        elif attribute_name == "before":
            return self.__pack_info_before
        elif attribute_name == "after":
            return self.__pack_info_after
        elif attribute_name == "side":
            return self.__pack_info_side
        elif attribute_name == "anchor":
            return self.__pack_info_anchor
        elif attribute_name == "__all__":
            return {
                "padx": self.__pack_info_padx,
                "pady": self.__pack_info_pady,
                "before": self.__pack_info_before,
                "after": self.__pack_info_after,
                "side": self.__pack_info_side,
                "anchor": self.__pack_info_anchor
            }
        else:
            Validate._invalid_cget(attribute_name)

    def grid_info(
            self,
            attribute_name: Literal[
                "row", "column", "rowspan", "columnspan",
                "padx", "pady", "sticky", "__all__"
            ] = "__all__"
    ) -> Any:
        """
        Get the value of the specified grid info.

        Args:
            attribute_name (str): The name of the attribute to get.

        Returns:
            Any: The value of the specified attribute.
            
        Raises:
            ValueError: If the given attribute name is not recognized.
        """
        if attribute_name == "row":
            return self.__grid_info_row
        elif attribute_name == "column":
            return self.__grid_info_column
        elif attribute_name == "rowspan":
            return self.__grid_info_rowspan
        elif attribute_name == "columnspan":
            return self.__grid_info_columnspan
        elif attribute_name == "padx":
            return self.__grid_info_padx
        elif attribute_name == "pady":
            return self.__grid_info_pady
        elif attribute_name == "sticky":
            return self.__grid_info_sticky

        elif attribute_name == "__all__":
            return {
                "row": self.__grid_info_row,
                "column": self.__grid_info_column,
                "rowspan": self.__grid_info_rowspan,
                "columnspan": self.__grid_info_columnspan,
                "padx": self.__grid_info_padx,
                "pady": self.__grid_info_pady,
                "sticky": self.__grid_info_sticky
            }
        else:
            Validate._invalid_cget(attribute_name)

    def __del__(self) -> None:
        """
        Destructor to clean up resources and perform necessary cleanup.
        This method will be called when the object is about to be destroyed.
        It ensures that all widgets are destroyed and attributes are deleted
        to aid in garbage collection.
        """
        # Destroy widgets
        try:
            self.__main_frame.destroy()
        except Exception as error:
            print(error)
            return
        
        self.__x_axis_values_frame.destroy()
        self.__y_axis_values_frame.destroy()
        self.__y_axis_data_label.destroy()
        self.__x_axis_data_label.destroy()
        self.__output_frame.destroy()
        self.__output_canvas.destroy()
        self.__y_axis_frame.destroy()
        self.__x_axis_frame.destroy()
        self.__pointer.destroy()

        # Deleting attributes to help with garbage collection
        del self.__main_frame
        del self.__x_axis_values_frame
        del self.__y_axis_values_frame
        del self.__y_axis_data_label
        del self.__x_axis_data_label
        del self.__output_frame
        del self.__output_canvas
        del self.__y_axis_frame
        del self.__x_axis_frame
        del self.__pointer
        del self.__master
        del self.__height
        del self.__width
        del self.__axis_size
        del self.__axis_color
        del self.__x_axis_point_spacing
        del self.__x_axis_point_spacing_handle_by
        del self.__data_font_style
        del self.__axis_font_style
        del self.__lines
        del self.__bg_color
        del self.__fg_color
        del self.__y_axis_font_color
        del self.__y_axis_data_font_color
        del self.__y_axis_section_color
        del self.__y_axis_section_style
        del self.__y_axis_section_style_type
        del self.__y_axis_section_count
        del self.__y_axis_label_count
        del self.__y_axis_data
        del self.__y_axis_data_position
        del self.__y_axis_values
        del self.__y_axis_min_value
        del self.__y_axis_max_value
        del self.__y_axis_precision
        del self.__y_space
        del self.__x_axis_font_color
        del self.__x_axis_data_font_color
        del self.__x_axis_section_color
        del self.__x_axis_section_style
        del self.__x_axis_section_style_type
        del self.__x_axis_section_count
        del self.__x_axis_label_count
        del self.__x_axis_display_values_indices
        del self.__x_labels_values_index_change
        del self.__x_axis_data
        del self.__x_axis_data_position
        del self.__x_axis_values
        del self.__x_axis_values_handle_by
        del self.__x_space
        del self.__pointer_state
        del self.__pointing_callback_function
        del self.__pointing_values_precision
        del self.__pointer_lock
        del self.__pointer_size
        del self.__pointer_color
        del self.__x_values_frame_place_req
        del self.__y_values_frame_place_req
        del self.__place_x
        del self.__real_height
        del self.__real_width
        del self.__const_real_height
        del self.__const_real_width
        del self.__visibility
        del self.__place_info_x
        del self.__place_info_y
        del self.__place_info_rely
        del self.__place_info_relx
        del self.__place_info_anchor
        del self.__pack_info_pady
        del self.__pack_info_padx
        del self.__pack_info_before
        del self.__pack_info_after
        del self.__pack_info_side
        del self.__pack_info_anchor
        del self.__grid_info_column
        del self.__grid_info_columnspan
        del self.__grid_info_padx
        del self.__grid_info_pady
        del self.__grid_info_row
        del self.__grid_info_rowspan
        del self.__grid_info_sticky

    def destroy(self) -> None:
        """
        Cleanly destroy the line chart and all associated widgets.

        This method removes all line elements from the chart, then performs full cleanup
        by calling the internal destructor to release remaining resources.
        It should be called explicitly to ensure proper widget and memory cleanup.
        """
        for line in self.__lines:
            line.destroy()

        self.__del__()

    # -------------------------------------------------------------------------
    # Individual configure_* methods
    # Each method configures exactly one attribute by delegating to configure().
    # The existing configure() method is NOT modified.
    # -------------------------------------------------------------------------

    def configure_width(self, width: int) -> None:
        """Configure the width of the LineChart widget.

        Args:
            width (int): New width in pixels.

        Raises:
            TypeError: If width is not an integer.
        """
        self.configure(width=width)

    def configure_height(self, height: int) -> None:
        """Configure the height of the LineChart widget.

        Args:
            height (int): New height in pixels.

        Raises:
            TypeError: If height is not an integer.
        """
        self.configure(height=height)

    def configure_axis_size(self, axis_size: int) -> None:
        """Configure the thickness/size of the axis lines.

        Args:
            axis_size (int): New axis size in pixels.

        Raises:
            TypeError: If axis_size is not an integer.
        """
        self.configure(axis_size=axis_size)

    def configure_x_axis_point_spacing(self, x_axis_point_spacing: Union[int, Literal["auto"]]) -> None:
        """Configure the spacing between data points on the x-axis.

        Args:
            x_axis_point_spacing (Union[int, str]): Pixel spacing between points, or ``"auto"``
                to let the chart calculate it automatically.

        Raises:
            TypeError: If the value is not an integer or ``"auto"``.
        """
        self.configure(x_axis_point_spacing=x_axis_point_spacing)

    def configure_bg_color(self, bg_color: str) -> None:
        """Configure the background color of the LineChart widget.

        Args:
            bg_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(bg_color=bg_color)

    def configure_axis_color(self, axis_color: str) -> None:
        """Configure the color of the axis lines.

        Args:
            axis_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(axis_color=axis_color)

    def configure_fg_color(self, fg_color: str) -> None:
        """Configure the foreground (plot area) color of the LineChart widget.

        Args:
            fg_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(fg_color=fg_color)

    def configure_data_font_style(self, data_font_style: Tuple[str, int, str]) -> None:
        """Configure the font style used for axis data labels (e.g. \"X\", \"Y\" labels).

        Args:
            data_font_style (Tuple[str, int, str]): A tuple of (family, size, weight),
                e.g. ``("arial", 10, "bold")``.

        Raises:
            TypeError: If the tuple does not match the expected font format.
        """
        self.configure(data_font_style=data_font_style)

    def configure_axis_font_style(self, axis_font_style: Tuple[str, int, str]) -> None:
        """Configure the font style used for axis value labels (tick labels).

        Args:
            axis_font_style (Tuple[str, int, str]): A tuple of (family, size, weight),
                e.g. ``("arial", 8, "normal")``.

        Raises:
            TypeError: If the tuple does not match the expected font format.
        """
        self.configure(axis_font_style=axis_font_style)

    def configure_y_axis_values(self, y_axis_values: Tuple[Union[int, float], Union[int, float]]) -> None:
        """Configure the minimum and maximum values displayed on the y-axis.

        Args:
            y_axis_values (Tuple[Union[int, float], Union[int, float]]): A tuple of
                ``(min_value, max_value)``.

        Raises:
            ValueError: If the tuple is invalid.
        """
        self.configure(y_axis_values=y_axis_values)

    def configure_y_axis_precision(self, y_axis_precision: int) -> None:
        """Configure the decimal precision of y-axis value labels.

        Args:
            y_axis_precision (int): Number of decimal places (0 = integers).

        Raises:
            TypeError: If y_axis_precision is not an integer.
        """
        self.configure(y_axis_precision=y_axis_precision)

    def configure_y_axis_font_color(self, y_axis_font_color: str) -> None:
        """Configure the color of y-axis tick (value) labels.

        Args:
            y_axis_font_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(y_axis_font_color=y_axis_font_color)

    def configure_y_axis_data_font_color(self, y_axis_data_font_color: str) -> None:
        """Configure the color of the y-axis data title label.

        Args:
            y_axis_data_font_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(y_axis_data_font_color=y_axis_data_font_color)

    def configure_y_axis_section_count(self, y_axis_section_count: int) -> None:
        """Configure the number of horizontal grid sections on the y-axis.

        Args:
            y_axis_section_count (int): Number of sections (0 disables sections).

        Raises:
            TypeError: If y_axis_section_count is not an integer.
        """
        self.configure(y_axis_section_count=y_axis_section_count)

    def configure_y_axis_section_color(self, y_axis_section_color: str) -> None:
        """Configure the color of y-axis grid section lines.

        Args:
            y_axis_section_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(y_axis_section_color=y_axis_section_color)

    def configure_y_axis_section_style(self, y_axis_section_style: Literal["normal", "dashed"]) -> None:
        """Configure the style of y-axis grid section lines.

        Args:
            y_axis_section_style (str): Either ``"normal"`` or ``"dashed"``.

        Raises:
            ValueError: If the value is not ``"normal"`` or ``"dashed"``.
        """
        self.configure(y_axis_section_style=y_axis_section_style)

    def configure_y_axis_section_style_type(self, y_axis_section_style_type: Tuple[int, int]) -> None:
        """Configure the dash width and gap for dashed y-axis sections.

        Args:
            y_axis_section_style_type (Tuple[int, int]): A tuple of
                ``(dash_width, gap_width)`` in pixels.

        Raises:
            TypeError: If the tuple does not match the expected format.
        """
        self.configure(y_axis_section_style_type=y_axis_section_style_type)

    def configure_y_axis_label_count(self, y_axis_label_count: int) -> None:
        """Configure the number of value labels shown on the y-axis.

        Args:
            y_axis_label_count (int): Number of y-axis labels (0 hides all labels).

        Raises:
            TypeError: If y_axis_label_count is not an integer.
        """
        self.configure(y_axis_label_count=y_axis_label_count)

    def configure_y_axis_data(self, y_axis_data: Any) -> None:
        """Configure the title/label text for the y-axis.

        Args:
            y_axis_data (Any): The label text (will be converted to string).
        """
        self.configure(y_axis_data=y_axis_data)

    def configure_y_axis_data_position(self, y_axis_data_position: Literal["top", "side"]) -> None:
        """Configure the position of the y-axis title label.

        Args:
            y_axis_data_position (str): Either ``"top"`` (above the y-axis) or
                ``"side"`` (beside the y-axis).

        Raises:
            ValueError: If the value is not ``"top"`` or ``"side"``.
        """
        self.configure(y_axis_data_position=y_axis_data_position)

    def configure_y_space(self, y_space: int) -> None:
        """Configure the extra vertical space between the y-axis and the plot area.

        Args:
            y_space (int): Space in pixels.

        Raises:
            TypeError: If y_space is not an integer.
        """
        self.configure(y_space=y_space)

    def configure_x_axis_values(self, x_axis_values: Tuple[Any, ...]) -> None:
        """Configure the values/labels displayed on the x-axis.

        Args:
            x_axis_values (Tuple[Any, ...]): A tuple of x-axis label values.

        Raises:
            ValueError: If the tuple format is invalid.
        """
        self.configure(x_axis_values=x_axis_values)

    def configure_x_axis_data(self, x_axis_data: Any) -> None:
        """Configure the title/label text for the x-axis.

        Args:
            x_axis_data (Any): The label text (will be converted to string).
        """
        self.configure(x_axis_data=x_axis_data)

    def configure_x_axis_font_color(self, x_axis_font_color: str) -> None:
        """Configure the color of x-axis tick (value) labels.

        Args:
            x_axis_font_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(x_axis_font_color=x_axis_font_color)

    def configure_x_axis_data_font_color(self, x_axis_data_font_color: str) -> None:
        """Configure the color of the x-axis data title label.

        Args:
            x_axis_data_font_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(x_axis_data_font_color=x_axis_data_font_color)

    def configure_x_axis_label_count(self, x_axis_label_count: int) -> None:
        """Configure the number of labels shown on the x-axis.

        Args:
            x_axis_label_count (int): Number of x-axis labels (0 hides all labels).

        Raises:
            TypeError: If x_axis_label_count is not an integer.
        """
        self.configure(x_axis_label_count=x_axis_label_count)

    def configure_x_axis_section_count(self, x_axis_section_count: int) -> None:
        """Configure the number of vertical grid sections on the x-axis.

        Args:
            x_axis_section_count (int): Number of sections (0 disables sections).

        Raises:
            TypeError: If x_axis_section_count is not an integer.
        """
        self.configure(x_axis_section_count=x_axis_section_count)

    def configure_x_axis_section_style(self, x_axis_section_style: Literal["normal", "dashed"]) -> None:
        """Configure the style of x-axis grid section lines.

        Args:
            x_axis_section_style (str): Either ``"normal"`` or ``"dashed"``.

        Raises:
            ValueError: If the value is not ``"normal"`` or ``"dashed"``.
        """
        self.configure(x_axis_section_style=x_axis_section_style)

    def configure_x_axis_section_style_type(self, x_axis_section_style_type: Tuple[int, int]) -> None:
        """Configure the dash height and gap for dashed x-axis sections.

        Args:
            x_axis_section_style_type (Tuple[int, int]): A tuple of
                ``(dash_height, gap_height)`` in pixels.

        Raises:
            TypeError: If the tuple does not match the expected format.
        """
        self.configure(x_axis_section_style_type=x_axis_section_style_type)

    def configure_x_axis_section_color(self, x_axis_section_color: str) -> None:
        """Configure the color of x-axis grid section lines.

        Args:
            x_axis_section_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(x_axis_section_color=x_axis_section_color)

    def configure_x_axis_display_values_indices(
            self, x_axis_display_values_indices: Tuple[int, ...]
    ) -> None:
        """Configure which x-axis value indices are displayed as labels.

        Args:
            x_axis_display_values_indices (Tuple[int, ...]): A tuple of integer indices
                into ``x_axis_values`` that should be displayed.

        Raises:
            ValueError: If any index is out of range for the current x_axis_values.
        """
        self.configure(x_axis_display_values_indices=x_axis_display_values_indices)

    def configure_x_axis_data_position(self, x_axis_data_position: Literal["top", "side"]) -> None:
        """Configure the position of the x-axis title label.

        Args:
            x_axis_data_position (str): Either ``"top"`` (right end) or ``"side"`` (below).

        Raises:
            ValueError: If the value is not ``"top"`` or ``"side"``.
        """
        self.configure(x_axis_data_position=x_axis_data_position)

    def configure_x_space(self, x_space: int) -> None:
        """Configure the extra horizontal space between the x-axis and the plot area.

        Args:
            x_space (int): Space in pixels.

        Raises:
            TypeError: If x_space is not an integer.
        """
        self.configure(x_space=x_space)

    def configure_pointer_state(self, pointer_state: Literal["enabled", "disabled"]) -> None:
        """Configure whether the hover pointer is enabled or disabled.

        Args:
            pointer_state (str): Either ``"enabled"`` or ``"disabled"``.

        Raises:
            ValueError: If the value is not ``"enabled"`` or ``"disabled"``.
        """
        self.configure(pointer_state=pointer_state)

    def configure_pointing_values_precision(self, pointing_values_precision: int) -> None:
        """Configure the decimal precision of values displayed by the hover pointer.

        Args:
            pointing_values_precision (int): Number of decimal places.

        Raises:
            TypeError: If pointing_values_precision is not an integer.
        """
        self.configure(pointing_values_precision=pointing_values_precision)

    def configure_pointer_color(self, pointer_color: str) -> None:
        """Configure the color of the hover pointer line.

        Args:
            pointer_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(pointer_color=pointer_color)

    def configure_pointer_lock(self, pointer_lock: Literal["enabled", "disabled"]) -> None:
        """Configure whether the pointer snaps to the nearest data point (lock) or moves freely.

        Args:
            pointer_lock (str): Either ``"enabled"`` (snap to points) or ``"disabled"`` (free).

        Raises:
            ValueError: If the value is not ``"enabled"`` or ``"disabled"``.
        """
        self.configure(pointer_lock=pointer_lock)

    def configure_pointing_callback_function(self, pointing_callback_function: Callable) -> None:
        """Configure the callback function invoked when the pointer moves.

        The callback receives ``(x_value, [y_values...])`` as arguments.

        Args:
            pointing_callback_function (Callable): A callable with signature
                ``(x_value, values_list)``.

        Raises:
            TypeError: If the argument is not callable.
        """
        self.configure(pointing_callback_function=pointing_callback_function)

    def configure_pointer_size(self, pointer_size: int) -> None:
        """Configure the width (in pixels) of the hover pointer line.

        Args:
            pointer_size (int): Pointer width in pixels.

        Raises:
            TypeError: If pointer_size is not an integer.
        """
        self.configure(pointer_size=pointer_size)
