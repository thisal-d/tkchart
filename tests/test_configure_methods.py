# -*- coding: utf-8 -*-
"""
test_configure_functions.py
============================
Interactive test file for all individual configure_* methods on LineChart.

How to run
----------
    python test_configure_functions.py

Layout
------
- Left panel  : scrollable list of buttons grouped by category.
- Right panel : the live LineChart widget.

Each button calls the corresponding configure_* method with a preset value.
"""

import sys
import os
import tkinter as tk
import threading
import random

# ---------------------------------------------------------------------------
# Make sure the local src/ is importable when running from the project root
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from tkchart import LineChart, Line  # noqa: E402

# ---------------------------------------------------------------------------
# Color palette
# ---------------------------------------------------------------------------
BG_DARK   = "#0f1117"
BG_PANEL  = "#1a1d27"
BTN_BG    = "#2c2f4a"
BTN_HOVER = "#3d4170"
BTN_ACT   = "#5865f2"
SEP_COLOR = "#2e3155"
TEXT_MAIN = "#e0e0f0"
TEXT_DIM  = "#8888aa"
ACCENT2   = "#57f287"
ACCENT    = "#5865f2"

FONT_TITLE = ("Segoe UI", 13, "bold")
FONT_CAT   = ("Segoe UI", 10, "bold")
FONT_BTN   = ("Segoe UI", 9)


# ---------------------------------------------------------------------------
# Flat button widget
# ---------------------------------------------------------------------------
class FlatButton(tk.Frame):
    def __init__(self, master, text, command, width=340, **kw):
        super().__init__(master, bg=BTN_BG, cursor="hand2",
                         highlightthickness=1, highlightbackground=SEP_COLOR)
        self._cmd = command
        self._lbl = tk.Label(
            self, text=text, font=FONT_BTN,
            bg=BTN_BG, fg=TEXT_MAIN,
            padx=8, pady=4, anchor="w"
        )
        self._lbl.pack(fill="x")
        for w in (self, self._lbl):
            w.bind("<Enter>",    self._on_enter)
            w.bind("<Leave>",    self._on_leave)
            w.bind("<Button-1>", self._on_click)

    def _on_enter(self, _):
        self.config(bg=BTN_HOVER, highlightbackground=ACCENT)
        self._lbl.config(bg=BTN_HOVER)

    def _on_leave(self, _):
        self.config(bg=BTN_BG, highlightbackground=SEP_COLOR)
        self._lbl.config(bg=BTN_BG)

    def _on_click(self, _):
        self.config(bg=BTN_ACT)
        self._lbl.config(bg=BTN_ACT)
        self.after(150, self._on_leave, None)
        self._cmd()


# ---------------------------------------------------------------------------
# Scrollable frame
# ---------------------------------------------------------------------------
class ScrollableFrame(tk.Frame):
    def __init__(self, master, **kw):
        container = tk.Frame(master, bg=BG_PANEL)
        container.pack(fill="both", expand=True)

        self._canvas = tk.Canvas(container, bg=BG_PANEL, highlightthickness=0)
        vsb = tk.Scrollbar(container, orient="vertical",
                           command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        super().__init__(self._canvas, bg=BG_PANEL, **kw)
        self._window = self._canvas.create_window((0, 0), window=self, anchor="nw")

        self.bind("<Configure>", self._on_frame_configure)
        self._canvas.bind("<Configure>", self._on_canvas_configure)
        self._canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_frame_configure(self, _):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _on_canvas_configure(self, e):
        self._canvas.itemconfig(self._window, width=e.width)

    def _on_mousewheel(self, e):
        self._canvas.yview_scroll(-1 * (e.delta // 120), "units")


# ---------------------------------------------------------------------------
# Main application
# ---------------------------------------------------------------------------
class TestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LineChart  configure_*  Test Suite")
        self.geometry("1280x750")
        self.configure(bg=BG_DARK)
        self.resizable(True, True)

        self._build_header()
        self._build_body()
        self._build_chart()
        self._build_lines()
        self._build_controls()
        self._start_data_loop()   # starts the live data thread last

    # ------------------------------------------------------------------ Header
    def _build_header(self):
        hdr = tk.Frame(self, bg=BG_PANEL, height=52)
        hdr.pack(fill="x", side="top")
        hdr.pack_propagate(False)
        tk.Label(
            hdr, text="LineChart  configure_*  Test Suite",
            font=FONT_TITLE, bg=BG_PANEL, fg=TEXT_MAIN
        ).pack(side="left", padx=20, pady=12)
        tk.Label(
            hdr, text="Click any button to apply the configuration live ->",
            font=("Segoe UI", 9), bg=BG_PANEL, fg=TEXT_DIM
        ).pack(side="right", padx=20)
        tk.Frame(self, bg=SEP_COLOR, height=1).pack(fill="x")

    # ------------------------------------------------------------------ Body
    def _build_body(self):
        body = tk.Frame(self, bg=BG_DARK)
        body.pack(fill="both", expand=True)

        # Left – scrollable buttons
        left = tk.Frame(body, bg=BG_PANEL, width=430)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)
        self._scroll = ScrollableFrame(left)
        # The ScrollableFrame already packs itself via container

        # Right – chart area
        self._right = tk.Frame(body, bg=BG_DARK)
        self._right.pack(side="left", fill="both", expand=True)

        # Status bar
        self._status_var = tk.StringVar(value="Ready")
        tk.Label(
            self._right, textvariable=self._status_var,
            font=("Segoe UI", 9), bg=BG_DARK, fg=ACCENT2,
            anchor="w"
        ).pack(side="bottom", fill="x", padx=20, pady=4)

    # ------------------------------------------------------------------ Chart
    def _build_chart(self):
        self._x_vals = tuple("T{}".format(i) for i in range(1, 21))

        self._chart = LineChart(
            master=self._right,
            width=800,
            height=430,
            axis_size=2,
            bg_color="#191919",
            fg_color="#191919",
            axis_color="#3a3a5c",
            data_font_style=("Segoe UI", 9, "bold"),
            axis_font_style=("Segoe UI", 8, "normal"),
            y_axis_values=(0, 100),
            y_axis_label_count=5,
            y_axis_section_count=5,
            y_axis_section_color="#2a2a4a",
            y_axis_font_color="#8888aa",
            y_axis_data_font_color="#aaaacc",
            y_axis_data="Y",
            x_axis_values=self._x_vals,
            x_axis_label_count=10,
            x_axis_section_count=5,
            x_axis_section_color="#2a2a4a",
            x_axis_font_color="#8888aa",
            x_axis_data_font_color="#aaaacc",
            x_axis_data="Time",
            x_axis_point_spacing="auto",
            pointer_state="enabled",
            pointer_color="#5865f2",
            pointer_size=2,
        )
        self._chart.pack(pady=20, padx=20)

    # ------------------------------------------------------------------ Lines
    def _build_lines(self):
        # Line(master=chart, ...) automatically registers itself in chart.__lines
        self._line1 = Line(
            master=self._chart,
            color="#5865f2",
            size=2,
            style="normal",
            point_highlight="enabled",
            point_highlight_color="#5865f2",
            point_highlight_size=6,
            fill="enabled",
            fill_color="#1e2140",
        )
        self._line2 = Line(
            master=self._chart,
            color="#57f287",
            size=2,
            style="normal",
            point_highlight="enabled",
            point_highlight_color="#57f287",
            point_highlight_size=6,
        )

    # ------------------------------------------------------------------ Live data loop
    def _start_data_loop(self):
        """Spawn a daemon thread that pushes one data point to each line every second.
        The thread itself never touches tkinter; it schedules updates via after()."""
        self._running = True

        def _loop():
            while self._running:
                # Schedule the actual chart update on the main (tkinter) thread
                self.after(0, self._push_data_point)
                threading.Event().wait(1.0)   # sleep 1 second without blocking Tk

        t = threading.Thread(target=_loop, daemon=True)
        t.start()

        # Stop the thread cleanly when the window is closed
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _push_data_point(self):
        """Called on the main thread every second to add one new value to each line."""
        try:
            self._chart.show_data(line=self._line1, data=[random.randint(20, 90)])
            self._chart.show_data(line=self._line2, data=[random.randint(10, 80)])
        except Exception:
            pass   # chart may have been destroyed

    def _on_close(self):
        self._running = False
        self.destroy()

    # ------------------------------------------------------------------ Status
    def _set_status(self, msg):
        self._status_var.set("Applied:  " + msg)

    # ================================================================== All Controls
    def _build_controls(self):
        p = self._scroll  # parent for all buttons

        # ---- Width ----
        self._section(p, "Width")
        for v in (400, 500, 600, 700, 800):
            self._btn(p, "width = {}".format(v), lambda val=v: (
                self._chart.configure_width(val),
                self._set_status("configure_width({})".format(val))
            ))

        # ---- Height ----
        self._section(p, "Height")
        for v in (280, 340, 430, 500, 560):
            self._btn(p, "height = {}".format(v), lambda val=v: (
                self._chart.configure_height(val),
                self._set_status("configure_height({})".format(val))
            ))

        # ---- Axis Size ----
        self._section(p, "Axis Size")
        for v in (1, 2, 4, 6):
            self._btn(p, "axis_size = {}".format(v), lambda val=v: (
                self._chart.configure_axis_size(val),
                self._set_status("configure_axis_size({})".format(val))
            ))

        # ---- X Axis Point Spacing ----
        self._section(p, "X Axis Point Spacing")
        for v in ("auto", 20, 35, 50, 70):
            self._btn(p, "x_axis_point_spacing = {!r}".format(v), lambda val=v: (
                self._chart.configure_x_axis_point_spacing(val),
                self._set_status("configure_x_axis_point_spacing({!r})".format(val))
            ))

        # ---- bg_color ----
        self._section(p, "Background Color  (bg_color)")
        for v in ("#191919", "#0d0d1a", "#1a1a2e", "#0f1117", "#2c1810"):
            self._btn(p, "bg_color = {}".format(v), lambda val=v: (
                self._chart.configure_bg_color(val),
                self._set_status("configure_bg_color('{}')".format(val))
            ), swatch=v)

        # ---- axis_color ----
        self._section(p, "Axis Color  (axis_color)")
        for v in ("#3a3a5c", "#5865f2", "#ff4444", "#44ff88", "#aaaaaa"):
            self._btn(p, "axis_color = {}".format(v), lambda val=v: (
                self._chart.configure_axis_color(val),
                self._set_status("configure_axis_color('{}')".format(val))
            ), swatch=v)

        # ---- fg_color ----
        self._section(p, "Foreground Color  (fg_color)")
        for v in ("#191919", "#101020", "#1e1e2e", "#0a0a15"):
            self._btn(p, "fg_color = {}".format(v), lambda val=v: (
                self._chart.configure_fg_color(val),
                self._set_status("configure_fg_color('{}')".format(val))
            ), swatch=v)

        # ---- data_font_style ----
        self._section(p, "Data Font Style")
        fonts_data = [
            ("Segoe UI", 9, "bold"),
            ("Arial", 10, "bold"),
            ("Courier New", 9, "normal"),
            ("Consolas", 10, "bold"),
        ]
        for v in fonts_data:
            self._btn(p, str(v), lambda val=v: (
                self._chart.configure_data_font_style(val),
                self._set_status("configure_data_font_style({})".format(val))
            ))

        # ---- axis_font_style ----
        self._section(p, "Axis Font Style")
        fonts_axis = [
            ("Segoe UI", 8, "normal"),
            ("Arial", 9, "bold"),
            ("Consolas", 8, "normal"),
            ("Courier New", 10, "normal"),
        ]
        for v in fonts_axis:
            self._btn(p, str(v), lambda val=v: (
                self._chart.configure_axis_font_style(val),
                self._set_status("configure_axis_font_style({})".format(val))
            ))

        # ---- y_axis_values ----
        self._section(p, "Y Axis Values  (min, max)")
        for v in ((0, 100), (-50, 50), (0, 200), (10, 80), (0, 1000)):
            self._btn(p, "y_axis_values = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_values(val),
                self._set_status("configure_y_axis_values({})".format(val))
            ))

        # ---- y_axis_precision ----
        self._section(p, "Y Axis Precision")
        for v in (0, 1, 2, 3):
            self._btn(p, "y_axis_precision = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_precision(val),
                self._set_status("configure_y_axis_precision({})".format(val))
            ))

        # ---- y_axis_font_color ----
        self._section(p, "Y Axis Font Color")
        for v in ("#8888aa", "#ffffff", "#5865f2", "#57f287", "#ff9900"):
            self._btn(p, "y_axis_font_color = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_font_color(val),
                self._set_status("configure_y_axis_font_color('{}')".format(val))
            ), swatch=v)

        # ---- y_axis_data_font_color ----
        self._section(p, "Y Axis Data Font Color")
        for v in ("#aaaacc", "#ffffff", "#5865f2", "#57f287"):
            self._btn(p, "y_axis_data_font_color = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_data_font_color(val),
                self._set_status("configure_y_axis_data_font_color('{}')".format(val))
            ), swatch=v)

        # ---- y_axis_label_count ----
        self._section(p, "Y Axis Label Count")
        for v in (0, 3, 5, 8, 10):
            self._btn(p, "y_axis_label_count = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_label_count(val),
                self._set_status("configure_y_axis_label_count({})".format(val))
            ))

        # ---- y_axis_data ----
        self._section(p, "Y Axis Data Title  (y_axis_data)")
        for v in ("Y", "Value", "Score", "Temp", ""):
            self._btn(p, "y_axis_data = {!r}".format(v), lambda val=v: (
                self._chart.configure_y_axis_data(val),
                self._set_status("configure_y_axis_data({!r})".format(val))
            ))

        # ---- y_axis_data_position ----
        self._section(p, "Y Axis Data Position")
        for v in ("top", "side"):
            self._btn(p, "y_axis_data_position = {!r}".format(v), lambda val=v: (
                self._chart.configure_y_axis_data_position(val),
                self._set_status("configure_y_axis_data_position({!r})".format(val))
            ))

        # ---- y_axis_section_count ----
        self._section(p, "Y Axis Section Count")
        for v in (0, 3, 5, 8):
            self._btn(p, "y_axis_section_count = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_section_count(val),
                self._set_status("configure_y_axis_section_count({})".format(val))
            ))

        # ---- y_axis_section_color ----
        self._section(p, "Y Axis Section Color")
        for v in ("#2a2a4a", "#3d4170", "#444444", "#1e3a1e"):
            self._btn(p, "y_axis_section_color = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_section_color(val),
                self._set_status("configure_y_axis_section_color('{}')".format(val))
            ), swatch=v)

        # ---- y_axis_section_style ----
        self._section(p, "Y Axis Section Style")
        for v in ("normal", "dashed"):
            self._btn(p, "y_axis_section_style = {!r}".format(v), lambda val=v: (
                self._chart.configure_y_axis_section_style(val),
                self._set_status("configure_y_axis_section_style({!r})".format(val))
            ))

        # ---- y_axis_section_style_type ----
        self._section(p, "Y Axis Section Style Type  (dash, gap)")
        for v in ((100, 50), (60, 30), (20, 10), (10, 5)):
            self._btn(p, "y_axis_section_style_type = {}".format(v), lambda val=v: (
                self._chart.configure_y_axis_section_style_type(val),
                self._set_status("configure_y_axis_section_style_type({})".format(val))
            ))

        # ---- y_space ----
        self._section(p, "Y Space")
        for v in (0, 10, 20, 40):
            self._btn(p, "y_space = {}".format(v), lambda val=v: (
                self._chart.configure_y_space(val),
                self._set_status("configure_y_space({})".format(val))
            ))

        # ---- x_axis_data ----
        self._section(p, "X Axis Data Title  (x_axis_data)")
        for v in ("Time", "Date", "Index", "Step", ""):
            self._btn(p, "x_axis_data = {!r}".format(v), lambda val=v: (
                self._chart.configure_x_axis_data(val),
                self._set_status("configure_x_axis_data({!r})".format(val))
            ))

        # ---- x_axis_data_position ----
        self._section(p, "X Axis Data Position")
        for v in ("top", "side"):
            self._btn(p, "x_axis_data_position = {!r}".format(v), lambda val=v: (
                self._chart.configure_x_axis_data_position(val),
                self._set_status("configure_x_axis_data_position({!r})".format(val))
            ))

        # ---- x_axis_font_color ----
        self._section(p, "X Axis Font Color")
        for v in ("#8888aa", "#ffffff", "#5865f2", "#57f287", "#ff9900"):
            self._btn(p, "x_axis_font_color = {}".format(v), lambda val=v: (
                self._chart.configure_x_axis_font_color(val),
                self._set_status("configure_x_axis_font_color('{}')".format(val))
            ), swatch=v)

        # ---- x_axis_data_font_color ----
        self._section(p, "X Axis Data Font Color")
        for v in ("#aaaacc", "#ffffff", "#5865f2", "#57f287"):
            self._btn(p, "x_axis_data_font_color = {}".format(v), lambda val=v: (
                self._chart.configure_x_axis_data_font_color(val),
                self._set_status("configure_x_axis_data_font_color('{}')".format(val))
            ), swatch=v)

        # ---- x_axis_label_count ----
        self._section(p, "X Axis Label Count")
        for v in (0, 5, 10, 15, 20):
            self._btn(p, "x_axis_label_count = {}".format(v), lambda val=v: (
                self._chart.configure_x_axis_label_count(val),
                self._set_status("configure_x_axis_label_count({})".format(val))
            ))

        # ---- x_axis_section_count ----
        self._section(p, "X Axis Section Count")
        for v in (0, 3, 5, 8):
            self._btn(p, "x_axis_section_count = {}".format(v), lambda val=v: (
                self._chart.configure_x_axis_section_count(val),
                self._set_status("configure_x_axis_section_count({})".format(val))
            ))

        # ---- x_axis_section_color ----
        self._section(p, "X Axis Section Color")
        for v in ("#2a2a4a", "#3d4170", "#444444", "#3a1e1e"):
            self._btn(p, "x_axis_section_color = {}".format(v), lambda val=v: (
                self._chart.configure_x_axis_section_color(val),
                self._set_status("configure_x_axis_section_color('{}')".format(val))
            ), swatch=v)

        # ---- x_axis_section_style ----
        self._section(p, "X Axis Section Style")
        for v in ("normal", "dashed"):
            self._btn(p, "x_axis_section_style = {!r}".format(v), lambda val=v: (
                self._chart.configure_x_axis_section_style(val),
                self._set_status("configure_x_axis_section_style({!r})".format(val))
            ))

        # ---- x_axis_section_style_type ----
        self._section(p, "X Axis Section Style Type  (dash, gap)")
        for v in ((100, 50), (60, 30), (20, 10), (10, 5)):
            self._btn(p, "x_axis_section_style_type = {}".format(v), lambda val=v: (
                self._chart.configure_x_axis_section_style_type(val),
                self._set_status("configure_x_axis_section_style_type({})".format(val))
            ))

        # ---- x_space ----
        self._section(p, "X Space")
        for v in (0, 10, 20, 40):
            self._btn(p, "x_space = {}".format(v), lambda val=v: (
                self._chart.configure_x_space(val),
                self._set_status("configure_x_space({})".format(val))
            ))

        # ---- pointer_state ----
        self._section(p, "Pointer State")
        for v in ("enabled", "disabled"):
            self._btn(p, "pointer_state = {!r}".format(v), lambda val=v: (
                self._chart.configure_pointer_state(val),
                self._set_status("configure_pointer_state({!r})".format(val))
            ))

        # ---- pointer_color ----
        self._section(p, "Pointer Color")
        for v in ("#5865f2", "#ff4444", "#57f287", "#ffffff", "#ff9900"):
            self._btn(p, "pointer_color = {}".format(v), lambda val=v: (
                self._chart.configure_pointer_color(val),
                self._set_status("configure_pointer_color('{}')".format(val))
            ), swatch=v)

        # ---- pointer_size ----
        self._section(p, "Pointer Size")
        for v in (1, 2, 3, 5, 8):
            self._btn(p, "pointer_size = {}".format(v), lambda val=v: (
                self._chart.configure_pointer_size(val),
                self._set_status("configure_pointer_size({})".format(val))
            ))

        # ---- pointer_lock ----
        self._section(p, "Pointer Lock")
        for v in ("enabled", "disabled"):
            self._btn(p, "pointer_lock = {!r}".format(v), lambda val=v: (
                self._chart.configure_pointer_lock(val),
                self._set_status("configure_pointer_lock({!r})".format(val))
            ))

        # ---- pointing_values_precision ----
        self._section(p, "Pointing Values Precision")
        for v in (0, 1, 2, 3):
            self._btn(p, "pointing_values_precision = {}".format(v), lambda val=v: (
                self._chart.configure_pointing_values_precision(val),
                self._set_status("configure_pointing_values_precision({})".format(val))
            ))

        # ---- pointing_callback_function ----
        self._section(p, "Pointing Callback Function")

        def _cb_noop(x, vals):
            pass

        def _cb_print(x, vals):
            print("[Pointer Callback]  x={}  values={}".format(x, vals))

        for label, fn in [("None / no-op callback", _cb_noop),
                          ("print to console", _cb_print)]:
            self._btn(p, label, lambda f=fn, l=label: (
                self._chart.configure_pointing_callback_function(f),
                self._set_status("configure_pointing_callback_function  ->  " + l)
            ))

        # ======================================================================
        # LINE configure_* methods
        # Apply to self._line1 (blue, with fill) and self._line2 (green)
        # ======================================================================
        tk.Frame(p, bg="#5865f2", height=2).pack(fill="x", pady=(16, 0), padx=0)
        tk.Label(
            p, text="  LINE  configure_*  (line1 = blue   |   line2 = green)",
            font=("Segoe UI", 10, "bold"), bg="#20243a", fg="#e0e0f0",
            anchor="w", pady=6
        ).pack(fill="x")
        tk.Frame(p, bg="#5865f2", height=2).pack(fill="x", pady=(0, 4), padx=0)

        # ---- Line color ----
        self._section(p, "Line  color")
        colors_line = [
            ("#5865f2", "blue  (default line1)"),
            ("#57f287", "green (default line2)"),
            ("#ff4444", "red"),
            ("#ff9900", "orange"),
            ("#ffffff", "white"),
        ]
        for c, label in colors_line:
            self._btn(
                p, "line1.configure_color('{}')  {}".format(c, label),
                lambda val=c: (
                    self._line1.configure_color(val),
                    self._set_status("line1.configure_color('{}')".format(val))
                ), swatch=c
            )
        for c, label in colors_line:
            self._btn(
                p, "line2.configure_color('{}')  {}".format(c, label),
                lambda val=c: (
                    self._line2.configure_color(val),
                    self._set_status("line2.configure_color('{}')".format(val))
                ), swatch=c
            )

        # ---- Line size ----
        self._section(p, "Line  size  (thickness)")
        for v in (1, 2, 3, 5, 8):
            self._btn(p, "line1.configure_size({})".format(v), lambda val=v: (
                self._line1.configure_size(val),
                self._set_status("line1.configure_size({})".format(val))
            ))
        for v in (1, 2, 3, 5, 8):
            self._btn(p, "line2.configure_size({})".format(v), lambda val=v: (
                self._line2.configure_size(val),
                self._set_status("line2.configure_size({})".format(val))
            ))

        # ---- Line style ----
        self._section(p, "Line  style")
        for st in ("normal", "dashed", "dotted"):
            self._btn(p, "line1.configure_style({!r})".format(st), lambda val=st: (
                self._line1.configure_style(val),
                self._set_status("line1.configure_style({!r})".format(val))
            ))
        for st in ("normal", "dashed", "dotted"):
            self._btn(p, "line2.configure_style({!r})".format(st), lambda val=st: (
                self._line2.configure_style(val),
                self._set_status("line2.configure_style({!r})".format(val))
            ))

        # ---- Line style_type ----
        self._section(p, "Line  style_type  (segment, gap)  — for dashed/dotted")
        for v in ((4, 4), (8, 4), (12, 6), (2, 8), (20, 5)):
            self._btn(p, "line1.configure_style_type({})".format(v), lambda val=v: (
                self._line1.configure_style_type(val),
                self._set_status("line1.configure_style_type({})".format(val))
            ))
        for v in ((4, 4), (8, 4), (12, 6), (2, 8), (20, 5)):
            self._btn(p, "line2.configure_style_type({})".format(v), lambda val=v: (
                self._line2.configure_style_type(val),
                self._set_status("line2.configure_style_type({})".format(val))
            ))

        # ---- point_highlight ----
        self._section(p, "Line  point_highlight")
        for st in ("enabled", "disabled"):
            self._btn(p, "line1.configure_point_highlight({!r})".format(st), lambda val=st: (
                self._line1.configure_point_highlight(val),
                self._set_status("line1.configure_point_highlight({!r})".format(val))
            ))
        for st in ("enabled", "disabled"):
            self._btn(p, "line2.configure_point_highlight({!r})".format(st), lambda val=st: (
                self._line2.configure_point_highlight(val),
                self._set_status("line2.configure_point_highlight({!r})".format(val))
            ))

        # ---- point_highlight_size ----
        self._section(p, "Line  point_highlight_size")
        for v in (2, 4, 6, 10, 16):
            self._btn(p, "line1.configure_point_highlight_size({})".format(v), lambda val=v: (
                self._line1.configure_point_highlight_size(val),
                self._set_status("line1.configure_point_highlight_size({})".format(val))
            ))
        for v in (2, 4, 6, 10, 16):
            self._btn(p, "line2.configure_point_highlight_size({})".format(v), lambda val=v: (
                self._line2.configure_point_highlight_size(val),
                self._set_status("line2.configure_point_highlight_size({})".format(val))
            ))

        # ---- point_highlight_color ----
        self._section(p, "Line  point_highlight_color")
        hl_colors = [("#5865f2", "blue"), ("#57f287", "green"),
                     ("#ff4444", "red"), ("#ff9900", "orange"), ("#ffffff", "white")]
        for c, lbl in hl_colors:
            self._btn(
                p, "line1.configure_point_highlight_color('{}')  {}".format(c, lbl),
                lambda val=c: (
                    self._line1.configure_point_highlight_color(val),
                    self._set_status("line1.configure_point_highlight_color('{}')".format(val))
                ), swatch=c
            )
        for c, lbl in hl_colors:
            self._btn(
                p, "line2.configure_point_highlight_color('{}')  {}".format(c, lbl),
                lambda val=c: (
                    self._line2.configure_point_highlight_color(val),
                    self._set_status("line2.configure_point_highlight_color('{}')".format(val))
                ), swatch=c
            )

        # ---- fill ----
        self._section(p, "Line  fill")
        for st in ("enabled", "disabled"):
            self._btn(p, "line1.configure_fill({!r})".format(st), lambda val=st: (
                self._line1.configure_fill(val),
                self._set_status("line1.configure_fill({!r})".format(val))
            ))
        for st in ("enabled", "disabled"):
            self._btn(p, "line2.configure_fill({!r})".format(st), lambda val=st: (
                self._line2.configure_fill(val),
                self._set_status("line2.configure_fill({!r})".format(val))
            ))

        # ---- fill_color ----
        self._section(p, "Line  fill_color")
        fill_colors = [
            ("#1e2140", "dark blue"),
            ("#1e3a1e", "dark green"),
            ("#3a1e1e", "dark red"),
            ("#2a2010", "dark orange"),
            ("#252525", "dark grey"),
        ]
        for c, lbl in fill_colors:
            self._btn(
                p, "line1.configure_fill_color('{}')  {}".format(c, lbl),
                lambda val=c: (
                    self._line1.configure_fill_color(val),
                    self._set_status("line1.configure_fill_color('{}')".format(val))
                ), swatch=c
            )
        for c, lbl in fill_colors:
            self._btn(
                p, "line2.configure_fill_color('{}')  {}".format(c, lbl),
                lambda val=c: (
                    self._line2.configure_fill_color(val),
                    self._set_status("line2.configure_fill_color('{}')".format(val))
                ), swatch=c
            )

        # Bottom spacer
        tk.Frame(p, bg=BG_PANEL, height=40).pack(fill="x")

    # ================================================================== Helpers
    def _section(self, parent, title):
        """Section separator + title label."""
        tk.Frame(parent, bg=SEP_COLOR, height=1).pack(fill="x", pady=(10, 0), padx=6)
        tk.Label(
            parent, text="   " + title,
            font=FONT_CAT, bg=BG_PANEL, fg=TEXT_DIM,
            anchor="w"
        ).pack(fill="x", pady=(3, 1))

    def _btn(self, parent, text, cmd, swatch=None):
        """Button row, optionally with a color swatch."""
        row = tk.Frame(parent, bg=BG_PANEL)
        row.pack(fill="x", padx=8, pady=2)

        if swatch:
            tk.Frame(row, bg=swatch, width=14, height=14).pack(
                side="left", padx=(2, 6), pady=4)

        FlatButton(row, text=text, command=cmd).pack(side="left", fill="x")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
