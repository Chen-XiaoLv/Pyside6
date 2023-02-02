from PySide6.QtCore import Slot
from PySide6.QtGui import QAction,QKeySequence
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self,widget):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Earquakes Information")
        self.setCentralWidget(widget)

        # 设置菜单栏
        self.menu=self.menuBar()
        # 添加 文件 菜单项
        self.file_menu=self.menu.addMenu("文件")

        # 退出事件
        exit_action = QAction("Exit", self)  # 设置名字
        exit_action.setShortcut(QKeySequence.Quit)  # 设置快捷键
        exit_action.triggered.connect(self.close)  # 该事件直接与close函数关联

        self.file_menu.addAction(exit_action)

        # 状态栏
        self.status=self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        # 窗口尺寸
        geometry=self.screen().availableGeometry()
        self.setFixedSize(geometry.width()*0.8,geometry.height()*0.7)
