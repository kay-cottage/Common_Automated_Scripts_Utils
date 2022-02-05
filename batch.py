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
                 startNumber=0,
                 ):


        self.startNumber=startNumber


    #目标文件夹下按照自定义规则批量重命名文件
    def rename_with_num(self,dir_path,name='',fileType='.png'):
        count=0
        filelist=os.listdir(dir_path)
        for files in filelist:
            Olddir=os.path.join(dir_path,files)
            if os.path.isdir(Olddir):
                continue
            Newdir=os.path.join(dir_path,name+str(count+int(self.startNumber))+fileType)
            os.rename(Olddir,Newdir)
            count+=1
        print("rename successfully/共修改了"+str(count)+"个文件")



    #按照种类匹配删除
    def match_remove(self,dir_path,name=None,fileType_list=['all']):
        count=0
        del_path_list = self.get_name_filetype_match_filelist(dir_path,name,fileType_list)
        for del_path in del_path_list:
            os.remove(del_path)
            count+=1
        print('delete successfully!'+'共删除'+str(count)+'个文件')


    #按照文件种类匹配复制到目标文件夹下
    def match_copy(self,dir_path,Target_Dir_Path,name=None,fileType_list=['all']):
        count=0
        src_path_list = self.get_name_filetype_match_filelist(dir_path,name,fileType_list)
        for src_path in src_path_list:
            src_filename = os.path.basename(src_path)
            copyfile(src_path,os.path.join(Target_Dir_Path,src_filename))
            count+=1
        print('copy successfully'+'共复制'+str(count)+'个文件')

             

    #得到默认目录下所有文件路径并写入到.txt文件中   
    def get_filename_txt(self,dir_path,output_filename='output.txt'):
        file_list = []
        f = open(output_filename,"w")
        for root,dirs,files in os.walk(dir_path):
            for name in files:
                f.write(os.path.join(root,name)+'\n')
        f.close()


    def get_file_list(self,dir_path):
        file_list = []
        for root,dirs,files in os.walk(dir_path):
            for name in files:
                file_list.append(os.path.join(root,name))
        return file_list


    def get_match_filetype_list(self,dir_path,fileType_list=['all']):
        choosen_file_list = []
        file_list = self.get_file_list(dir_path)
        if fileType_list==['all']:
            return file_list           

        else:
            try:
                for filetype in fileType_list:
                    for filepath in file_list:
                        if filetype in filepath:
                            choosen_file_list.append(filepath)
                return choosen_file_list
            except:
                print('参数错误/args wrong')




    def get_name_filetype_match_filelist(self,dir_path,name=None,fileType_list=['all']):
        chosen_type_filelist = self.get_match_filetype_list(dir_path,fileType_list)
        if name != None:
            chosen_type_name_filelist=[]
            for chosen_name_file in chosen_type_filelist:
                    if name in chosen_name_file:
                        chosen_type_name_filelist.append(chosen_name_file)
            return chosen_type_name_filelist
        else:
            return chosen_type_filelist
            
        
        
        
            
        
        
                
                                  
            

