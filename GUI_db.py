import sys
import db_management

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QMainWindow, QAction, qApp, QLineEdit, QLabel, QDateEdit


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 250))
        self.setWindowTitle("Database management")

        # Task Name
        self.taskNameLabel = QLabel(self)
        self.taskNameLabel.setText('Task Name:')
        self.taskNameLine = QLineEdit(self)

        self.taskNameLine.move(190, 55)
        self.taskNameLine.resize(200, 32)
        self.taskNameLabel.move(20, 50)

        # Task Category
        self.taskCategoryLabel = QLabel(self)
        self.taskCategoryLabel.setText('Category:')
        self.taskCategoryLine = QLineEdit(self)

        self.taskCategoryLine.move(190, 95)
        self.taskCategoryLine.resize(200, 32)
        self.taskCategoryLabel.move(20, 90)

        # Task Deadline
        self.taskDeadlineLabel = QLabel(self)
        self.taskDeadlineLabel.setText('Deadline (DD/MM/YY):')
        self.dateEdit = QDateEdit(self)

        self.dateEdit.move(190, 140)
        self.dateEdit.resize(200, 32)
        self.taskDeadlineLabel.move(20, 130)
        self.taskDeadlineLabel.resize(200, 50)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(185, 185)

        self.initUI()

    def getTaskName(self):
        taskName = self.taskNameLine.text()
        return taskName

    def getTaskCategory(self):
        taskCategory = self.taskCategoryLine.text()
        return taskCategory

    def getTaskDeadline(self):
        taskDeadline = self.DateEdit.date.toPyDate()
        return taskDeadline

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
        # Launch the method from db_management to create new entry
        # print('Your name: ', self.getTaskName(), self.getTaskCategory())
        db_management.enter_new_entry()
        print("hello")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
