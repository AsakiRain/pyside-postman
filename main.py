from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_postman import Ui_MainWindow
import json


class PostMan(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.setup_table()

    def setup_table(self):
        self.tModel = QStandardItemModel()
        self.tModel.setHorizontalHeaderLabels(['启用', '字段', '值'])

        data = self.read_default_headers()
        for index, (key, value) in enumerate(data):
            item0 = QStandardItem()
            item0.setCheckable(True)
            self.tModel.appendRow(
                [item0, QStandardItem(key), QStandardItem(value)])
        self.ui.table.setModel(self.tModel)
        self.ui.table.setItemDelegateForColumn(
            0, ReadOnlyDelegate(self.ui.table))

    def read_default_headers(self):
        file = open('default_headers.json', 'r')
        data = json.loads(file.read())
        return data.items()
class ReadOnlyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(ReadOnlyDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        return None

if __name__ == "__main__":
    app = QApplication([])
    window = PostMan()
    window.show()
    app.exec_()
