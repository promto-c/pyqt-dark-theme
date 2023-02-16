# pyqt-dark-theme
A Python package that provides a dark theme for PyQt5 and PySide2 applications, as well as a dark theme for Matplotlib plots.

---
## Usage
The theme.py file contains the following functions:

```python
set_theme(app, theme='default')
```
This function sets the theme of a `PyQt5` or `PySide2` application to either a dark theme or the default theme, depending on the value of the `theme` argument. The `app` argument is the `QApplication` object that represents the application.

```python
set_matplotlib_dark_theme()
```
This function sets the theme of Matplotlib plots to a dark theme.

---
## Example usage

### For PyQt5:
```python
import sys
from PyQt5 import QtWidgets
from theme import set_theme

app = QtWidgets.QApplication(sys.argv)

# Set theme of QApplication to the dark theme
set_theme(app, theme='dark')

# Your PyQt5 application code here

sys.exit(app.exec_())
```

### For PySide2:
```python
import sys
from PySide2 import QtWidgets
from theme import set_theme

app = QtWidgets.QApplication(sys.argv)

# Set theme of QApplication to the dark theme
set_theme(app, theme='dark')

# Your PySide2 application code here

sys.exit(app.exec_())
```

---
## Files
The repository contains the following files:

- `dark_theme.css`: A CSS file that contains styles for the dark theme.

- `theme.py`: A Python file that contains the `set_theme` and `set_matplotlib_dark_theme` functions.

- `icons/drop-down.svg`: An SVG file that contains an icon for the drop-down menu that used by `dark_theme.css`.