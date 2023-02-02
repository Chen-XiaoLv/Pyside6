from PySide6.QtWidgets import (QHBoxLayout,QHeaderView,QSizePolicy,QTableView,QWidget)
from .Q003_TableModel import CustomTableModel
from PySide6.QtCharts import QChart,QChartView,QLineSeries,QDateTimeAxis,QValueAxis
from PySide6.QtGui import QPainter
from PySide6.QtCore import QDateTime,Qt


class Widget(QWidget):
    def __init__(self,data):
        super(Widget, self).__init__()

        # 获取TableModel
        self.model=CustomTableModel(data) # 基于TableModel的数据读取

        # 创建表视图
        self.table_view=QTableView()
        self.table_view.setModel(self.model) # 设置模型

        # 设置表视图的标头
        self.horizontal_header=self.table_view.horizontalHeader()
        self.vertical_header=self.table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(
            QHeaderView.ResizeToContents
        )# 依据内容自动设置尺寸
        self.vertical_header.setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.horizontal_header.setStretchLastSection(True) # 拉伸部件

        # 创建QChart对象
        self.chat=QChart()
        self.chat.setAnimationOptions(QChart.AllAnimations) # 设置移动动画
        self.add_series("Magnitude")

        # 创建表视图
        self.chat_view=QChartView(self.chat)
        self.chat_view.setRenderHint(QPainter.Antialiasing) # 抗锯齿


        # 设置布局
        self.main_layout=QHBoxLayout()
        size=QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred) # 默认sizeHint()为最优尺寸的策略

        # 左布局
        size.setHorizontalStretch(1) # 设置水平拉伸因子为1
        self.table_view.setSizePolicy(size) # 对组件应用尺寸策略
        self.main_layout.addWidget(self.table_view) # mainlayout是一个水平布局盒子，将我们的组件加进来

        # 右布局
        size.setHorizontalStretch(4)
        self.chat_view.setSizePolicy(size)
        self.main_layout.addWidget(self.chat_view)

        # 将布局设置到QWidget中
        self.setLayout(self.main_layout) # 最后，将我们的水平盒子设为小组件的布局

    def add_series(self,name):
        # 创建线序列QLineSeries
        self.series=QLineSeries()
        self.series.setName(name)

        # 填充QLineSeries
        for i in range(self.model.row_count):

            t=self.model.index(i,0).data()
            data_fmt="yyyy-MM-dd HH:mm:ss.zzz"
            x=QDateTime().fromString(t,data_fmt).toSecsSinceEpoch() # 转化为时间戳
            y=float(self.model.index(i,1).data())
            if x>0 and y>0:
                self.series.append(x,y)

        self.chat.addSeries(self.series)

        # 设置图样式
        # 设置x坐标
        self.axis_x=QDateTimeAxis()
        self.axis_x.setTickCount(10) # 设置间隔
        # self.axis_x.setFormat("dd.MM (h:mm)") # 设置时间显示
        self.axis_x.setFormat("MM.dd") # 设置时间显示
        self.axis_x.setTitleText("Date")
        self.chat.addAxis(self.axis_x,Qt.AlignBottom) # 在表格中加入坐标，位置为底部
        self.series.attachAxis(self.axis_x) # 自动让QLineSeries贴附

        # 设置y坐标
        self.axis_y=QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Magnitude")
        self.chat.addAxis(self.axis_y,Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        # 从Chart上获取颜色，并在QTableView上使用
        color_name=self.series.pen().color().name()
        self.model.color=f"{color_name}"
