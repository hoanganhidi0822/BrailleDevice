# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label.setMinimumSize(QtCore.QSize(300, 330))
        self.label.setMaximumSize(QtCore.QSize(300, 350))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 63 15pt \"Segoe UI Semibold\";")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(234, 30))
        self.label_3.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(149, 149, 149);\n"
"min-width: 10em;\n"
"border-radius: 5px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 25, 25)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Your Application Setup"))
        self.label_2.setText(_translate("MainWindow", "Welcome to Your Application Setup Wizard"))
        self.label_3.setText(_translate("MainWindow", "Notification"))
        self.pushButton.setText(_translate("MainWindow", "Install"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
