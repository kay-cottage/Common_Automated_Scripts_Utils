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
    def match_remove(self,dir_path,name=None,fileType_list=['all']，current_dir=True):
        count=0
        del_path_list = self.get_name_filetype_match_filelist(dir_path,name,fileType_list，current_dir=current_dir)
        for del_path in del_path_list:
            os.remove(del_path)
            count+=1
        print('delete successfully!'+'共删除'+str(count)+'个文件')


    #按照文件种类匹配复制到目标文件夹下
    def match_copy(self,dir_path,Target_Dir_Path,name=None,fileType_list=['all']，current_dir=True):
        count=0
        src_path_list = self.get_name_filetype_match_filelist(dir_path,name,fileType_list，current_dir=current_dir)
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


    # 文件移动（参数【全部必填】：源目录，目标目录，文件）
    def move_file(self,src_path, dst_path, file):
        try:
            f_src = os.path.join(src_path, os.path.basename(file))
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            f_dst = os.path.join(dst_path, file)
            shutil.move(f_src, f_dst)
        except Exception as e:
            print('move_file ERROR: ',e)
        

    # 得到遍历文件的列表，参数【dir_path必填】，current_dir为默认遍历dir_path目录下所有文件
    def get_file_list(self,dir_path,current_dir=True):
        file_list = []
        if current_dir==True:
            for name in os.listdir(dir_path):
                if not bool(os.path.isdir(os.path.join(dir_path,name))):
                    file_list.append(os.path.join(dir_path,name))
            return file_list
        else:        
            for root,dirs,files in os.walk(dir_path):
                for name in files:
                    file_list.append(os.path.join(root,name))
            return file_list


    def get_match_filetype_list(self,dir_path,fileType_list=['all'],current_dir=True):
        choosen_file_list = []
        file_list = self.get_file_list(dir_path,current_dir=current_dir)
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



    # 程序列表遍历操作总入口
    def get_name_filetype_match_filelist(self,dir_path,name=None,fileType_list=['all'],current_dir=True):
        chosen_type_filelist = self.get_match_filetype_list(dir_path,fileType_list=fileType_list,current_dir=current_dir)
        if name != None:
            chosen_type_name_filelist=[]
            for chosen_name_file in chosen_type_filelist:
                    if name in chosen_name_file:
                        chosen_type_name_filelist.append(chosen_name_file)
            return chosen_type_name_filelist
        else:
            return chosen_type_filelist
            
        
        

                
           
            

