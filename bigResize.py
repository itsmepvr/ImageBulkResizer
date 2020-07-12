#! /usr/bin/python3
# -*- coding: utf-8 -*-
# bigResize
# Resize images in bulk
# Author: Venkata Ramana P
# Github: github.com/itsmepvr
# Email: <pvrreddy155@gmail.com>
# Date: 12 July 2020
# Covid-19 Pandemic :(

import os
from PIL import Image
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from os.path import expanduser

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(480, 410)
    MainWindow.setMinimumSize(QtCore.QSize(480, 410))
    MainWindow.setMaximumSize(QtCore.QSize(480, 410))
    MainWindow.setAutoFillBackground(False)
    MainWindow.setStyleSheet("font: 75 11pt \"Chilanka\";")
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.sourceBtn = QtWidgets.QPushButton(self.centralwidget)
    self.sourceBtn.setGeometry(QtCore.QRect(20, 40, 151, 25))
    self.sourceBtn.setObjectName("sourceBtn")
    self.sourceBtn.clicked.connect(self.chooseSrcDirectory)
    self.endBtn = QtWidgets.QPushButton(self.centralwidget)
    self.endBtn.setGeometry(QtCore.QRect(20, 80, 151, 25))
    self.endBtn.setObjectName("endBtn")
    self.endBtn.clicked.connect(self.chooseEndDirectory)
    self.sourceEdit = QtWidgets.QLineEdit(self.centralwidget)
    self.sourceEdit.setGeometry(QtCore.QRect(180, 40, 291, 25))
    self.sourceEdit.setObjectName("sourceEdit")
    self.endEdit = QtWidgets.QLineEdit(self.centralwidget)
    self.endEdit.setGeometry(QtCore.QRect(180, 80, 291, 25))
    self.endEdit.setObjectName("endEdit")
    self.widthBtn = QtWidgets.QPushButton(self.centralwidget)
    self.widthBtn.setGeometry(QtCore.QRect(20, 150, 81, 25))
    self.widthBtn.setObjectName("widthBtn")
    self.widthEdit = QtWidgets.QLineEdit(self.centralwidget)
    self.widthEdit.setGeometry(QtCore.QRect(120, 150, 81, 25))
    self.widthEdit.setObjectName("widthEdit")
    self.heightBtn = QtWidgets.QPushButton(self.centralwidget)
    self.heightBtn.setGeometry(QtCore.QRect(230, 150, 81, 25))
    self.heightBtn.setObjectName("heightBtn")
    self.heightEdit = QtWidgets.QLineEdit(self.centralwidget)
    self.heightEdit.setGeometry(QtCore.QRect(330, 150, 81, 25))
    self.heightEdit.setObjectName("heightEdit")
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(20, 120, 201, 17))
    self.label.setObjectName("label")
    self.aspectCheckBox = QtWidgets.QCheckBox(self.centralwidget)
    self.aspectCheckBox.setGeometry(QtCore.QRect(20, 190, 201, 23))
    self.aspectCheckBox.setObjectName("aspectCheckBox")
    self.aspectCheckBox.setChecked(True)
    self.aspectCheckBox.setEnabled(False)
    self.aspectCheckBox.stateChanged.connect(lambda:self.btnstate(self.aspectCheckBox))
    self.label_2 = QtWidgets.QLabel(self.centralwidget)
    self.label_2.setGeometry(QtCore.QRect(20, 230, 101, 17))
    self.label_2.setObjectName("label_2")
    self.aspectEdit = QtWidgets.QLineEdit(self.centralwidget)
    self.aspectEdit.setGeometry(QtCore.QRect(120, 220, 41, 25))
    self.aspectEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
    self.aspectEdit.setAutoFillBackground(False)
    self.aspectEdit.setObjectName("aspectEdit")
    self.aspectEdit.setEnabled(False)
    self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
    self.progressBar.setGeometry(QtCore.QRect(97, 270, 291, 23))
    self.progressBar.setProperty("value", 0)
    self.progressBar.setObjectName("progressBar")
    self.progressBar.hide()
    self.resizeBtn = QtWidgets.QPushButton(self.centralwidget)
    self.resizeBtn.setGeometry(QtCore.QRect(260, 320, 88, 25))
    self.resizeBtn.setObjectName("resizeBtn")
    self.resizeBtn.clicked.connect(self.resizeImages)
    self.aboutBtn = QtWidgets.QPushButton(self.centralwidget)
    self.aboutBtn.setGeometry(QtCore.QRect(370, 320, 88, 25))
    self.aboutBtn.setObjectName("aboutBtn")
    self.line = QtWidgets.QFrame(self.centralwidget)
    self.line.setGeometry(QtCore.QRect(7, 350, 461, 20))
    self.line.setFrameShape(QtWidgets.QFrame.HLine)
    self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line.setObjectName("line")
    self.label_3 = QtWidgets.QLabel(self.centralwidget)
    self.label_3.setGeometry(QtCore.QRect(10, 370, 121, 17))
    self.label_3.setStyleSheet("color:blue;")
    self.label_3.setObjectName("label_3")
    self.label_4 = QtWidgets.QLabel(self.centralwidget)
    self.label_4.setGeometry(QtCore.QRect(330, 370, 141, 17))
    self.label_4.setStyleSheet("color:blue;")
    self.label_4.setObjectName("label_4")
    MainWindow.setCentralWidget(self.centralwidget)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "bigResize"))
    self.sourceBtn.setText(_translate("MainWindow", "Choose Source Path"))
    self.endBtn.setText(_translate("MainWindow", "Choose End Path"))
    self.widthBtn.setText(_translate("MainWindow", "Width"))
    self.widthEdit.setText(_translate("MainWindow", "400"))
    self.heightBtn.setText(_translate("MainWindow", "Height"))
    self.heightEdit.setText(_translate("MainWindow", "400"))
    self.label.setText(_translate("MainWindow", "Select Image Size (in px)"))
    self.aspectCheckBox.setText(_translate("MainWindow", "Keep image aspect ratio"))
    self.label_2.setText(_translate("MainWindow", "Aspect ratio : "))
    self.aspectEdit.setText(_translate("MainWindow", "1:1"))
    self.resizeBtn.setText(_translate("MainWindow", "Resize"))
    self.aboutBtn.setText(_translate("MainWindow", "About"))
    self.label_3.setText(_translate("MainWindow", "bigResize-v0.0.1"))
    self.label_4.setText(_translate("MainWindow", "github.com/itsmepvr"))
    
  def validateForm(self):
    srcText = self.sourceEdit.text()
    endText = self.endEdit.text()
    widthText = self.widthEdit.text()
    heightText = self.heightEdit.text()
    aspectText = '1:1'
    if self.aspectCheckBox.isChecked == False:
      aspectText = self.aspectEdit.text()
    errorFields = []
    if srcText == '':
      errorFields.append('Missing source path')
    if endText == '':
      errorFields.append('Missing end path')
    if widthText == '':
      errorFields.append('Missing width')
    if heightText == '':
      errorFields.append('Missing height')
    if aspectText == '':
      errorFields.append('Missing aspect ratio')
    return errorFields                     
    
  def btnstate(self, b):
    if b.isChecked() == True:
      self.aspectEdit.setEnabled(False)
    else:
      self.aspectEdit.setEnabled(True) 
    self.progressBar.hide()       
  
  def chooseSrcDirectory(self):
    src_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
    self.sourceEdit.setText(src_dir)
    self.endEdit.setText(src_dir)
    self.progressBar.hide()
    
  def chooseEndDirectory(self):
    end_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
    self.endEdit.setText(end_dir)
    self.progressBar.hide() 
  
  def resizeImages(self):
    errors = self.validateForm()
    if len(errors) > 0:
      QMessageBox.warning(None, "Warning", "\n".join(errors), QtWidgets.QMessageBox.Ok)
      return
    srcPath = self.endEdit.text()
    width = float(self.widthEdit.text())
    height = float(self.heightEdit.text())
    print(width)
    files = os.listdir(srcPath)
    incValue = 100/len(files)
    totalLen = 0
    itemCount = 0
    self.progressBar.setValue(0)
    self.progressBar.show()
    errorImages = []
    for item in files:
      if os.path.isfile(os.path.join(srcPath, item)):
        if item.endswith('png') or item.endswith('jpg') or item.endswith  ('jpeg'):
          fileName = os.path.join(srcPath, item)
          try:
            img = Image.open(fileName)
            new_img = img.resize((width,height))
            new_img.save(fileName)   
            totalLen += 1
          except IOError:
            print ('%s could not be opened' % fileName)
            errorImages.append(item)
        itemCount += incValue
      self.progressBar.setValue(itemCount)
    self.progressBar.setValue(100)  
    if len(errorImages) > 0:
      QMessageBox.information(None, "Resize Images", str(totalLen)+" images are resized \n "+errorImages.join(", ")+" could note be opened", QtWidgets.QMessageBox.Ok)    
    else:
      QMessageBox.information(None, "Resize Images", str(totalLen)+" images are resized \n No errors in the process", QtWidgets.QMessageBox.Ok)  
    

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())