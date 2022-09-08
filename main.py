from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_postman import Ui_MainWindow

class PostMan(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

if __name__ == "__main__":
  app = QApplication([])
  window = PostMan()
  window.show()
  app.exec_()