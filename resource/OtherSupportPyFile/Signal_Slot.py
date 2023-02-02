import sys
from PySide6.QtWidgets import QApplication,QPushButton
from PySide6.QtCore import QObject,Signal,Slot,Qt
from PySide6.QtWidgets import QWidget

# def function():
#     print("The 'function' has been called")
#
# app=QApplication()
# button=QPushButton("Call function")
# button.clicked.connect(function)
# button.show()
# sys.exit(app.exec())

#
# class Communicate(QObject):
#     # 创建两个新的信号，一个用于处理整数类型，一个处理字符串类型
#     speak=Signal((int,),(str,))
#
#     def __init__(self,parent=None):
#         super(Communicate, self).__init__()
#         # 将 信号1 连接到 槽函数
#         self.speak[int].connect(self.say_something)
#         # 将 信号2 连接到 槽函数
#         self.speak[str].connect(self.say_something)
#
#     # 定义一个新的槽函数，将会接收一个整形或者一个字符串
#     # 并且打印他们的名字
#     @Slot(int)
#     @Slot(str)
#     def say_something(self,arg):
#         if isinstance(arg,int):
#             print("This is a number: ",arg)
#         elif isinstance(arg,str):
#             print("This is a String: ",arg)
#
# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     someone=Communicate()
#
#     # 发送带有不同参数的'speak'信号
#     # 当然，如果想要发射`str`类型的信号，必须指定，否则是以默认`int`类型进行的
#     someone.speak.emit(10)
#     someone.speak[str].emit("Hello everybody")

class Button(QWidget):

    clicked=Signal(Qt.MouseButton)

    def __init__(self):
        super(Button, self).__init__()
        # 绑定信号与槽
        self.clicked.connect(self.PrintE)

    @Slot()
    def PrintE(self,arg):
        print(arg)

    def mousePressEvent(self,event):
        # 鼠标移动时，作为触发器发出信号
        self.clicked.emit(event.button())

App=QApplication()
button=Button()
button.show()
sys.exit(App.exec())
