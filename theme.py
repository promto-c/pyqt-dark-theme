# Standard Library Imports
# ------------------------
import re
from pathlib import Path


# Constants Definition
# --------------------
PACKAGE_ROOT = Path(__file__).parent

ICON_DIRECTORY = 'icons'
ABS_ICON_PATH = (PACKAGE_ROOT / ICON_DIRECTORY).as_posix()


# Function Definitions
# --------------------
def invert_color(color: str) -> str:
    """Inverts a given RGB or RGBA color string.

    Args:
        color (str): A string representing the color in RGB or RGBA format.

    Returns:
        str: The inverted color string in RGB or RGBA format.

    Note:
        - RGB format is 'rgb(r, g, b)'.
        - RGBA format is 'rgba(r, g, b, a)'.
    """
    parts = [int(c) for c in color.split(',')]

    # Handle RGB format
    if len(parts) == 3:
        r, g, b = [255 - c for c in parts]
        return f'rgb({r}, {g}, {b})'

    # Handle RGBA format
    elif len(parts) == 4:
        r, g, b, a = [255 - c if i < 3 else c for i, c in enumerate(parts)]
        return f'rgba({r}, {g}, {b}, {a})'

def invert_style_sheet(css: str) -> str:
    """Processes a CSS string and inverts its RGB and RGBA color values.

    Args:
        css (str): The CSS stylesheet as a string.

    Returns:
        str: The CSS stylesheet with inverted color values.
    """
    # Regular expressions for matching RGB and RGBA patterns
    rgb_pattern = r'rgb\((\d+), (\d+), (\d+)\)'
    rgba_pattern = r'rgba\((\d+), (\d+), (\d+), (\d+\.?\d*)\)'

    # Invert RGB and RGBA colors
    css = re.sub(rgb_pattern, lambda m: invert_color(m.group(0)[4:-1]), css)
    css = re.sub(rgba_pattern, lambda m: invert_color(m.group(0)[5:-1]), css)

    return css

def get_style_sheet(theme_name: str = 'dark') -> str:
    """Retrieves and processes a CSS stylesheet based on the specified theme.
    """
    # Construct the path to the stylesheet file
    file_path = PACKAGE_ROOT / f'{theme_name}.css'

    # Check if the stylesheet file exists
    if not file_path.exists():
        return str()

    # Read and process the stylesheet file
    with open(file_path, 'r') as file:
        style_sheet = file.read()

    # Replace placeholders in the stylesheet
    return style_sheet.replace(ICON_DIRECTORY, ABS_ICON_PATH)

def set_theme(app, theme: str = 'dark') -> None:
    """This function use to set theme for "QApplication", support for "PySide2" and "PyQt5"
    """
    # Get the name of the library that the app object belongs to
    lib_name = app.__module__.split('.')[0]
    # Import the QtGui module from the library with the name stored in lib_name
    QtGui = __import__(lib_name).QtGui

    # Check if the theme is set to 'dark'
    if theme == 'dark':
        # Set the application style to 'Fusion'
        app.setStyle('Fusion')

        # Create a palette with dark colors
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(44, 44, 44))
        palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor(246, 246, 246))
        palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(29, 29, 29))
        palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, QtGui.QColor(210, 210, 210))
        palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor(210, 218, 218))
        palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(44, 44, 44))
        palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor(210, 210, 210))
        palette.setColor(QtGui.QPalette.ColorRole.BrightText, QtGui.QColor(246, 0, 0))
        palette.setColor(QtGui.QPalette.ColorRole.Link, QtGui.QColor(42, 130, 218))
        palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor(110, 120, 125, 127))
        # Apply the dark palette to the application
        app.setPalette(palette)

        # Set theme style sheet
        app.setStyleSheet(get_style_sheet(theme))

    # Check if the theme is set to 'light'
    elif theme == 'light':
        # Set light theme specific settings
        app.setStyleSheet(invert_style_sheet(get_style_sheet('dark')))
        app.setPalette(QtGui.QPalette())

    # Else set to 'default'
    else:
        # Set to default style and palette
        app.setStyle(str())
        app.setPalette(QtGui.QPalette())

def set_matplotlib_dark_theme() -> None:
    """This function sets the theme of Matplotlib plots to a dark theme.
    """
    # Import the Matplotlib library and the Pyplot submodule
    import matplotlib
    import matplotlib.pyplot as plt

    # Set the Matplotlib style to the 'dark_background' style
    plt.style.use('dark_background')

    # Set the color of the axes edges to a dark gray color
    matplotlib.rcParams['axes.edgecolor'] = (0.4, 0.4, 0.4)
    # Set the color of the x-axis tick labels to a light gray color
    matplotlib.rcParams['xtick.color'] = (0.56, 0.56, 0.56)
    # Set the color of the y-axis tick labels to a light gray color
    matplotlib.rcParams['ytick.color'] = (0.56, 0.56, 0.56)
