# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qr_code_generator1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.qrButton = QtWidgets.QPushButton(self.centralwidget)
        self.qrButton.setGeometry(QtCore.QRect(180, 180, 121, 41))
        self.qrButton.setObjectName("qrButton")
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(109, 10, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_text.setFont(font)
        self.input_text.setObjectName("input_text")
        self.qrCodeImage = QtWidgets.QLabel(self.centralwidget)
        self.qrCodeImage.setGeometry(QtCore.QRect(140, 240, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qrCodeImage.setFont(font)
        self.qrCodeImage.setFrameShape(QtWidgets.QFrame.Box)
        self.qrCodeImage.setObjectName("qrCodeImage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 470, 201, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.qrButton.clicked.connect(self.generateQR)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR Code Generator"))
        self.qrButton.setText(_translate("MainWindow", "Generate_QR_Code"))
        self.qrCodeImage.setText(_translate("MainWindow", "                 QR_Code"))
        self.label.setText(_translate("MainWindow", "Developer: Satish Kushwah"))

    def generateQR(self):
        img = qrcode.make(self.input_text.toPlainText())
        img.save("myQR.jpg")
        pixmap = QtGui.QPixmap("myQR.jpg","1") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.qrCodeImage.width(), self.qrCodeImage.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.qrCodeImage.setPixmap(pixmap) # Set the pixmap onto the label
        self.qrCodeImage.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

