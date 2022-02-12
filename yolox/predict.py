# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
import re
import time
import cv2
import numpy as np
from PIL import Image
from yolox.yolo import YOLO
from yolox.grabscreen import grab_screen

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from yolox.DB import classesinfo
import sys 
sys.path.append("..") 
import batch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + "db/pic_info.db/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '3542525234536365'

db = SQLAlchemy(app)





def dectect(rezize_tuple=(416,277)):
    yolo = YOLO()
    
    while(True):
        frame = grab_screen()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame,rezize_tuple)
            # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
            # 进行检测
        frame,label_list = yolo.detect_image(frame)
        frame = np.array(frame)
        if label_list != []:
            for label in label_list:
                print(label_list)
            
            # RGBtoBGR满足opencv显示格式
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        cv2.imshow('yolox_detect',frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    
    cv2.waitKey()# 视频结束后，按任意键退出
    cv2.destroyAllWindows()

#[[]]>>>{}
def transf_label(label_list):
    obj_list=[]
    obj_dic = {}
    if label_list != []:
        for i in range(len(label_list)):
            obj_list.append(re.sub(r'[0-9]+','',str(label_list[i][0],'utf-8')).strip('.').strip())
        for i in obj_list:
            obj_dic[i]=obj_list.count(i)
        return obj_dic
    else:
        return None

            
            
    
def dir_detect_db(dir_path):
    yolo = YOLO()
    b = batch.batch()
    obj_id =0
    img_path_list = b.get_file_list(dir_path=dir_path,current_dir=False)
    for img_path in img_path_list:
        image = Image.open(img_path)
        frame,label_list = yolo.detect_image(image)
        print(img_path,label_list)
        if label_list != []:
            obj_dic=transf_label(label_list)
            for i in obj_dic:
                classes_info = classesinfo(obj_id=obj_id,obj_path=img_path,obj_class=i,obj_num=int(obj_dic[i]))
                db.session.add(classes_info)
                db.session.commit()
                obj_id+=1


def get_classes_path():
    for keyword in keyword_list:
        classes_dic = classesinfo.query.filter(classesinfo.obj_class=='person')
        print(classes_dic)
        for i in classes_dic:
            print(i)
        
        
        
            

        
        
        
    

