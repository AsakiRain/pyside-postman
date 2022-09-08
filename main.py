from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_postman import Ui_MainWindow
from ui.ui_dialogEditor import Ui_dialogEditor
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
        self.ui.table.doubleClicked.connect(self.handle_edit)
        self.ui.table.setItemDelegateForColumn(
            0, ReadOnlyDelegate(self.ui.table))
        self.ui.table.setItemDelegateForColumn(
            1, LineEditDelegate(self.ui.table))
        self.ui.table.setItemDelegateForColumn(
            2, ReadOnlyDelegate(self.ui.table))

    def read_default_headers(self):
        file = open('default_headers.json', 'r')
        data = json.loads(file.read())
        return data.items()

    def handle_edit(self, index: QModelIndex):
        if(index.column() == 2):
            self.dEditor = DialogEditor()
            self.dEditor.show()
            key_index = QModelIndex(index.model().index(index.row(), 1))
            value_index = QModelIndex(index.model().index(index.row(), 2))
            key = index.model().data(key_index)
            value = index.model().data(value_index)

            self.dEditor.key_index = key_index
            self.dEditor.value_index = value_index
            self.dEditor.setValue(key, value)
            self.dEditor.accept_signal.connect(self.handle_accept)
            self.dEditor.exec_()

    def handle_accept(self, key, value):
        if(self.dEditor.newItem):
            item0 = QStandardItem()
            item0.setCheckable(True)
            self.tModel.appendRow(
                [item0, QStandardItem(key), QStandardItem(value)])
        else:
            self.tModel.setData(self.dEditor.key_index, key)
            self.tModel.setData(self.dEditor.value_index, value)


class DialogEditor(QDialog):
    accept_signal = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.newItem = False
        self.key_index: QModelIndex = None
        self.value_index: QModelIndex = None
        self.ui = Ui_dialogEditor()
        self.ui.setupUi(self)

    def accept(self):
        key = self.ui.keyEdit.text()
        value = self.ui.valueEdit.toPlainText()
        if(not key or not value):
            QMessageBox.warning(self, '警告', '字段不能为空')
        else:
            self.accept_signal.emit(key, value)
            return super().accept()

    def reject(self):
        return super().reject()

    def setValue(self, key, value):
        self.ui.keyEdit.setText(key)
        self.ui.valueEdit.setText(value)


class ReadOnlyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(ReadOnlyDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        return None


class LineEditDelegate(QItemDelegate):
    def __init__(self, parent):
        super(LineEditDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        LineEdit = QLineEdit(parent)
        return LineEdit

    def setEditorData(self, editor, index):
        self.oText = index.model().data(index)
        editor.setText(self.oText)

    def setModelData(self, editor, model, index):
        if(not editor.text()):
            QMessageBox.warning(self.parent(), '警告', '字段不能为空')
            model.setData(index, self.oText)
        else:
            model.setData(index, editor.text())


class SpinBoxDelegate(QItemDelegate):
    def __init__(self, parent, uint):
        QItemDelegate.__init__(self, parent)
        self.suffix = uint

    # 创建控件并设置控件的最大和最小输入值及后缀
    def createEditor(self, parent, option, index):
        spinbox = QSpinBox(parent)
        spinbox.setMaximum(999)
        spinbox.setMinimum(0)
        spinbox.setSuffix(self.suffix)
        return spinbox

    # 设置控件数值
    def setEditorData(self, editor, index):
        if(index.model().data(index) == ''):
            editor.setValue(0)
        else:
            text = index.model().data(index).split(' ')[0]
            editor.setValue(float(text))

        # 设置更改数值后，单元格的数值
    def setModelData(self, editor, model, index):
        model.setData(index, str(editor.value()) + str(' ') + self.suffix)


if __name__ == "__main__":
    app = QApplication([])
    window = PostMan()
    window.show()
    app.exec_()
