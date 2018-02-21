from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
import sys
class App(QWidget):
 
    def __init__(self,game):
        super().__init__()
        self.title = 'Tou0ou - PROTOTYPE VERSION 0.1aB'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.setCentralWidget(ImageWidget(surface))
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
def tou0ouBuild(game):
    app = QApplication(sys.argv)
    ex = App(game)
    sys.exit(app.exec_())
