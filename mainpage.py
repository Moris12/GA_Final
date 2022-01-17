# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/shuhe/PycharmProjects/PhotovolaticGA/venv/MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import GAutils
from GAsetting import Ui_Dialog
from Result_page import Ui_MainWindow2
import Population
import numpy as np
import main


class Ui_MainWindow(object):
    population = Population.Population()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(907, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-image:url(images.jpeg);")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 140, 861, 371))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(650, 80, 111, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(230, 90, 111, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(500, 150, 121, 19))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 140, 111, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(470, 230, 121, 19))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(500, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(650, 230, 111, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(460, 50, 121, 19))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(650, 140, 111, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(70, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(70, 90, 121, 19))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 121, 19))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 310, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.get_data_from_user())
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 310, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.open_GAsetting())
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(20, 220, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_6.setGeometry(QtCore.QRect(230, 230, 111, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 30, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 907, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon('icon.jpeg'))
        MainWindow.setWindowTitle(_translate("MainWindow", "PV-Master"))
        self.label_6.setText(_translate("MainWindow", "width:"))
        self.label_9.setText(_translate("MainWindow", "Azimuth:"))
        self.label_5.setText(_translate("MainWindow", "Length:"))
        self.label_3.setText(_translate("MainWindow", "Cell\'s size:"))
        self.label_8.setText(_translate("MainWindow", "Longitude:"))
        self.label_7.setText(_translate("MainWindow", "Latitude:"))
        self.label_4.setText(_translate("MainWindow", "Landmark:"))
        self.pushButton.setText(_translate("MainWindow", "Go!"))
        self.pushButton_2.setText(_translate("MainWindow", "GA setting"))
        self.label_10.setText(_translate("MainWindow", "Field Area (nxn):"))
        self.label_15.setText(_translate("MainWindow", "PV-Array Configuration"))

    def get_data_from_user(self):
        print('im in the function')
        flag = 0
        z = self.textEdit.toPlainText()  # latitude
        y = self.textEdit_2.toPlainText()  # length
        x = self.textEdit_3.toPlainText()  # width
        q = self.textEdit_4.toPlainText()  # longtitude
        w = self.textEdit_5.toPlainText()  # azimuth
        e = self.textEdit_6.toPlainText()  # area
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setText("Error")
        msg_box.setWindowTitle("Error")
        if len(x) is 0:
            length = 0
        else:
            length = int(x)  # length
        if len(w) is 0:
            azimuth = 0
        else:
            azimuth = int(w)  # azimuth
        if len(y) is 0:
            long = 0
        else:
            long = int(y)  # long
        if len(q) is 0:
            width = 0
        else:
            width = int(q)  # width
        if len(z) is 0:
            lat = 0
        else:
            lat = int(z)  # lat
        if len(e) is 0:
            area = 0
        else:
            area = int(e)  # lat
        print(length, width, lat, long, azimuth)
        if width is 0 or length is 0 or lat is 0 or long is 0 or azimuth is 0 or area is 0:
            print('im in none check\n')
            flag = 1
            msg_box.setInformativeText('One of the fields is empty!')
            msg_box.exec_()
        else:
            if width > GAutils.CONST_MAX_LENGTH or width < GAutils.CONST_MIN_LENGTH:
                print('im in width')
                flag = 1
                msg_box.setInformativeText('Length error')
                msg_box.exec_()
            if length > GAutils.CONST_MAX_WIDTH or length < GAutils.CONST_MIN_WIDTH:
                print('im in length')
                flag = 1
                msg_box.setInformativeText('width error')
                msg_box.exec_()
            if lat > GAutils.CONST_MAX_LATITUDE or lat < GAutils.CONST_MIN_LATITUDE:
                print('im in latitude')
                flag = 1
                msg_box.setInformativeText('Latitude is not valid!')
                msg_box.exec_()
            if area < (width * 3) + 4:
                print('im in area error')
                flag = 1
                msg_box.setInformativeText('Area field is too small')
                msg_box.exec_()
            if azimuth > 360 or azimuth < 0:
                print('im in azimuth')
                flag = 1
                msg_box.setInformativeText('Azimuth is not legal!')
                msg_box.exec_()
        print(flag)
        if flag is 0:
            self.population.cell_length = length
            self.population.cell_width = width
            self.population.azimuth = azimuth
            self.population.latitude = lat
            self.population.longtitude = long
            self.population.area = area
            GAutils.CONST_MAX_DISTANCE = np.floor((area - (3 * width)) / 2)
            print(GAutils.CONST_MAX_DISTANCE)
            lst = main.main_run(self.population)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi(self.window, lst)
            self.window.show()

    def open_GAsetting(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
