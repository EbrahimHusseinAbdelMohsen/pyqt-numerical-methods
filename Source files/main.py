import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

import bisection_handler
import false_position_handler
import fixed_point_handler
import newton_handler 
import secant_handler
import gaussin_handler
import lu_handler
import gauss_jordan_handler
import cramers_handler

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Numerical Project.ui", self)
        
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon("Favicon.png"))
        self.setWindowTitle("Numerical Methods Project")

        try:
            with open("Black_Theme.qss", "r") as f:
                self.black_qss = f.read()
            with open("Gray_Theme.qss", "r") as f:
                self.gray_qss = f.read()
        except FileNotFoundError as e:
            print(f"Theme file error: {e}")
            self.black_qss = self.gray_qss = ""

        self.black_theme_radio_btn.toggled.connect(self.apply_black_theme)
        self.gray_theme_radio_btn.toggled.connect(self.apply_gray_theme)

        self.gray_theme_radio_btn.setChecked(True)
        
        self.apply_gray_theme(True)

        self._connect_navigation_buttons()
        self._connect_calculation_handlers()

    def apply_black_theme(self, checked):
        if checked:
            QApplication.instance().setStyleSheet(self.black_qss)

    def apply_gray_theme(self, checked):
        if checked:
            QApplication.instance().setStyleSheet(self.gray_qss)

    def _connect_navigation_buttons(self):
        nav_map = {
            self.settings_btn: 1,
            self.bisection_btn: 2,
            self.falseposition_btn: 3,
            self.simple_fixed_point_btn: 4,
            self.newton_btn: 5,
            self.secant_btn: 6,
            self.gaussin_elimination_btn: 7,
            self.lu_decomposition_btn: 8,
            self.cramersrule_btn: 9,
            self.gauss_jordan_btn: 10
        }

        for btn, index in nav_map.items():
            btn.clicked.connect(lambda _, i=index: self.tabWidget.setCurrentIndex(i))

        for i in range(1, 11):
            btn_name = f"back_{i}" if i > 1 else "back"
            if hasattr(self, btn_name):
                getattr(self, btn_name).clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))

    def _connect_calculation_handlers(self):
        calc_connections = [
            (self.gaussin_calc_btn, gaussin_handler.run_gaussin),
            (self.secant_calc_btn, secant_handler.run_secant),
            (self.fixed_point_calc_btn, fixed_point_handler.run_simple_fixed_point),
            (self.false_position_calc_btn, false_position_handler.run_false_position),
            (self.bisection_calc_btn, bisection_handler.run_bisection),
            (self.newton_calc_btn, newton_handler.run_newton),
            (self.lu_decomposition_calc_btn, lu_handler.run_lu),
            (self.gauss_jordan_calc_btn, gauss_jordan_handler.run_gauss_jordan),
            (self.cramers_calc_btn, cramers_handler.run_cramers),
        ]

        for btn, handler_func in calc_connections:
            btn.clicked.connect(lambda _, h=handler_func: h(self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())