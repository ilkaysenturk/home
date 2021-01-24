import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

def window():
    app = QApplication(sys.argv)
    #app.setStyle('Fusion')
    window = QWidget()
    window.setWindowTitle('ilkay')
    window.setGeometry(100, 100, 280, 80)
    window.move(60, 15)
    helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
    helloMsg.move(60, 15)
    window.show()
    sys.exit(app.exec_())
    e2 = QLineEdit()
    e2.setValidator(QDoubleValidator(0.99,99.99,2))

if __name__=='__main__':
    window()
