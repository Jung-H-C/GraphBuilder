# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphbuild_demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(280, 550, 491, 101))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.graph_frame = QtWidgets.QFrame(self.centralwidget)
        self.graph_frame.setGeometry(QtCore.QRect(380, 20, 661, 471))
        self.graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_frame.setObjectName("graph_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.graph_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(54, 89, 60, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_x_label = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x_label.setGeometry(QtCore.QRect(120, 58, 231, 20))
        self.lineEdit_x_label.setObjectName("lineEdit_x_label")
        self.radioButton_black = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_black.setGeometry(QtCore.QRect(210, 249, 41, 16))
        self.radioButton_black.setObjectName("radioButton_black")
        self.lineEdit_x_value = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x_value.setGeometry(QtCore.QRect(120, 90, 231, 20))
        self.lineEdit_x_value.setObjectName("lineEdit_x_value")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(53, 217, 60, 20))
        self.label_3.setObjectName("label_3")
        self.comboBox_marker = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_marker.setGeometry(QtCore.QRect(120, 216, 131, 22))
        self.comboBox_marker.setObjectName("comboBox_marker")
        self.comboBox_marker.addItem("")
        self.comboBox_marker.addItem("")
        self.comboBox_marker.addItem("")
        self.comboBox_marker.addItem("")
        self.radioButton_red = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_red.setGeometry(QtCore.QRect(162, 249, 51, 16))
        self.radioButton_red.setObjectName("radioButton_red")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(54, 150, 60, 20))
        self.label_8.setObjectName("label_8")
        self.radioButton_custom = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_custom.setGeometry(QtCore.QRect(257, 249, 81, 16))
        self.radioButton_custom.setObjectName("radioButton_custom")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(54, 124, 56, 12))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(53, 247, 60, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 276, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(120, 276, 75, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.lineEdit_y_value = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_y_value.setGeometry(QtCore.QRect(120, 150, 231, 20))
        self.lineEdit_y_value.setObjectName("lineEdit_y_value")
        self.lineEdit_y_label = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_y_label.setGeometry(QtCore.QRect(120, 120, 231, 20))
        self.lineEdit_y_label.setObjectName("lineEdit_y_label")
        self.radioButton_blue = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_blue.setGeometry(QtCore.QRect(115, 249, 51, 16))
        self.radioButton_blue.setChecked(True)
        self.radioButton_blue.setObjectName("radioButton_blue")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(54, 59, 60, 20))
        self.label_5.setObjectName("label_5")
        self.comboBox_line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_line.setGeometry(QtCore.QRect(120, 186, 131, 22))
        self.comboBox_line.setObjectName("comboBox_line")
        self.comboBox_line.addItem("")
        self.comboBox_line.addItem("")
        self.comboBox_line.addItem("")
        self.comboBox_line.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(53, 187, 60, 20))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAbout.addAction(self.actionExit)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "x값"))
        self.radioButton_black.setText(_translate("MainWindow", "검정"))
        self.label_3.setText(_translate("MainWindow", "마커"))
        self.comboBox_marker.setItemText(0, _translate("MainWindow", "point marker"))
        self.comboBox_marker.setItemText(1, _translate("MainWindow", "pixel marker"))
        self.comboBox_marker.setItemText(2, _translate("MainWindow", "circle marker"))
        self.comboBox_marker.setItemText(3, _translate("MainWindow", "square marker"))
        self.radioButton_red.setText(_translate("MainWindow", "빨강"))
        self.label_8.setText(_translate("MainWindow", "y값"))
        self.radioButton_custom.setText(_translate("MainWindow", "사용자 설정"))
        self.label_6.setText(_translate("MainWindow", "y축 라벨"))
        self.label_2.setText(_translate("MainWindow", "색상"))
        self.pushButton_2.setText(_translate("MainWindow", "Build"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.radioButton_blue.setText(_translate("MainWindow", "파랑"))
        self.label_5.setText(_translate("MainWindow", "x축 라벨"))
        self.comboBox_line.setItemText(0, _translate("MainWindow", "solid line style"))
        self.comboBox_line.setItemText(1, _translate("MainWindow", "dashed line style"))
        self.comboBox_line.setItemText(2, _translate("MainWindow", "dash-dot line style"))
        self.comboBox_line.setItemText(3, _translate("MainWindow", "dotted line style"))
        self.label_4.setText(_translate("MainWindow", "선 종류"))
        self.menuAbout.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
