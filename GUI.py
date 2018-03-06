# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:29:10 2018

@author: 310128142
"""

from qtpy.QtWidgets import QTreeWidgetItem,QMenu,QApplication,QAction,QMainWindow
from qtpy import QtGui,QtWidgets,QtCore
from qtpy.QtCore import Qt,QUrl,QDate
from main_layout import MainWindow_UI
import sys

class mywindow(QMainWindow):
    def __init__(self,parent = None):
        super(mywindow,self).__init__(parent)
        self.ui=MainWindow_UI()
        self.ui.setupUi(self)
def main():

    app = QtWidgets.QApplication(sys.argv)
    widows =mywindow()
    #label= QtWidgets.QLabel(widows)
    #label.setText("GUI")
      

    widows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
