import pandas as pd
import numpy as np


path=r"../OtherFile"

wordsDir=[
    ["0",["呼啦圈"]],
    ["1",["蜡烛"]],
    ["2",["天鹅"]],
    ["3", ["耳朵"]],
    ["4", ["旗子"]],
    ["5", ["钩子"]],
    ["6", ["汤勺"]],
    ["7", ["镰刀"]],
    ["8", ["葫芦"]],
    ["9", ["哨子"]],
    ["10", ["石头"]],
    ["11", ["梯子"]],
    ["12", ["椅儿"]],
    ["13", ["医生"]],
    ["14", ["钥匙"]],
    ["15", ["鹦鹉"]],
    ["16", ["石榴"]],
    ["17", ["仪器"]],
    ["18", ["糖葫芦"]],
    ["19", ["狮鹫"]],
    ["20", ["恶灵"]],
    ["21", ["鳄鱼"]],
    ["22", ["三三娘"]],
    ["23", ["和尚"]],
    ["24", ["闹钟"]],
    ["25", ["二胡"]],
    ["26", ["河流"]],
    ["27", ["耳机"]],
    ["28", ["恶霸"]],
    ["29", ["二球"]],
    ["30", ["三轮车"]],
    ["31", ["鲨鱼"]],
    ["32", ["扇儿"]],
    ["33", ["三三娘"]],
    ["34", ["三尸"]],
    ["35", ["珊瑚"]],
    ["36", ["山路"]],
    ["37", ["山鸡王"]],
    ["38", ["妇女"]],
    ["39", ["山丘"]],
    ["40", ["司令"]],

]

w=pd.DataFrame(wordsDir)
w.to_csv(path+"/EDB.csv")