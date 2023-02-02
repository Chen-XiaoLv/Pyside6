from chatgpt_wrapper import ChatGPT
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
import time
import os
from qt_material import apply_stylesheet
# import subprocess as sp

# init
# try:
#    sp.Popen("ChatGPT install")
# except:
#    print("the FireFox is already running in your computer, plz shut it up, or just input 'ChatGPT install' in your Terminal)")
#    sys.exit()

# preworking: input ChatGPT in your Terminal
# bot=ChatGPT()
# with open("./resource/Setting.txt",'r',encoding='utf-8') as f:
#    setting=f.readlines()[0]
# print("请稍等，伊雷娜正在赶来的路上~")
# c=bot.ask(setting)

loader=QUiLoader()

app=QtWidgets.QApplication(sys.argv)
window=loader.load("./resource/UI/ChatBot_001.ui",None)
window.Button1.text="开始聊天吧！"

apply_stylesheet(app,theme='dark_teal.xml')

window.label.setPixmap(QPixmap(r"resource/Img/yln_01.png"))
window.label.setScaledContents (True)

@Slot()
def do_something():
   A=window.Edit1.toPlainText()
   window.Browser1.setPlainText("正在发送信息，请不要走开哦")
   window.Button1.text="请稍等~"
   # ans=bot.ask(A)
   # window.Browser1.setPlainText(ans)
   # window.Button1.text="开始聊天吧！"
   # window.Edit1.clear()

window.Button1.clicked.connect(do_something)
window.show()
app.exec()




