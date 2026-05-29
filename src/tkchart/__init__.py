"""
tkchart: A library to create live-update charts for Tkinter GUIs.
"""

from .LineChart import LineChart
from .Line import Line

# Constants for common string values
ENABLED = "enabled"
DISABLED = "disabled"

NORMAL = "normal"
DASHED = "dashed"
DOTTED = "dotted"

TOP = "top"
SIDE = "side"

AUTO = "auto"

__title__ = "tkchart"
__version__ = "2.2.0"
__authors__ = ("Thisal Dilmith", "childeyouyu (有语)")

__all__ = [
    "LineChart",
    "Line",
    "ENABLED",
    "DISABLED",
    "NORMAL",
    "DASHED",
    "DOTTED",
    "TOP",
    "SIDE",
    "AUTO",
]
