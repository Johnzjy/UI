# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:18:20 2018

@author: 310128142
"""
from qtpy import QtCore,QtWidgets,QtGui
from qtpy.QtWebEngineWidgets import QWebEngineView
from qtpy.QtCore import Qt,QUrl,QDate
import time
import os,sys



class MainWindow_UI(object):
    def __init__(self):
        self.WindowStyle="""background-color:rgba(0, 0, 0, 0);
                      
                            border-width: 1px;
                            border-style: solid solid solid solid;
                            border-color: white black black white;
                            border-radius: 4px;
                            """
        self.WingetStyle="""
                            background:white;
                            border-width: 0.5px;
                            border-style: solid solid solid solid;
                            border-color: black;
                            border-radius: 2px;
     
                            """   


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350,750)
        MainWindow.setWindowTitle('GUI 界面')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.create_window(MainWindow)
        
    def create_window(self,MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow) #主框
        self.centralwidget.setStyleSheet(self.WindowStyle)
      

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        
        self.createLeftGroupBox()
        self.createGraphBox()
        self.createRightGroupBox()
        self.creatFormGroupBox()
        mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        hboxLayout = QtWidgets.QHBoxLayout()
        #hboxLayout.addStretch()  
        hboxLayout.addWidget(self.LeftGroupBox)
        hboxLayout.addWidget(self.GraphTab)
        hboxLayout.addWidget(self.RightGroupBox)
        hboxLayout.setStretch(0,10)
        hboxLayout.setStretch(1,70)
        hboxLayout.setStretch(2,20)
        
        
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.setStretch(0, 90)
        mainLayout.setStretch(1, 10)
      
        #self.setLayout(mainLayout)
    def createGraphBox(self):
        self.GraphTab=QtWidgets.QTabWidget()
        self.GraphTab.setStyleSheet(self.WingetStyle)
        self.GraphTab.setObjectName("Graph Tab")
        self.createTAB()
        
    def createTAB(self):
        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setMinimumSize(QtCore.QSize(500, 400))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.WebTab=self.GraphTab.addTab(self.webView,'Web view')
        #self.GraphBox=QtWidgets.QWidget()
        #self.GraphTab=self.GraphTab.addTab(self.GraphBox,'graph view')
        
    def setQbutton(self,QButton):
        self.ButtonStyle="""
                            background:lightgray;
                            border-width: 0.5px;
                            border-style: none;
                            border-color: black;
                            border-radius: 2px;
     
                            """   
        QButton.setFixedSize(150,30)
        QButton.setStyleSheet(self.ButtonStyle)
    
    def createLeftGroupBox(self):
        self.LeftGroupBox = QtWidgets.QGroupBox("Grid layout")
        self.LeftGroupBox.setStyleSheet(self.WingetStyle)
        layout = QtWidgets.QGridLayout()
        self.AButton=QtWidgets.QPushButton("A")
        self.BButton=QtWidgets.QPushButton("B")
        self.CButton=QtWidgets.QPushButton("C")
        self.DButton=QtWidgets.QPushButton("D")
        self.setQbutton(self.AButton)
        self.setQbutton(self.BButton)
        self.setQbutton(self.CButton)
        self.setQbutton(self.DButton)
        
        layout.setSpacing(100) 
        layout.addWidget(self.AButton,0,0)
        layout.addWidget(self.BButton,1,0)
        layout.addWidget(self.CButton,0,1)
        layout.addWidget(self.DButton,1,1)
        self.LeftGroupBox.setLayout(layout)
  

    def createRightGroupBox(self):
        self.RightGroupBox = QtWidgets.QGroupBox("Vbox layout")
        self.RightGroupBox.setStyleSheet(self.WingetStyle)
        layout = QtWidgets.QGridLayout()
        bigEditor = QtWidgets.QTextEdit()
        bigEditor.setPlainText("搭载了空间冷原子钟等14项应用载荷，以及失重心血管研究等航天医学实验设备 "
                "开展空间科学及技术试验.")
        layout.addWidget(bigEditor)
        self.RightGroupBox.setLayout(layout)
        

    def creatFormGroupBox(self):
        self.formGroupBox = QtWidgets.QGroupBox("Form layout")
        self.formGroupBox.setStyleSheet(self.WingetStyle)

        layout = QtWidgets.QFormLayout()
        performanceLabel = QtWidgets.QLabel("性能特点：")
        performanceEditor = QtWidgets.QLineEdit("舱内设计更宜居方便天宫生活")
        planLabel = QtWidgets.QLabel("发射规划：")
        planEditor = QtWidgets.QTextEdit()
        planEditor.setPlainText("2020年之前，中国计划初步完成空间站建设")
        layout.addRow(performanceLabel,performanceEditor)
        layout.addRow(planLabel,planEditor)
        self.formGroupBox.setLayout(layout)