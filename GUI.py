import sys
import db_management

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Create application')
        exitAct.triggered.connect(qApp.quit)

        addAct = QAction(QIcon('new_logo.png'), '&Add entry', self)
        addAct.setShortcut('Ctrl+E')
        addAct.setStatusTip('Create entry')
        addAct.triggered.connect(db_management.enter_new_entry)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        createMenu = menubar.addMenu('&Add entry')
        createMenu.addAction(addAct)

        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Database management')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
