import PySide6
from PySide6 import QtGui,QtWidgets,QtCore
from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QImage,QIcon,QFont
import sys
from PySide6.QtCore import Slot,Signal
import time
from qt_material import apply_stylesheet
import pandas as pd
import random
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput,QSoundEffect
from PySide6 import QtGui,QtCore,QtWidgets
EDB=pd.read_csv(r"../OtherFile/EDB.csv")


Language=["中文","英文"]
L=Language[0]
t=time.time()
idx=random.randint(0,EDB.shape[0]-1)
a=0
cor=0
mis=0

app=PySide6.QtWidgets.QApplication(sys.argv)
apply_stylesheet(app,theme='dark_teal.xml')

loader = QUiLoader()
ui = loader.load("../UI/Q005_Main.ui", None)
ui.setWindowTitle("伊蕾娜的英语科目一")
ui.setWindowIcon(QIcon(r"..\Img\yln_02.png"))



@ Slot()
def send():
    global a,mis,cor,idx,ui
    text = ui.edit1.toPlainText().strip()
    if (v := check(text,idx)) == 1:
        cor += 1
        statebar.showMessage(f"您已经学习了{(time.time() - t) // 60}分钟！完成了{cor}道题目！")
        random.seed(time.time())
        idx = random.randint(0, EDB.shape[0] - 1)
        ui.label2.setText(f"  {EDB.iloc[idx, 1]}  ")
        ui.edit1.clear()
        a += 1
    elif v == -1:
        mis += 1
        statebar.showMessage(f"您已经学习了{(time.time() - t) // 60}分钟！完成了{cor}道题目！")
        defaultButton = QMessageBox.NoButton
        # result = QMessageBox.question(self, dlgTitle, strText, QMessageBox.Yes | QMessageBox.No, defaultButton)
        QtWidgets.QMessageBox.question(ui, "诶嘿", "抱歉，您答错啦", QMessageBox.Yes, defaultButton)
        ui.edit1.clear()
        a += 1
    elif v == 0:
        statebar.showMessage(f"您已经学习了{(time.time() - t) // 60}分钟！完成了{cor}道题目！")
        defaultButton = QMessageBox.NoButton
        # result = QMessageBox.question(self, dlgTitle, strText, QMessageBox.Yes | QMessageBox.No, defaultButton)
        QtWidgets.QMessageBox.question(ui, "诶嘿", "咦，您似乎什么也没写呢", QMessageBox.Yes, defaultButton)


def check(text,idx):
    if not text:
        return 0
    for i in eval(EDB.iloc[idx,2]):
        if i==text:
            return 1
    return -1

    # MainWindow.button1.clicked.connect(sound.play)
ui.label1.setText(f"请写出所给单词的{L}形式~")
ui.label2.setText(f"  {EDB.iloc[idx, 1]}  ")
statebar = ui.statusBar()
statebar.showMessage(f"您已经学习了{(time.time() - t) // 60}分钟！完成了{cor}道题目！")
ui.button1.clicked.connect(send)

ui.show()


ui.show()

sys.exit(app.exec())