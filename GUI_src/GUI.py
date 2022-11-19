# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class mainGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('form.ui', self)
        # self.GUI_item : we inherit everything from the above call
    
    def start(self):
        app = QApplication(sys.argv)
        self.show()
        sys.exit(app.exec())
 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = mainGUI()
    widget.show()
    sys.exit(app.exec())
