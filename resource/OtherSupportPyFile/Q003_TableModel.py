from PySide6.QtCore import Qt,QAbstractTableModel,QModelIndex
from PySide6.QtGui import QColor

class CustomTableModel(QAbstractTableModel):
    def __init__(self,data=None):
        super(CustomTableModel, self).__init__()
        self.load_data(data)

    def load_data(self,data):
        # 获取UTC日期
        self.input_dates=data[0].values
        # 获取震级
        self.input_magnitudes=data[1].values

        self.column_count=2
        self.row_count=len(self.input_dates)

    def rowCount(self, parent=QModelIndex()):
        # parent需要获取Qt模型索引
        return self.row_count
    def columnCount(self, parent=QModelIndex()):
        # parent需要获取Qt模型索引
        return self.column_count
    def headerData(self,section,orientation,role):
        # 头文件信息
        if role!=Qt.DisplayRole:
            return None
        if orientation==Qt.Horizontal:
            return ("Date","Magnitude")[section]
        else:
            return f"{section}"

    def data(self,index,role=Qt.DisplayRole):
        # 需要实现的抽象方法
        # index是索引位置，role是当前状态

        column=index.column()
        row=index.row()

        if role==Qt.DisplayRole:
            # 如果当前在显示
            if column==0:
                # 表示当前的位置为： row,0 理应返回date数据
                # 返回str格式的数据，除了时区
                date=self.input_dates[row].toPython()
                return str(date)[:-3]
            elif column==1:
                # 返回震级数据
                magnitude=self.input_magnitudes[row]
                return f"{magnitude:.2f}"

        elif role==Qt.BackgroundRole:
            # 在背后的话就返回一个颜色
            return QColor(Qt.white)
        elif role==Qt.TextAlignmentRole:
            return Qt.AlignRight
        return None

