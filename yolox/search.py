# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from DB import classesinfo



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + "db/pic_info.db/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '3542525234536365'

db = SQLAlchemy(app)




def get_classes_path():
    
    classes_dic = db.session.query(classesinfo.obj_class).all()
    #print(classes_dic)
    for i in classes_dic:
        print('i',i)


def get_classes_path1():
    classes_dic = classesinfo.query.filter_by(obj_class='car',obj_num=17).all()
    print(classes_dic)
    for i in classes_dic:
        print('i',i.obj_path)


get_classes_path()


