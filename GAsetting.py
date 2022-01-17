# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/shuhe/PycharmProjects/PhotovolaticGA/venv/GAsetting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import GAutils
import numpy as np


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 408)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-image:url(images.jpeg);")
        self.frame.setGeometry(QtCore.QRect(30, 90, 401, 271))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.PopSize_TF_3 = QtWidgets.QTextEdit(self.frame)
        self.PopSize_TF_3.setGeometry(QtCore.QRect(270, 30, 81, 31))
        self.PopSize_TF_3.setObjectName("PopSize_TF_3")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 140, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 90, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Confirm_BTN_3 = QtWidgets.QPushButton(self.frame)
        self.Confirm_BTN_3.setGeometry(QtCore.QRect(140, 210, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setBold(False)
        font.setWeight(50)
        self.Confirm_BTN_3.setFont(font)
        self.Confirm_BTN_3.setCheckable(False)
        self.Confirm_BTN_3.setObjectName("Confirm_BTN_3")
        self.Confirm_BTN_3.clicked.connect(lambda: self.Confirm_GAsetting(Dialog))
        self.NumOfGen_TF_4 = QtWidgets.QTextEdit(self.frame)
        self.NumOfGen_TF_4.setGeometry(QtCore.QRect(270, 80, 81, 31))
        self.NumOfGen_TF_4.setObjectName("NumOfGen_TF_4")
        self.MutatioRate_TF_5 = QtWidgets.QTextEdit(self.frame)
        self.MutatioRate_TF_5.setGeometry(QtCore.QRect(270, 130, 81, 31))
        self.MutatioRate_TF_5.setObjectName("MutatioRate_TF_5")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(30, 10, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GA-setting"))
        Dialog.setWindowIcon(QtGui.QIcon('icon.jpeg'))
        self.label_11.setText(_translate("Dialog", "Mutation rate:"))
        self.label_9.setText(_translate("Dialog", "Population size: "))
        self.label_10.setText(_translate("Dialog", "Number of generations:"))
        self.Confirm_BTN_3.setText(_translate("Dialog", "Confirm"))
        self.label_13.setText(_translate("Dialog", "GA setting"))

    def Confirm_GAsetting(self, dialog):
        """
        This method saves the data from UI to the system
        :param dialog: needed only to close the window after finished
        """
        print('Confirm GAsetting')
        PopSize = self.PopSize_TF_3.toPlainText()
        NumGen = self.NumOfGen_TF_4.toPlainText()
        MutatRate = self.MutatioRate_TF_5.toPlainText()
        if len(PopSize) is 0:
            PopSize2 = 0
        else:
            PopSize2 = int(PopSize)  # PopSize
        if len(NumGen) is 0:
            NumGen2 = 0
        else:
            NumGen2 = int(NumGen)  # NumGen
        if len(MutatRate) is 0:
            MutatRate2 = 0
        else:
            MutatRate2 = float(MutatRate)  # MutatRate
        flag = 0
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setText("Error")
        msg_box.setWindowTitle("Error")
        print(PopSize2, NumGen2, MutatRate2)
        if PopSize2 is 0 or NumGen2 is 0 or MutatRate2 is 0:
            print('im in none check\n')
            flag = 1
            msg_box.setInformativeText('One of the fields is empty!')
            msg_box.exec_()
        if MutatRate2 < 0 or MutatRate2 > 1:
            print('im in mutate Prob')
            flag = 1
            msg_box.setInformativeText('Mutate Rate is : 0 < x < 1')
            msg_box.exec_()
        if flag is 0:
            GAutils.CONST_POPULATION_SIZE = np.abs(PopSize2)
            GAutils.CONST_GENERATIONS = np.abs(NumGen2)
            GAutils.CONST_MUTATION_PROBABILITY = MutatRate2
            print(GAutils.CONST_GENERATIONS, GAutils.CONST_POPULATION_SIZE, GAutils.CONST_MUTATION_PROBABILITY)
            dialog.close()
