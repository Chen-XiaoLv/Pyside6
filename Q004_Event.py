import sys
import PySide6
from PySide6.QtCore import QEvent,Qt,QObject
from PySide6 import QtCore,QtWidgets,QtGui
from PySide6.QtWidgets import QWidget,QApplication,QMessageBox
from PySide6.QtGui import QPainter,QPixmap


class Widget(object):
    def setupUi(self,widget):
        widget.setObjectName("Widget")
        widget.resize(930,1342)

        self.label=QtWidgets.QLabel(widget) # 设置Parent，即父对象
        self.label.setGeometry(QtCore.QRect(130,256,241,21))
        self.label.setObjectName("label")

        self.button1=QtWidgets.QPushButton(widget)
        self.button1.setGeometry(QtCore.QRect(104,130,161,23))
        self.button1.setObjectName("button1")

        self.button2 = QtWidgets.QPushButton(widget)
        self.button2.setGeometry(QtCore.QRect(110, 180, 151, 23))
        self.button2.setObjectName("button2")
        self.RetranslateUi(widget)
        # 用于自动匹配信号与槽！
        # 关于槽函数，需要写作：
        # on_子对象名_信号名
        # 例如：
        # on_button1_clicked()
        # QtCore.QMetaObject.connectSlotsByName(widget)


    def RetranslateUi(self,widget):
        _translate=QtCore.QCoreApplication.translate
        # Qt自带的文本翻译
        widget.setWindowTitle(_translate("Widget","窗体"))
        self.label.setText(_translate("Widget","鼠标当前的位置是： "))
        self.button2.setText(_translate("Widget","Button_moveEvent"))
        self.button1.setText(_translate("Widget","Button_resizeEvent"))


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui=Widget()
        self.ui.setupUi(self)

    def resizeEvent(self,event):
    # 组件改变大小事件
        H=self.height()
        W=self.width()
        Hbtn=self.ui.button1.height()
        Wbtn=self.ui.button1.width()
        self.ui.button1.setGeometry((W-Wbtn)>>1,(H-Hbtn)>>1,
                                    Wbtn,Hbtn)

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        pt=event.pos()
        self.ui.label.setText(f"鼠标当前位置是: x:{pt.x()} y:{pt.y()}")
        super().mouseMoveEvent(event)

    # 自定义键盘按下事件
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        rect=self.ui.button2.geometry()
        if (k:=event.key()) in set([Qt.Key.Key_4,Qt.Key.Key_Left]):
            rect.setLeft(rect.left()-50)
            rect.setRight(rect.right()-50)
        elif k in set([Qt.Key.Key_8,Qt.Key.Key_Up]):
            rect.setTop(rect.top()-50)
            rect.setBottom(rect.bottom()-50)
        elif k in set([Qt.Key.Key_6,Qt.Key.Key_Right]):
            rect.setLeft(rect.left()+50)
            rect.setRight(rect.right()+50)
        elif k in set([Qt.Key.Key_2, Qt.Key.Key_Down]):
            rect.setTop(rect.top() + 50)
            rect.setBottom(rect.bottom()+50)
        self.ui.button2.setGeometry(rect)

    # 重绘触发事件
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        paint=QPainter(self)
        img=PySide6.QtGui.QImage("resource/Img/yln_01.png")
        paint.drawImage(img.rect(),img)
        super().paintEvent(event)

    # 窗口关闭事件
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        dlgTitle="Dialogue"
        strText="Will you exit?"
        defaultButton=QMessageBox.NoButton
        result=QMessageBox.question(self,dlgTitle,strText,QMessageBox.Yes|QMessageBox.No,defaultButton)
        if result==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




if __name__ == '__main__':
    app=QApplication(sys.argv)
    btnevent=MyWidget()
    btnevent.show()
    sys.exit(app.exec())