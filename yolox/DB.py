# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + "db/pic_info.db/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '35425245436365'

db = SQLAlchemy(app)

# 类别详情
class classesinfo(db.Model):
    __tablename__ = "classesinfo"
    obj_id = db.Column(db.Integer, primary_key=True)  # id号(独一无二的)
    obj_path = db.Column(db.String(1024), nullable=False)
    obj_class = db.Column(db.String(2048), nullable=False)  
    obj_num = db.Column(db.Integer, primary_key=True)


#if __name__ == "__main__":
    #db.create_all()
  
