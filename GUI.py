import sys
import db_management

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QMainWindow, QAction, qApp, QLineEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 200))
        self.setWindowTitle("Database management")

        # Task Name
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Task Name:')
        self.line = QLineEdit(self)
        taskName = self.line.text()

        self.line.move(135, 50)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 50)

        # Task Category
        nameLabel = QLabel(self)
        nameLabel.setText('Task Category:')
        line = QLineEdit(self)
        taskCategory = self.line.text()

        self.line.move(135, 90)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 90)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(135, 130)

        self.initUI()

        print('Your name: ' + self.line.text())

    def initUI(self):
        exitAct = QAction(QIcon('exit.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        deleteAct = QAction(QIcon('exit.jpg'), '&Delete table', self)
        deleteAct.setStatusTip('Delete table')
        deleteAct.triggered.connect(db_management.delete_table)

        dropAct = QAction(QIcon('exit.jpg'), '&Drop table', self)
        dropAct.setStatusTip('Drop table')
        dropAct.triggered.connect(db_management.drop_table)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        fileMenu.addAction(deleteAct)
        fileMenu.addAction(dropAct)

    def clickMethod(self):
        print('Your name: ' + self.line.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
