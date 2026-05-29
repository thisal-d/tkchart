from typing import Tuple, Literal, Any
from .Validate import Validate


class Line:
    current_usable_id = 1
    def __init__(
            self,
            master: Any = None,
            color: str = "#768df1",
            size: int = 1,
            style: Literal["normal", "dashed", "dotted"] = "normal",
            style_type: Tuple[int, int] = (4, 4),
            point_highlight: Literal["enabled", "disabled"] = "disabled",
            point_highlight_size: int = 4,
            point_highlight_color: str = "#768df1",
            fill: Literal["enabled", "disabled"] = "disabled",
            fill_color: str = "#5d6db6",
            *args: Any
    ) -> None:
        """
        Initialize a Line object.

        Args:
            master (LineChart): The master object.
            color (str): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (str): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (str): The color of the fill for the line.
        
        Raises:
            TypeError: If any of the parameters are of an incorrect type.
            ValueError: If any of the parameters are invalid.
        """
        if master is None:
            if len(args) != 0:
                master = args[0]
            else:
                Validate._master_att_not_provided_for_line("master")

        Validate._is_valid_line_chart(master, "master")
        Validate._is_valid_color(color, "color")
        Validate._is_int(size, "size")
        Validate._is_valid_line_style(style, "style")
        Validate._is_valid_style_type(style_type, "style_type")
        Validate._is_valid_line_highlight(point_highlight, "point_highlight")
        Validate._is_int(point_highlight_size, "point_highlight_size")
        Validate._is_valid_color(point_highlight_color, "point_highlight_color")
        Validate._is_valid_line_fill(fill, "fill")
        Validate._is_valid_color(fill_color, "fill_color")

        # id (int): The id of the line. need  unique
        self.__id = Line.current_usable_id
        Line.current_usable_id += 1
        
        self.__master = master
        self.__color = color
        self.__size = size
        self.__y_end = 0
        self.__x_end = self.__master._LineChart__x_axis_point_spacing * -1
        self.__data = []
        self.__temp_data = []
        self.__ret_data = []
        self.__visibility = self.__master._LineChart__visibility
        self.__style = style
        self.__style_type = style_type
        self.__point_highlight = point_highlight
        self.__point_highlight_size = point_highlight_size
        self.__point_highlight_color = point_highlight_color
        self.__fill = fill
        self.__fill_color = fill_color

        self.__master._LineChart__lines.append(self)

    def configure(
            self,
            color: str = None,
            size: int = None,
            style: Literal["normal", "dashed", "dotted"] = None,
            style_type: Tuple[int, int] = None,
            point_highlight: Literal["enabled", "disabled"] = None,
            point_highlight_size: int = None,
            point_highlight_color: str = None,
            fill: Literal["enabled", "disabled"] = None,
            fill_color: str = None
    ) -> None:
        """
        Configure attributes of the Line object.

        Args:
            color (str): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (str): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (str): The color of the fill for the line.
        
        Raises:
            TypeError: If any of the parameters are of an incorrect type.
            ValueError: If any of the parameters are invalid.
        """
        changes_req = False

        if color is not None:
            Validate._is_valid_color(color, "color")
            self.__color = color
            changes_req = True

        if size is not None:
            Validate._is_int(size, "size")
            self.__size = size
            changes_req = True

        if style is not None:
            Validate._is_valid_line_style(style, "style")
            self.__style = style
            changes_req = True

        if style_type is not None:
            Validate._is_valid_style_type(style_type, "style_type")
            self.__style_type = style_type
            changes_req = True

        if point_highlight is not None:
            Validate._is_valid_line_highlight(point_highlight, "point_highlight")
            self.__point_highlight = point_highlight
            changes_req = True

        if point_highlight_size is not None:
            Validate._is_int(point_highlight_size, "point_highlight_size")
            self.__point_highlight_size = point_highlight_size
            changes_req = True

        if point_highlight_color is not None:
            Validate._is_valid_color(point_highlight_color, "point_highlight_color")
            self.__point_highlight_color = point_highlight_color
            changes_req = True

        if fill is not None:
            Validate._is_valid_line_fill(fill, "fill")
            self.__fill = fill
            changes_req = True

        if fill_color is not None:
            Validate._is_valid_color(fill_color, "fill_color")
            self.__fill_color = fill_color
            changes_req = True

        if changes_req:
            self.__master._LineChart__apply_line_configuration()
            
    def get_id(self) -> int:
        """
        Get the unique identifier of the Line object.
        
        Returns:
            int: The unique identifier of the line.
        """
        return self.__id
    
    def __reset_positions(self) -> None:
        """
        Reset the Line object.
        """
        self.__y_end = 0
        self.__x_end = self.__master._LineChart__x_axis_point_spacing * -1
        
    def __reset_data(self) -> None:
        self.__data = []
        
    def clear_data(self) -> None:
        """
        Clears the chart data, ensuring that only the relevant visible data is retained.

        This method works by checking the maximum number of data points across all lines in the chart 
        and the maximum number of visible data points. If the chart contains more data points than 
        the visible limit, the data is cropped so that only the most recent data points (up to the 
        visible limit) are kept. If the chart is already within the visible limit, the data is not altered.

        The data is trimmed from the beginning of the dataset, and the most recent points are kept.
        
        This ensures that the chart does not display more data than the allowed visible limit, 
        optimizing performance and display consistency.

        Attributes:
            self.__data: The internal list that holds all the data for the lines on the chart.

        Returns:
            None: This method modifies the internal state of the data but does not return any value.
        """
        maximum_data = self.__master._LineChart__get_max_data_length_across_lines()
        max_visible_points = self.__master._LineChart__get_max_visible_data_points()
        
        if maximum_data > max_visible_points:
            self.__data = self.__data[maximum_data - max_visible_points::]

    def get_data(self, start: int = None, end: int = None, step: int = None) -> Tuple[int | float]:
        """
        Retrieve data points from the specified range and step.

        Args:
            start (int, optional): The starting index for slicing the data. Defaults to None.
            end (int, optional): The ending index for slicing the data. Defaults to None.
            step (int, optional): The step size for slicing the data. Defaults to None.

        Returns:
            Tuple[int | float]: A tuple of data points from the specified range and step.
        """
        return tuple(self.__data[start: end: step])
    
    def get_current_visible_data(self) -> Tuple[int | float]:
        """
        Retrieve the currently visible data points.

        Determines visible data points based on the maximum data length across all lines
        and the maximum number of visible points.

        Returns:
            Tuple[int | float]: A tuple of currently visible data points.
                If no data is visible, an empty tuple is returned.
        """
        maximum_data = self.__master._LineChart__get_max_data_length_across_lines()
        max_visible_points = self.__master._LineChart__get_max_visible_data_points()
        
        if maximum_data > max_visible_points:
            data = tuple(self.__data[maximum_data - max_visible_points::])
        else:
            data = tuple(self.__data)
        return data
    
    def get_x_axis_visible_point_count(self) -> int:
        """
        Get the maximum number of data points that can be visible along the X-axis.

        Returns:
            int: The maximum number of visible data points on the X-axis.
        """
        return self.__master.get_x_axis_visible_point_count()    
    
    def reset(self) -> None:
        """
        Reset the line.
        """
        self.__reset_positions()
        self.__reset_data()
        self.__master._LineChart__apply_line_configuration()

    def set_visible(self, state: bool) -> None:
        """
        Set the visibility of the line.

        Args:
            state (bool): True if the line should be visible, False otherwise.
            
        Raises:
            TypeError: If the state is not a boolean.
        """
        Validate._is_bool(state, "state")
        if self.__visibility != state:
            self.__visibility = state
            self.__master._LineChart__apply_line_configuration()

    def cget(
            self,
            attribute_name: Literal[
                "master", "color", "size", "style", "style_type", "point_highlight",
                "point_highlight_size", "point_highlight_color", "fill", "fill_color",
                "__all__"
            ] = "__all__"
    ) -> Any:
        """
        Get the value of a Line attribute.

        Args:
            attribute_name (str): Name of the attribute.

        Returns:
            Any: Value of the attribute.
            
        Raises:
            ValueError: If the attribute name is invalid.
        """
        if attribute_name == "master":
            return self.__master
        elif attribute_name == "color":
            return self.__color
        elif attribute_name == "size":
            return self.__size
        elif attribute_name == "style":
            return self.__style
        elif attribute_name == "style_type":
            return self.__style_type
        elif attribute_name == "point_highlight":
            return self.__point_highlight
        elif attribute_name == "point_highlight_size":
            return self.__point_highlight_size
        elif attribute_name == "point_highlight_color":
            return self.__point_highlight_color
        elif attribute_name == "fill":
            return self.__fill
        elif attribute_name == "fill_color":
            return self.__fill_color
        elif attribute_name == "__all__":
            return {
                "master": self.__master,
                "color": self.__color,
                "size": self.__size,
                "style": self.__style,
                "style_type": self.__style_type,
                "point_highlight": self.__point_highlight,
                "point_highlight_size": self.__point_highlight_size,
                "point_highlight_color": self.__point_highlight_color,
                "fill": self.__fill,
                "fill_color": self.__fill_color
            }
        else:
            Validate._invalid_cget(attribute_name)

    def get_visibility(self) -> bool:
        """
        Get the visibility of the line.

        Returns:
            bool: True if the line is visible, False otherwise.
        """
        return self.__visibility

    def __del__(self) -> None:
        """Destructor method to delete instance attributes."""
        del self.__id
        del self.__master
        del self.__color
        del self.__size
        del self.__y_end
        del self.__x_end
        del self.__data
        del self.__temp_data
        del self.__ret_data
        del self.__visibility
        del self.__style
        del self.__style_type
        del self.__point_highlight
        del self.__point_highlight_size
        del self.__point_highlight_color
        del self.__fill
        del self.__fill_color

    def destroy(self) -> None:
        """
        Removes the instance from its master's line chart and 
        applies the updated line configuration. Calls the destructor 
        to clean up resources.
        """
        try:
            self.__master._LineChart__lines.remove(self)
            self.__master._LineChart__apply_line_configuration()
        except ValueError:
            pass  # In case the line is not in the list
        finally:
            self.__del__()

    # -------------------------------------------------------------------------
    # Individual configure_* methods
    # Each method configures exactly one attribute by delegating to configure().
    # The existing configure() method is NOT modified.
    # -------------------------------------------------------------------------

    def configure_color(self, color: str) -> None:
        """Configure the color of the line.

        Args:
            color (str): A valid Tkinter/hex color string (e.g. ``"#ff0000"``).

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(color=color)

    def configure_size(self, size: int) -> None:
        """Configure the thickness of the line in pixels.

        Args:
            size (int): Line thickness in pixels (e.g. 1, 2, 4).

        Raises:
            TypeError: If size is not an integer.
        """
        self.configure(size=size)

    def configure_style(self, style: "Literal['normal', 'dashed', 'dotted']") -> None:
        """Configure the drawing style of the line.

        Args:
            style (str): One of ``"normal"``, ``"dashed"``, or ``"dotted"``.

        Raises:
            ValueError: If the value is not one of the accepted styles.
        """
        self.configure(style=style)

    def configure_style_type(self, style_type: "Tuple[int, int]") -> None:
        """Configure the dash/dot size and gap for dashed or dotted lines.

        Args:
            style_type (Tuple[int, int]): A tuple of ``(segment_size, gap_size)``
                in pixels. Applies only when ``style`` is ``"dashed"`` or ``"dotted"``.

        Raises:
            TypeError: If the tuple does not match the expected format.
        """
        self.configure(style_type=style_type)

    def configure_point_highlight(self, point_highlight: "Literal['enabled', 'disabled']") -> None:
        """Configure whether data-point highlight circles are drawn.

        Args:
            point_highlight (str): Either ``"enabled"`` or ``"disabled"``.

        Raises:
            ValueError: If the value is not ``"enabled"`` or ``"disabled"``.
        """
        self.configure(point_highlight=point_highlight)

    def configure_point_highlight_size(self, point_highlight_size: int) -> None:
        """Configure the diameter of the point highlight circles.

        Args:
            point_highlight_size (int): Diameter in pixels.

        Raises:
            TypeError: If point_highlight_size is not an integer.
        """
        self.configure(point_highlight_size=point_highlight_size)

    def configure_point_highlight_color(self, point_highlight_color: str) -> None:
        """Configure the fill color of the point highlight circles.

        Args:
            point_highlight_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(point_highlight_color=point_highlight_color)

    def configure_fill(self, fill: "Literal['enabled', 'disabled']") -> None:
        """Configure whether the area below the line is filled.

        Args:
            fill (str): Either ``"enabled"`` or ``"disabled"``.

        Raises:
            ValueError: If the value is not ``"enabled"`` or ``"disabled"``.
        """
        self.configure(fill=fill)

    def configure_fill_color(self, fill_color: str) -> None:
        """Configure the fill color of the area below the line.

        Args:
            fill_color (str): A valid Tkinter/hex color string.

        Raises:
            ValueError: If the color string is not a valid color.
        """
        self.configure(fill_color=fill_color)