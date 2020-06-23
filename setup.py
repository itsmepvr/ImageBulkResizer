#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import glob
from PIL import Image
import sys
# localPath = './'
# imgg = glob.glob('./*.jpg')
# for fileName in imgg:
#   images = glob.glob("./*.jpg")
#   img = Image.open('a.jpg')
#   new_img = img.resize((500,500))
#   new_img.save("a.jpg")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from os.path import expanduser

class Ui_Dialog(object):
  def setupUi(self, Dialog):
    Dialog.setObjectName("Dialog")
    Dialog.setEnabled(True)
    Dialog.resize(500, 240)
    self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
    self.buttonBox.setGeometry(QtCore.QRect(180, 190, 301, 32))
    self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
    self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
    self.buttonBox.setObjectName("buttonBox")
    self.radioButton = QtWidgets.QRadioButton(Dialog)
    self.radioButton.setGeometry(QtCore.QRect(20, 140, 161, 23))
    self.radioButton.setObjectName("radioButton")
    self.lineEdit = QtWidgets.QLineEdit(Dialog)
    self.lineEdit.setEnabled(True)
    self.lineEdit.setGeometry(QtCore.QRect(120, 20, 361, 25))
    self.lineEdit.setObjectName("lineEdit")
    self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
    self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 361, 25))
    self.lineEdit_2.setObjectName("lineEdit_2")
    self.pushButton = QtWidgets.QPushButton(Dialog)
    self.pushButton.setGeometry(QtCore.QRect(7, 20, 101, 25))
    self.pushButton.setObjectName("pushButton")
    self.pushButton_2 = QtWidgets.QPushButton(Dialog)
    self.pushButton_2.setGeometry(QtCore.QRect(7, 60, 101, 25))
    self.pushButton_2.setObjectName("pushButton_2")
    self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
    self.lineEdit_3.setGeometry(QtCore.QRect(120, 100, 61, 25))
    self.lineEdit_3.setObjectName("lineEdit_3")
    self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
    self.lineEdit_4.setGeometry(QtCore.QRect(210, 100, 61, 25))
    self.lineEdit_4.setObjectName("lineEdit_4")
    self.label = QtWidgets.QLabel(Dialog)
    self.label.setGeometry(QtCore.QRect(190, 110, 21, 21))
    self.label.setObjectName("label")
    self.label_2 = QtWidgets.QLabel(Dialog)
    self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 17))
    self.label_2.setObjectName("label_2")

    self.retranslateUi(Dialog)
    self.buttonBox.accepted.connect(Dialog.accept)
    self.buttonBox.rejected.connect(Dialog.reject)
    self.pushButton.clicked.connect(self.choose_directory)
    self.pushButton_2.clicked.connect(self.src_directory)
    QtCore.QMetaObject.connectSlotsByName(Dialog)

  def retranslateUi(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", "bigResize"))
    self.radioButton.setText(_translate("Dialog", "Keep Aspect Ratio"))
    self.pushButton.setText(_translate("Dialog", "Choose path"))
    self.pushButton_2.setText(_translate("Dialog", "Source Path"))
    self.lineEdit_3.setText(_translate("Dialog", "400"))
    self.lineEdit_4.setText(_translate("Dialog", "400"))
    self.label.setText(_translate("Dialog", "X"))
    self.label_2.setText(_translate("Dialog", "Image Size"))
  
  def choose_directory(self):
    input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
    self.lineEdit.setText(input_dir)
    self.lineEdit_2.setText(input_dir)
    
  def src_directory(self):
    input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
    self.lineEdit_2.setText(input_dir)     
       

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
  def __init__(self, *args, obj=None, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()