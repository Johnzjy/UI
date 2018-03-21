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
        self.LogText ="""2018-3-8 15:09:18 开始奔跑，good luck!/n"""


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
        self.p=PatientLoginWindow()
   #按钮的动作 
        self.webButtonAction()
        self.PatientButtonAction()
        
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
        hboxLayout.setSpacing(10) #设置间隔信息
        hboxLayout.setStretch(0,5)
        hboxLayout.setStretch(1,400)
        hboxLayout.setStretch(2,60)
        
        
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
        
    def setQbutton(self,QButton,pixPATH,name):
        self.ButtonStyle="""
                            background:rgba(0, 0, 0, 0);
                            border-width: 0.5px;
                            border-style: none;
                            border-color: black;
                            border-radius: 2px;
                            icon-size:50px 5px;
                           
                            """   
        QButton.setText(name)                 
        QButton.setIcon(QtGui.QIcon(QtGui.QPixmap(pixPATH)))
        QButton.setFixedSize(68,68)#设置按钮大小
        QButton.setStyleSheet(self.ButtonStyle)
        QButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)#设置文字在图标面 

        #QButton.setIconSize(150,150)
    
    def createLeftGroupBox(self):
        self.LeftGroupBox = QtWidgets.QGroupBox("Grid layout")
        self.LeftGroupBox.setStyleSheet(self.WingetStyle)
        #self.LeftGroupBox.setFixedSize(200,600)
        layout = QtWidgets.QGridLayout()
        

        '''
        创建按钮
        '''
        self.DatasButton=QtWidgets.QToolButton()#数据按钮
        self.GraphButton=QtWidgets.QToolButton()#绘图
        self.ContactsButton=QtWidgets.QToolButton()#联系人
        self.PatientButton=QtWidgets.QToolButton()#病人信息
        self.FileButton=QtWidgets.QToolButton()#文件
        self.WebButton=QtWidgets.QToolButton()#网络
        self.CloudButton=QtWidgets.QToolButton()
        self.ScanButton=QtWidgets.QToolButton()
        '''
        设置按钮的外观
        '''
        self.setQbutton(self.DatasButton,'ICON\\pie.ico',"Date")
        self.setQbutton(self.GraphButton,'ICON\\bar.ico',"Graph")
        self.setQbutton(self.ContactsButton,'ICON\\contacts.ico',"contacts")
        self.setQbutton(self.PatientButton,'ICON\\patient.ico',"patient")
        self.setQbutton(self.FileButton,'ICON\\file.ico',"File")
        self.setQbutton(self.WebButton,'ICON\\baidu.ico',"Web")
        self.setQbutton(self.CloudButton,'ICON\\Cloud.ico',"Cloud")
        self.setQbutton(self.ScanButton,'ICON\\Scan.png',"Scan")
        '''
        设置按钮位置信息
        '''
        layout.setSpacing(2) 
        layout.addWidget(self.DatasButton,0,0)
        layout.addWidget(self.GraphButton,1,0)
        layout.addWidget(self.ContactsButton,0,1)
        layout.addWidget(self.PatientButton,1,1)
        layout.addWidget(self.FileButton,2,0)
        layout.addWidget(self.WebButton,2,1)
        layout.addWidget(self.CloudButton,3,0)
        layout.addWidget(self.ScanButton,4,0)
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
        performanceLabel = QtWidgets.QLabel("Console：")
        performanceEditor = QtWidgets.QLineEdit("目前显示的都是<信息>")
        planLabel = QtWidgets.QLabel("History Log：")
        self.planEditor = QtWidgets.QTextEdit()
        self.planEditor.setPlainText(self.LogText)
        layout.addRow(performanceLabel,performanceEditor)
        layout.addRow(planLabel,self.planEditor)
        self.formGroupBox.setLayout(layout)
    def setPlanEditor(self,msg):
        self.LogText =self.LogText + msg+ "\n"
        self.planEditor.setPlainText(self.LogText)
  
    
    def CreatWebTab(self):#穿件一个TAB 用于网络 现在占时定义为百度
        if self.webTabFlag == False:
            self.BaiduView = QWebEngineView(self.centralwidget)
            self.BaiduView.setMinimumSize(QtCore.QSize(500, 400))
            self.BaiduView.setUrl(QtCore.QUrl("https://www.baidu.com/"))
            self.BaiduView.setObjectName("search")
            self.WebTab=self.GraphTab.addTab(self.BaiduView,'百度 view')
            self.setPlanEditor('打开web 信息')
            self.webTabFlag = True
        elif self.webTabFlag == True:
            self.WebTab=self.GraphTab.removeTab(1)
            self.setPlanEditor('关闭web 信息')
            self.webTabFlag = False
    def webButtonAction(self): # 百度按钮的 动作
        self.webTabFlag=False
        self.WebButton.clicked.connect(self.CreatWebTab)
        
    def PatientButtonAction(self):
        self.PatientButton.clicked.connect(self.p.handle_click)
        self.setPlanEditor('打开Patient 信息')
        
class PatientLoginWindow(QtWidgets.QWidget):# 未完成 病人注册信息
    def __init__(self, parent=None):
        super(PatientLoginWindow, self).__init__(parent)
        self.resize(400, 400)
        self.setStyleSheet("background-color:rgba(255, 255, 255,220);")
        self.setWindowTitle('Patient Information Login')
        self.CreatLayoutBox()
        
    def CreatLayoutBox(self):
         self.mainLayout= QtWidgets.QVBoxLayout(self)
         
         self.informationLayout= QtWidgets.QGridLayout()
         self.massage=QtWidgets.QWidget()

         label=QtWidgets.QLabel()
         label.setText("Patient")
         #label.setFixedSize(400,20)
         #label.setScaledContents(True)
         self.mainLayout.addWidget(label)
         
         self.mainLayout.addLayout(self.informationLayout)
         self.mainLayout.addWidget(self.massage)
         self.mainLayout.setSpacing(2)
         self.mainLayout.setStretch(0,1)
         self.mainLayout.setStretch(1,20)
         self.mainLayout.setStretch(2,20)

         self.CrearPatientInf()

    def CrearPatientInf(self):
        self.NameLabel=QtWidgets.QLabel("Patient Name")
        self.NameEdit = QtWidgets.QLineEdit()
        self.NameEdit.setPlaceholderText('输入姓名')
        self.informationLayout.addWidget(self.NameLabel,0,0)
        self.informationLayout.addWidget(self.NameEdit,0,1)
        
        self.IDLabel=QtWidgets.QLabel("Patient ID")
        self.IDEdit = QtWidgets.QLineEdit()
        self.IDEdit.setPlaceholderText('输入ID')
        self.informationLayout.addWidget(self.IDLabel,1,0)
        self.informationLayout.addWidget(self.IDEdit,1,1)
        
        
        self.BirthLabel=QtWidgets.QLabel("Date of Birth")
        self.BirthDateEdit=QtWidgets.QDateEdit()
        strdate = time.strftime("%Y-%m-%d") #gets current time to put into dateedit
        #dateobj = datetime.strptime(curdate, "%Y-%m-%d")#converts to datetime object
        self.Qdate = QDate.fromString(strdate,"yyyy-MM-dd")
        self.BirthDateEdit.setDate(self.Qdate )
        self.informationLayout.addWidget(self.BirthLabel,2,0)
        self.informationLayout.addWidget(self.BirthDateEdit,2,1)
        self.
        
    def handle_click(self):
       
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()


        