# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
import json
import os
import random
import sys
import json
sys.path.append("..") 
import batch


# make_label parm:路径列表，返回：路径列表/类别数量
def make_label(images_path_list):
    images_label_list=[]
    for images_path in images_path_list:
        images_label_list.append(os.path.dirname(images_path))
    return list(set(images_label_list)),len(list(set(images_label_list)))


# one-hot 形式下的标签
def make_label_index(images_path_list):
    f = open('classes.json')
    dic_classes = json.loads(f.read())
    classes_index_list = []
    for images_path in images_path_list:
        classes_index_list.append(dic_classes[os.path.dirname(images_path)])
    return classes_index_list
    


# 单类别下分离train,val
def single_class_split_train_val(images_path_list,scale=0.8):
    single_class_train_list=[]
    single_class_val_list=[]
    try:
        random_list=random.sample(range(0,len(images_path_list)),int(scale*len(images_path_list)))                         
        for index in random_list:
            single_class_train_list.append(images_path_list[index])
        single_class_val_list=list(set(images_path_list)-set(single_class_train_list))
        return single_class_train_list, single_class_val_list
                                  
    except:
        print('数据集数量不足，请补充数据')


# 多类别合并数据集,得到最终train,val数据集的列表
def get_train_val(dir_list,scale=0.8):
    b = batch.batch()
    train_list=[]
    val_list=[]
    for dir_name in dir_list:
        images_path_list = b.get_file_list(dir_name)
        single_class_train_list, single_class_val_list=single_class_split_train_val(images_path_list,scale=scale)
        train_list.append(single_class_train_list)
        val_list.append(single_class_val_list)
        
    return  [i for item in train_list for i in item],[i for item in val_list for i in item]
        



# txt to json 脚本 使用readline()读文件
def txt_to_json():
    classes_list = []
    f = open("classes.txt",encoding='utf-8')
    while True:
        line = f.readline()
        if line:
            classes_list.append(line.replace('\n',''))
        else:
            break
    f.close()

#0 1
def list_to_json(classes_list):
    classes_dic={}
    num = 0
    for i in classes_list:
        classes_dic[num]=i
        num = num+1
    f = open('classes1.json','w')
    f.write(json.dumps(classes_dic))
    f.close()

#1 0
def list_to_json_one(classes_list):
    classes_dic={}
    num = 0
    for i in classes_list:
        classes_dic[i]= num
        num = num+1
    f = open('classes.json','w')
    f.write(json.dumps(classes_dic))
    f.close()
    

def dic_classes(classes_list):
    list_to_json(classes_list)
    list_to_json_one(classes_list)
