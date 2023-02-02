import argparse
import pandas as pd
from PySide6.QtCore import QDateTime,QTimeZone
from PySide6.QtWidgets import QApplication
from resource.OtherSupportPyFile.Q003_DataProcess import MainWindow
from resource.OtherSupportPyFile.Q003_Table import Widget
import sys
from qt_material import apply_stylesheet


def transform_date(utc,timezone=None):
    # 日期转换
    utc_fmt="yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date=QDateTime().fromString(utc,utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date

def read_data(file):
    # 读取数据
    data=pd.read_csv(file)
    # 处理震级
    data=data.drop(data[data['mag']<0].index)
    magnitudes=data['mag']
    # 时区设置
    timezone = QTimeZone(QTimeZone.systemTimeZone()) # "Asia/Shanghai"
    # 时间转换
    times=data['time'].apply(lambda x:transform_date(x,timezone))
    return times,magnitudes


if __name__ == '__main__':
    options=argparse.ArgumentParser()
    options.add_argument("-f","--file",type=str,required=True)
    args=options.parse_args()
    data=read_data(args.file)
    # 创建应用程序
    app=QApplication()
    widget=Widget(data)
    window=MainWindow(widget)
    window.show()
    apply_stylesheet(app,theme='dark_teal.xml')

    sys.exit(app.exec())