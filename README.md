# pyqt-dark-theme
A Python package that provides a dark theme for PyQt5 and PySide2 applications, as well as a dark theme for Matplotlib plots.

## Usage
The theme.py file contains the following functions:

```python
setTheme(app, theme='default')
```
This function sets the theme of a `PyQt5` or `PySide2` application to either a dark theme or the default theme, depending on the value of the `theme` argument. The `app` argument is the `QApplication` object that represents the application.

```python
setMatplotlibDarkTheme()
```
This function sets the theme of Matplotlib plots to a dark theme.

## Files
The repository contains the following files:

- `dark_theme.css`: A CSS file that contains styles for the dark theme.

- `theme.py`: A Python file that contains the `setTheme` and `setMatplotlibDarkTheme` functions.

- `icons/drop-down.svg`: An SVG file that contains an icon for the drop-down menu that used by `dark_theme.css`.