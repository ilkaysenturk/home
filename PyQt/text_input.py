import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QApplication,QFormLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

def window():
   app = QApplication(sys.argv)
   app.setStyle('Fusion')
   win = QWidget()
   flo = QFormLayout()
   e4 = QLineEdit()
   e4.textChanged.connect(textchanged)
   flo.addRow("Text changed",e4)

   e5 = QLineEdit()
   e5.setEchoMode(QLineEdit.Password)
   flo.addRow("Password",e5)

   e6 = QLineEdit("Hello Python")
   e6.setReadOnly(True)
   flo.addRow("Read Only",e6)

   e5.editingFinished.connect(enterPress)
   win.setLayout(flo)
   win.setWindowTitle("PyQt")
   win.show()

   sys.exit(app.exec_())

def textchanged(text):
   print ("contents of text box: "+text)

def enterPress():
   print ("edited")

if __name__ == '__main__':
   window()
