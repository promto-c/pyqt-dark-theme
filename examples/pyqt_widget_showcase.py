import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from theme import set_theme

class DemoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Comprehensive Widgets Demo")
        self.setGeometry(100, 100, 1000, 800)
        self.initUI()

    def initUI(self):
        # Central Widget
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        # Tab Widget
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(self.create_form_tab(), "Form Inputs")
        tab_widget.addTab(self.create_display_tab(), "Display Widgets")
        tab_widget.addTab(self.create_container_tab(), "Container Widgets")
        tab_widget.addTab(self.create_button_group_tab(), "Button Groups")
        main_layout.addWidget(tab_widget)

        # Menu Bar
        self.initMenuBar()

        # Status Bar
        self.statusBar().showMessage("Ready")

        central_widget.setLayout(main_layout)

    def initMenuBar(self):
        menu_bar = self.menuBar()
        
        # File Menu
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction("New")
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        # Edit Menu
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        # View Menu
        view_menu = menu_bar.addMenu("&View")

        # Submenu
        submenu = view_menu.addMenu("Submenu")
        submenu.addAction("Submenu Item 1")
        submenu.addAction("Submenu Item 2")

        # Help Menu
        help_menu = menu_bar.addMenu("&Help")
        help_menu.addAction("About")

    def create_form_tab(self):
        form_widget = QtWidgets.QWidget()
        form_layout = QtWidgets.QFormLayout(form_widget)

        # Form Inputs
        form_layout.addRow("LineEdit:", QtWidgets.QLineEdit("Sample Text"))
        spin_box = QtWidgets.QSpinBox()
        spin_box.setRange(0, 100)
        form_layout.addRow("SpinBox:", spin_box)
        combo_box = QtWidgets.QComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        form_layout.addRow("ComboBox:", combo_box)
        date_edit = QtWidgets.QDateEdit()
        date_edit.setCalendarPopup(True)
        form_layout.addRow("DateEdit:", date_edit)

        return form_widget

    def create_display_tab(self):
        display_widget = QtWidgets.QWidget()
        display_layout = QtWidgets.QVBoxLayout(display_widget)

        # Display Widgets
        display_layout.addWidget(QtWidgets.QLabel("Label"))
        text_edit = QtWidgets.QTextEdit()
        text_edit.setPlainText("Text Edit Content")
        display_layout.addWidget(text_edit)
        progress_bar = QtWidgets.QProgressBar()
        progress_bar.setValue(50)
        display_layout.addWidget(progress_bar)

        return display_widget

    def create_container_tab(self):
        container_widget = QtWidgets.QWidget()
        container_layout = QtWidgets.QVBoxLayout(container_widget)

        # List Widget
        list_widget = QtWidgets.QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])
        container_layout.addWidget(list_widget)

        # Tree Widget
        tree_widget = QtWidgets.QTreeWidget()
        tree_widget.setHeaderLabels(["Column 1", "Column 2"])
        item = QtWidgets.QTreeWidgetItem(["Item 1", "Detail 1"])
        tree_widget.addTopLevelItem(item)
        container_layout.addWidget(tree_widget)

        # Table Widget
        table_widget = QtWidgets.QTableWidget(3, 2)
        table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2"])
        table_widget.setItem(0, 0, QtWidgets.QTableWidgetItem("Cell (0,0)"))
        table_widget.setItem(0, 1, QtWidgets.QTableWidgetItem("Cell (0,1)"))
        container_layout.addWidget(table_widget)

        return container_widget

    def create_button_group_tab(self):
        button_group_widget = QtWidgets.QWidget()
        button_group_layout = QtWidgets.QVBoxLayout(button_group_widget)

        # Button Widgets Group
        button_group = QtWidgets.QGroupBox("Button Widgets")
        button_layout = QtWidgets.QHBoxLayout(button_group)
        checkable_button = QtWidgets.QPushButton("Checkable PushButton")
        checkable_button.setCheckable(True)
        button_layout.addWidget(QtWidgets.QPushButton("PushButton"))
        button_layout.addWidget(checkable_button)
        tool_button = QtWidgets.QToolButton(button_group)
        tool_button.setText('Tool Button')
        button_layout.addWidget(tool_button)
        button_layout.addWidget(QtWidgets.QCheckBox("CheckBox"))
        button_layout.addWidget(QtWidgets.QRadioButton("RadioButton"))

        # Slider Widget
        slider_group = QtWidgets.QGroupBox("Slider Widget")
        slider_layout = QtWidgets.QHBoxLayout(slider_group)
        slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)  # Horizontal Slider
        slider_layout.addWidget(slider)

        button_group_layout.addWidget(button_group)
        button_group_layout.addWidget(slider_group)

        return button_group_widget

def main():
    app = QtWidgets.QApplication(sys.argv)
    set_theme(app, 'dark')

    demo = DemoWindow()
    demo.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
