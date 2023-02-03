from PyQt6 import QtCore, QtGui, QtWidgets
import pyperclip


class Ui_MainWindow(object):
    def __init__(self):
        self.comboData_3 = ['km','m','cm','mm','μm','nm']
        self.comboData_2 = ['km','m','cm','mm','μm','nm']
        return

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 180)
        
        #centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        #comboboxes
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 141, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['Lenght','Mass','Time'])
        self.comboBox.currentTextChanged.connect(self.unitChange)
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 120, 141, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(self.comboData_2)
        
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(400, 80, 141, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(self.comboData_3)


        #textboxes
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 40, 181, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        #buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 40, 81, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.convert)
        self.pushButton.isDefault()
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360,120,181,21))
        self.pushButton_2.setObjectName('pushButton_2')
        self.pushButton_2.clicked.connect(self.copyClip)
        

        #labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 47, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 80, 41, 21))
        self.label_3.setObjectName("label_3")
        
        
        #statusbar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #?
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))
        self.pushButton_2.setText(_translate("MainWindow", "Copy to clipboard"))
        self.label.setText(_translate("MainWindow", "Type"))
        self.label_2.setText(_translate("MainWindow", "Unit"))
        self.label_3.setText(_translate("MainWindow", "Unit"))


    def unitChange(self):
        if self.comboBox.currentText() == 'Mass':
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_2.addItems(['kg','g','mg'])
            self.comboBox_3.addItems(['kg','g','mg'])
        elif self.comboBox.currentText() == 'Lenght':
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_2.addItems(['km','m','cm','mm','μm','nm'])
            self.comboBox_3.addItems(['km','m','cm','mm','μm','nm'])
        else:
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_2.addItems(['h','min','s','ms'])
            self.comboBox_3.addItems(['h','min','s','ms'])

    def convert(self):
        self.unit_dict = {
            'km': 1000,
            'm': 1,
            'cm': 0.1,
            'mm': 0.001,
            'kg': 1000,
            'g': 1,
            'mg': 0.001,
            's': 1,
            'min': 60,
            'h': 3600,
            'ms': (1/1000),
            'μm': (1/1000000),
            'nm': (1/1000000000)
        }
        def calculate(self):
            try:
                return (float(self.unit_dict[self.comboBox_2.currentText()])) /\
                    (float(self.unit_dict[self.comboBox_3.currentText()])) *\
                    (float(self.lineEdit.text()))
            except ValueError:
                return ''
        self.lineEdit_2.clear()
        self.lineEdit_2.setText(str(calculate(self)))
    
    def copyClip(self):
        if self.lineEdit_2.text() == '':
            return
        else:
            pyperclip.copy(self.lineEdit_2.text())
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())