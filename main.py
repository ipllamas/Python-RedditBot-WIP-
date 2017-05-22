#This program creates a UI from which to execute my reddit bot.
#The file required to log into reddit is not included, which prevents
#this program from being executed by others.

#When the file is included, the bot tracks a user's comment history and
#is able to reply to each of them, though this latter feature is currently
#disabled.

#Future goals of this personal project is to be able to configure the bot
#from the UI in order to do different tasks.


import sys
import reddit_bot
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtWidgets import QAction, QMessageBox

class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pyqt5 Tut')
        self.setWindowIcon(QIcon('redditIcon.jpg'))

        self.aboutWindow = otherWindow(self)

        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Leave The App")
        exitAction.triggered.connect(self.close_application)

        aboutAction = QAction("&About", self)
        aboutAction.setShortcut("Ctrl+A")
        aboutAction.setStatusTip("Open the About window")
        aboutAction.triggered.connect(self.openAbout)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(aboutAction)
        fileMenu.addAction(exitAction)
        
        self.home()
        
    def home(self):
        btn_bot = QPushButton("Run Bot", self)
        btn_bot.clicked.connect(self.create_bot)
        btn_bot.resize(btn_bot.sizeHint())
        btn_bot.move(200, 100)
        
        btn_exit = QPushButton("Quit", self)
        btn_exit.clicked.connect(self.close_application)
        #btn.resize(100, 50) #width x height
        btn_exit.resize(btn_exit.sizeHint()) 
        btn_exit.move(200, 200)


##TOOLBAR
##        extractAction = QAction(QIcon('redditIcon.jpg'), 'Exit', self)
##        extractAction.triggered.connect(self.close_application)
##
##        self.toolbar = self.addToolBar("Extraction")
##        self.toolbar.addAction(extractAction)

     
        self.show()

    def close_application(self):
        self.choice = QMessageBox.question(self,"Confirmation","Exit program?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if self.choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def create_bot(self):
        bot = reddit_bot.RedditBot()

    def openAbout(self):
        self.aboutWindow.show()

class otherWindow(QMainWindow):
    def __init__(self, parent=None):
        super(otherWindow, self).__init__(parent)

        self.setGeometry(80, 80, 500, 300)
        self.setWindowTitle('About')
        self.setWindowIcon(QIcon('redditIcon.jpg'))

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()


