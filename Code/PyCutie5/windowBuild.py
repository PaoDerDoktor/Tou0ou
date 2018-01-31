from PyQt5.QtWidgets import QWidget
import sys
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Tou0ou - PROTOTYPE VERSION 0.1aB'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
def tou0ouBuild():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
