from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_postman import Ui_MainWindow
from ui.ui_dialogEditor import Ui_dialogEditor
import json
import urllib.request
import urllib.parse


class PostMan(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.setup_table()
        self.ui.btnAdd.clicked.connect(self.handle_add)
        self.ui.btnRemove.clicked.connect(self.handle_remove)
        self.ui.btnSend.clicked.connect(self.handle_send)
        self.ui.btnClear.clicked.connect(self.handle_clear)
        self.ui.textURL.setText("http://localhost:3000/")

    def setup_table(self):
        self.tModel = QStandardItemModel()
        self.tModel.setHorizontalHeaderLabels(['启用', '字段', '值'])
        self.tModel.itemChanged.connect(self.on_model_change)
        self.ui.table.setModel(self.tModel)

        self.tHeader = CheckBoxHeader([0], parent=self.ui.table)
        self.tHeader.clicked.connect(self.on_header_click)
        self.ui.table.setHorizontalHeader(self.tHeader)

        self.ui.table.setItemDelegateForColumn(
            0, ReadOnlyDelegate(self.ui.table))
        self.ui.table.setItemDelegateForColumn(
            1, LineEditDelegate(self.ui.table))
        self.ui.table.setItemDelegateForColumn(
            2, ReadOnlyDelegate(self.ui.table))

        self.ui.table.horizontalHeader().setStretchLastSection(True)
        self.ui.table.doubleClicked.connect(self.handle_edit)

        data = self.read_default_headers()
        for index, (key, value) in enumerate(data):
            item0 = QStandardItem()
            item0.setCheckable(True)
            self.tModel.appendRow(
                [item0, QStandardItem(key), QStandardItem(value)])

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

    def handle_remove(self):
        selected = self.ui.table.selectedIndexes()
        indexes = list(set(map(lambda x: x.row(), selected)))
        indexes.reverse()
        for index in indexes:
            self.tModel.removeRow(index)

    def handle_add(self):
        self.dEditor = DialogEditor()
        self.dEditor.newItem = True
        self.dEditor.accept_signal.connect(self.handle_accept)
        self.dEditor.show()
        self.dEditor.exec_()

    def handle_send(self):
        url = self.ui.textURL.text().strip()
        if not url:
            return
        if not url.startswith('http://') and not url.startswith('https://'):
            QMessageBox.warning(self, '错误', '请输入正确的协议名称')
            return
        method = self.ui.comboMethod.currentText()
        headers = {}
        for i in range(self.tModel.rowCount()):
            if self.tModel.item(i, 0).checkState() == Qt.Checked:
                key = self.tModel.item(i, 1).text().strip()
                value = self.tModel.item(i, 2).text().strip()
                headers[key] = value
        req = urllib.request.Request(url, method=method, headers=headers)
        res = urllib.request.urlopen(req).read().decode('utf-8')
        self.ui.textResp.insertPlainText(res)
        self.ui.textResp.moveCursor(QTextCursor.End)

    def handle_clear(self):
        self.ui.textResp.clear()

    def on_model_change(self):
        for i in range(self.tModel.columnCount()):
            checked = 0
            unchecked = 0
            for j in range(self.tModel.rowCount()):
                if self.tModel.item(j, i).checkState() == Qt.Checked:
                    checked += 1
                elif self.tModel.item(j, i).checkState() == Qt.Unchecked:
                    unchecked += 1

            if checked and unchecked:
                self.tHeader.updateCheckState(i, 2)
            elif checked:
                self.tHeader.updateCheckState(i, 1)
            else:
                self.tHeader.updateCheckState(i, 0)

    def on_header_click(self, index, state):
        for i in range(self.ui.table.model().rowCount()):
            item = self.tModel.item(i, index)
            item.setCheckState(Qt.Checked if state else Qt.Unchecked)


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
        key = self.ui.keyEdit.text().strip()
        value = self.ui.valueEdit.toPlainText().strip()
        if(not key):
            QMessageBox.warning(self, '警告', '字段名不能为空')
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
        if(not editor.text().strip()):
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


class CheckBoxHeader(QHeaderView):
    """自定义表头类"""
    # 自定义 复选框全选信号
    clicked = Signal(int, bool)
    # 这4个变量控制列头复选框的样式，位置以及大小
    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, column_index, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.setSectionsClickable(True)

        if isinstance(column_index, list) or isinstance(column_index, tuple):
            self.column_index = column_index
        elif isinstance(column_index, int):
            self.column_index = [column_index]
        else:
            raise RuntimeError('column_index must be a list, tuple or integer')

        self.isChecked = {}
        for column in self.column_index:
            self.isChecked[column] = 0

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height() - self._width) / 2.)

        if logicalIndex in self.column_index:
            option = QStyleOptionButton()
            option.rect = QRect(
                rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isChecked[logicalIndex] == 2:
                option.state |= QStyle.State_NoChange
            elif self.isChecked[logicalIndex]:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def updateCheckState(self, index, state):
        '''
        记录每个点击checkbox 状态及序号存入dict
        :param index: 
        :param state: 
        :return: 
        '''
        self.isChecked[index] = state
        self.viewport().update()

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 <= index < self.count():
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isChecked[index] == 1:
                    self.isChecked[index] = 0
                else:
                    self.isChecked[index] = 1
                self.clicked.emit(index, self.isChecked[index])
                self.viewport().update()
            else:
                super(CheckBoxHeader, self).mousePressEvent(event)
        else:
            super(CheckBoxHeader, self).mousePressEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    window = PostMan()
    window.show()
    app.exec_()
