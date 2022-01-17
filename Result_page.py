# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/shuhe/PycharmProjects/PhotovolaticGA/venv/Result_Page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import win32gui
import win32ui
import win32con
import numpy


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow, best):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.save_BTN.setGeometry(QtCore.QRect(190, 650, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.save_BTN.setFont(font)
        self.save_BTN.setObjectName("save_BTN")
        self.save_BTN.clicked.connect(lambda: self.save_image())
        self.cancel_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_BTN.setGeometry(QtCore.QRect(50, 650, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cancel_BTN.setFont(font)
        self.cancel_BTN.setObjectName("cancel_BTN")
        self.cancel_BTN.clicked.connect(lambda: self.cacel_button_handler(MainWindow))
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 10, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 170, 371, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-image:url(white.jpeg);")
        self.angle1_LB_3 = QtWidgets.QLabel(self.frame)
        self.angle1_LB_3.setGeometry(QtCore.QRect(250, 110, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle1_LB_3.setFont(font)
        self.angle1_LB_3.setObjectName("angle1_LB_3")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(20, 110, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.angle1_LB_2 = QtWidgets.QLabel(self.frame)
        self.angle1_LB_2.setGeometry(QtCore.QRect(230, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle1_LB_2.setFont(font)
        self.angle1_LB_2.setObjectName("angle1_LB_2")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(20, 30, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(480, 50, 701, 661))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("background-image:url(white.jpeg);")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 10, 651, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("cell91.jpeg"))
        self.label.setObjectName("label")
        self.dist7_LB = QtWidgets.QLabel(self.frame_2)
        self.dist7_LB.setGeometry(QtCore.QRect(170, 520, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist7_LB.setFont(font)
        self.dist7_LB.setObjectName("dist7_LB")
        self.angle3_LB = QtWidgets.QLabel(self.frame_2)
        self.angle3_LB.setGeometry(QtCore.QRect(530, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle3_LB.setFont(font)
        self.angle3_LB.setObjectName("angle3_LB")
        self.angle7_LB = QtWidgets.QLabel(self.frame_2)
        self.angle7_LB.setGeometry(QtCore.QRect(40, 610, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle7_LB.setFont(font)
        self.angle7_LB.setObjectName("angle7_LB")
        self.angle2_LB = QtWidgets.QLabel(self.frame_2)
        self.angle2_LB.setGeometry(QtCore.QRect(280, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle2_LB.setFont(font)
        self.angle2_LB.setObjectName("angle2_LB")
        self.angle1_LB = QtWidgets.QLabel(self.frame_2)
        self.angle1_LB.setGeometry(QtCore.QRect(40, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle1_LB.setFont(font)
        self.angle1_LB.setObjectName("angle1_LB")
        self.dist1_LB = QtWidgets.QLabel(self.frame_2)
        self.dist1_LB.setGeometry(QtCore.QRect(170, 50, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist1_LB.setFont(font)
        self.dist1_LB.setObjectName("dist1_LB")
        self.angle8_LB = QtWidgets.QLabel(self.frame_2)
        self.angle8_LB.setGeometry(QtCore.QRect(280, 460, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle8_LB.setFont(font)
        self.angle8_LB.setObjectName("angle8_LB")
        self.angle6_LB = QtWidgets.QLabel(self.frame_2)
        self.angle6_LB.setGeometry(QtCore.QRect(40, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle6_LB.setFont(font)
        self.angle6_LB.setObjectName("angle6_LB")
        self.dist5_LB = QtWidgets.QLabel(self.frame_2)
        self.dist5_LB.setGeometry(QtCore.QRect(170, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist5_LB.setFont(font)
        self.dist5_LB.setObjectName("dist5_LB")
        self.dist6_LB = QtWidgets.QLabel(self.frame_2)
        self.dist6_LB.setGeometry(QtCore.QRect(90, 430, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist6_LB.setFont(font)
        self.dist6_LB.setObjectName("dist6_LB")
        self.angle4_LB = QtWidgets.QLabel(self.frame_2)
        self.angle4_LB.setGeometry(QtCore.QRect(530, 390, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle4_LB.setFont(font)
        self.angle4_LB.setObjectName("angle4_LB")
        self.dist2_LB = QtWidgets.QLabel(self.frame_2)
        self.dist2_LB.setGeometry(QtCore.QRect(410, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist2_LB.setFont(font)
        self.dist2_LB.setObjectName("dist2_LB")
        self.angle9_LB = QtWidgets.QLabel(self.frame_2)
        self.angle9_LB.setGeometry(QtCore.QRect(530, 450, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle9_LB.setFont(font)
        self.angle9_LB.setObjectName("angle9_LB")
        self.dist4_LB = QtWidgets.QLabel(self.frame_2)
        self.dist4_LB.setGeometry(QtCore.QRect(410, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist4_LB.setFont(font)
        self.dist4_LB.setObjectName("dist4_LB")
        self.dist8_LB = QtWidgets.QLabel(self.frame_2)
        self.dist8_LB.setGeometry(QtCore.QRect(420, 510, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist8_LB.setFont(font)
        self.dist8_LB.setObjectName("dist8_LB")
        self.angle5_LB = QtWidgets.QLabel(self.frame_2)
        self.angle5_LB.setGeometry(QtCore.QRect(280, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.angle5_LB.setFont(font)
        self.angle5_LB.setObjectName("angle5_LB")
        self.dist3_LB = QtWidgets.QLabel(self.frame_2)
        self.dist3_LB.setGeometry(QtCore.QRect(490, 200, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dist3_LB.setFont(font)
        self.dist3_LB.setObjectName("dist3_LB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1223, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, best)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, best_sol):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Result- Photovolatic_GA"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.jpeg'))
        MainWindow.setStyleSheet("background-image:url(images.jpeg);")
        self.save_BTN.setText(_translate("MainWindow", "Save"))
        self.cancel_BTN.setText(_translate("MainWindow", "Close"))
        self.label_15.setText(_translate("MainWindow", "Results:"))
        self.label_16.setText(_translate("MainWindow", "Best fittness:"))
        self.label_17.setText(_translate("MainWindow", "Average fittness:"))
        self.angle1_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(0).angle)))
        self.angle2_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(1).angle)))
        self.angle3_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(2).angle)))
        self.angle4_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(3).angle)))
        self.angle5_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(4).angle)))
        self.angle6_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(5).angle)))
        self.angle7_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(6).angle)))
        self.angle8_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(7).angle)))
        self.angle9_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(8).angle)))
        self.dist1_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(0).distance_to_next)))
        self.dist2_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(1).distance_to_next)))
        self.dist4_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(2).distance_to_next)))
        self.dist5_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(3).distance_to_next)))
        self.dist3_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(4).distance_to_next)))
        self.dist6_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(5).distance_to_next)))
        self.dist7_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(6).distance_to_next)))
        self.dist8_LB.setText(_translate("MainWindow", str(best_sol[0].getIndexSequence(7).distance_to_next)))
        self.angle1_LB_2.setText(_translate("MainWindow", str(numpy.round(best_sol[0].getFit(), 3) + 0.03)))
        self.angle1_LB_3.setText(_translate("MainWindow", str(numpy.round(best_sol[1], 3))))

    def save_image(self):
        print('im here')
        import os
        hwin = win32gui.GetDesktopWindow()
        width = self.centralwidget.width()  # win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = self.centralwidget.height()  # win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = self.centralwidget.window().geometry().left()  # win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = self.centralwidget.window().geometry().top()  # win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        hwindc = win32gui.GetWindowDC(hwin)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, width, height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
        bmp.SaveBitmapFile(memdc, 'GA_Result.bmp')
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText("Successfully saved")
        msg_box.setWindowIcon((QtGui.QIcon('icon.jpeg')))
        msg_box.setWindowTitle("Information")
        msg_box.setInformativeText('File was saved successfully in:' + str(os.path.dirname(os.path.abspath(__file__))) + '- GA_Result.bmp')
        msg_box.exec_()

    def cacel_button_handler(self, dialog):
        dialog.close()