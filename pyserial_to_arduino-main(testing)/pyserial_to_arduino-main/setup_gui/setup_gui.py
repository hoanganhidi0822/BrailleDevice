#pyinstaller -F -w -i dist\setup.ico -n setup setup_gui.py
#pyuic5 -x gui.ui -o gui.py

import sys, shutil, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.uic.label.setPixmap(QPixmap("img.jpg"))
        self.main_win.setWindowIcon(QIcon("setup.ico"))

        self.dst = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp"
        self.src = "main.exe"
        self.icon = "product.ico"

        self.uic.pushButton_2.clicked.connect(self.cancel)
        self.uic.pushButton.clicked.connect(self.install)

    def install(self):
        try:
            shutil.copy2(self.src, self.dst + "/" + os.path.basename(self.src))
            shutil.copy2(self.src, self.dst + "/" + os.path.basename(self.icon))
            self.uic.label_3.setText("    Install success!    ")
            self.uic.label_3.setStyleSheet("background-color: green; color: white; border-style: outset; border-width: 2px; border-color: rgb(149, 149, 149); min-width: 10em; border-radius: 5px;")
                
        except:
            self.uic.label_3.setText("    Run as Administrator is required!    ")
            self.uic.label_3.setStyleSheet("background-color: red; color: yellow; border-style: outset; border-width: 2px; border-color: rgb(149, 149, 149); min-width: 10em; border-radius: 5px;")
            self.uic.pushButton_2.setText("Exit")

    def cancel(self):
        self.main_win.close()

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())