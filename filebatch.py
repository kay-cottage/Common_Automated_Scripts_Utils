# -*- coding: utf-8 -*-
"""
Created on Tue 1 09:12:41 2022
@author: kayak
"""
import os
from shutil import copyfile


#文件批量增删查改
class batch(object):
    #有默认值放后
    def __init__(self,
                 dir_path,
                 Target_Dir_Path = None,
                 name='',
                 output_filename='output.txt',
                 fileType='.png',
                 fileType_list=['all'],
                 startNumber=0,
                 ):

        self.dir_path=dir_path
        self.name=name
        self.startNumber=startNumber
        self.fileType=fileType
        self.output_filename=output_filename
        self.fileType_list=fileType_list
        self.Target_Dir_Path = Target_Dir_Path

    #目标文件夹下按照自定义规则批量重命名文件
    def rename_with_num(self):
        count=0
        filelist=os.listdir(self.dir_path)
        for files in filelist:
            Olddir=os.path.join(self.dir_path,files)
            if os.path.isdir(Olddir):
                continue
            Newdir=os.path.join(self.dir_path,self.name+str(count+int(self.startNumber))+self.fileType)
            os.rename(Olddir,Newdir)
            count+=1
        print("rename successfully/共修改了"+str(count)+"个文件")


    #按照种类匹配删除
    def match_type_remove(self):
        count=0
        del_path_list = self.get_match_filetype_list()
        for del_path in del_path_list:
            os.remove(del_path)
            count+=1
        print('delete successfully!'+'共删除'+str(count)+'个文件')

    #按照文件名称关键字匹配删除
    def match_name_remove(self):
        count=0
        name_path_list = self.get_name_match_filelist
        for name_path in name_path_list:
            os.remove(name_path)
            count+=1
        print('delete successfully!'+'共删除'+str(count)+'个文件')

    #按照文件种类匹配复制到目标文件夹下
    def match_type_copy(self):
        count=0
        src_path_list = self.get_match_filetype_list()
        for src_path in src_path_list:
            src_filename = os.path.basename(src_path)
            copyfile(src_path,os.path.join(self.Target_Dir_Path,src_filename))
            count+=1
        print('copy successfully'+'共复制'+str(count)+'个文件')

    ##按照文件名称关键字匹配复制到目标文件夹下
    def match_name_copy(self):
        count=0
        src_path_list = self.get_name_match_filelist()
        for src_path in src_path_list:
            src_filename = os.path.basename(src_path)
            copyfile(src_path,os.path.join(self.Target_Dir_Path,src_filename))
            count+=1
        print('copy successfully'+'共复制'+str(count)+'个文件')
            
             
    #得到默认目录下所有文件路径并写入到.txt文件中   
    def get_filename_txt(self):
        file_list = []
        f = open(self.output_filename,"w")
        for root,dirs,files in os.walk(self.dir_path):
            for name in files:
                f.write(os.path.join(root,name)+'\n')
        f.close()


    def get_file_list(self):
        file_list = []
        for root,dirs,files in os.walk(self.dir_path):
            for name in files:
                file_list.append(os.path.join(root,name))
        return file_list


    def get_match_filetype_list(self):
        choosen_file_list = []
        file_list = self.get_file_list()
        if self.fileType_list==['all']:
            return file_list           

        else:
            try:
                for filetype in self.fileType_list:
                    for filepath in file_list:
                        if filetype in filepath:
                            choosen_file_list.append(filepath)
                return choosen_file_list
            except:
                print('参数错误/args wrong')


    def get_name_match_filelist(self):
        choosen_name_filelist=[]
        file_list = self.get_file_list()
        for choosen_name_file in file_list:
            if self.name in choosen_name_file:
                choosen_name_filelist.append(choosen_name_file)
        return choosen_name_filelist
            
        
