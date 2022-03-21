# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
import os
from shutil import copyfile
import re
import json


# 将答案文件转换为字典{'1': 'A', '2': 'C'}
def match_answer(answer_filepath):
    f1=open(answer_filepath,'r',encoding='utf-8')
    f1=f1.read()
    
    num_list=list(re.compile(r'\d+').findall(f1))
    Answer_list=list(re.compile(r"[A-E]").findall(f1))
    del f1
    if len(num_list)==len(Answer_list):
        return dict(zip(num_list,Answer_list))
    else:
        return 'Answer Not Match'

# 返回所有题目的列表，整个文档的列表
def get_q_list(question_filepath):
    q_list=[]
    line_num=0
    f=open(question_filepath,encoding='utf-8')
    total_list = f.readlines() 
    for i in total_list:
        line_num+=1
        if re.search('(\d+)',i[0:4]) != None:
            if re.search('(\d+)',i[0:4]).span()[0]==0:
                q_list.append(i)

    Answer_index=[]
    for q in q_list:
        q_index=total_list.index(q)
        Answer_index.append(q_index)

    del Answer_index

    return q_list,total_list

# 匹配字符串 强制精确匹配
def match(sub,all_str):
    for i in range(len(all_str)):
        if all_str[i:int(i)+int(len(sub))] == sub:
            return [i,int(i)+int(len(sub))]


#Answer_list:题目列表[[A.XX  B.XX]],返回5个选项的字典
def get_index(Answer_list,sub_list=['A.','B.','C.','D.','E.']):
    
    index_dic={}
    for sub in sub_list:
        index_list=[]
        for i in Answer_list:
            index=match(sub,str(i))
            index_list.append(index)
        index_dic[sub]=index_list    
    return index_dic

#得到题目索引列表,索引值+1等于五个答案
#返回答案索引，题号：题目 字典，所有内容 total_list
def get_a_index(question_filepath,answer_filepath):
    q_list,total_list=get_q_list(question_filepath)
    answer_dict = match_answer(answer_filepath)

    Answer_index=[]
    q_num_list=[]
    #q:问题
    for q in q_list:
        #得到每一个q索引
        q_index=total_list.index(q)
        # 题号
        q_num=re.compile(r'\d+').findall(q[0:4])[0]
        Answer_index.append(q_index)
        
    Answer_list=[]
    
    Answer_index.append(len(total_list))
    
    for i in Answer_index:
        if Answer_index.index(i)+1<len(Answer_index):
            a_start,a_end=int(i)+1,Answer_index[Answer_index.index(i)+1]
            Answer_list.append(total_list[a_start:a_end])
    del Answer_index
    return total_list,q_list,Answer_list


# demo a = get_answer(19,'C') 返回19题的c选项内容
def get_answer(answer_num,sub,question_filepath,answer_filepath,sub_list=['A.','B.','C.','D.','E.']):
    _,_,Answer_list=get_a_index(question_filepath,answer_filepath)
    index_dic=get_index(Answer_list)    
    if sub in 'A.':
        if index_dic['A.'][answer_num-1] and index_dic['B.'][answer_num-1] != None:
            return str(Answer_list[answer_num-1])[int(index_dic['A.'][answer_num-1][1]):int(index_dic['B.'][answer_num-1][0])]
        else:
            return None

    elif sub in 'B.':
        if index_dic['B.'][answer_num-1] and index_dic['C.'][answer_num-1] != None:
            return str(Answer_list[answer_num-1])[int(index_dic['B.'][answer_num-1][1]):int(index_dic['C.'][answer_num-1][0])]
        else:
            return None

    elif sub in 'C.':
        if index_dic['C.'][answer_num-1] and index_dic['D.'][answer_num-1] != None:
            return str(Answer_list[answer_num-1])[int(index_dic['C.'][answer_num-1][1]):int(index_dic['D.'][answer_num-1][0])]
        else:
            return None

    elif sub in 'D.':
        if index_dic['D.'][answer_num-1] and index_dic['E.'][answer_num-1] != None:
            return str(Answer_list[answer_num-1])[int(index_dic['D.'][answer_num-1][1]):int(index_dic['E.'][answer_num-1][0])]
        else:
            return None

    elif sub in 'E.':
        if index_dic['E.'][answer_num-1] != None:
            return str(Answer_list[answer_num-1])[int(index_dic['E.'][answer_num-1][1]):int(len(str(Answer_list[answer_num-1])))]
        else:
            return None

        

def get_answer_list(question_filepath,answer_filepath):
    answer_list=[]
    answer_dict = match_answer(answer_filepath)        
    for k,v in answer_dict.items():
        answer = get_answer(int(k),v,question_filepath,answer_filepath)
        answer_list.append(answer)
    return answer_list


#生成答案文档文档question_filepath:单选题文档路径，默认A. B. C. D. E.  answer_filepath:答案文档路径 , output_filepath：输出文档路径
def make_q_a_doc(question_filepath,answer_filepath,output_filepath):
    _,q_list,_=get_a_index(question_filepath,answer_filepath)
    answer_list=get_answer_list(question_filepath,answer_filepath)

    all_={}
    all_=dict(zip(q_list,answer_list))
    f=open(output_filepath,'w',encoding='utf-8')

    for k,v in all_.items():
        f.writelines(str(k)+str(v).strip("' \n',[]{}''‘’")+2*'\n')                
    f.close()
    print('Match Successfully!'+'成功生成提纲文档 '+output_filepath)
    del q_list,answer_list
    return all_




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
    def match_remove(self,dir_path,name=None,fileType_list=['all'],current_dir=True):
        count=0
        del_path_list = self.get_name_filetype_match_filelist(dir_path=dir_path,name=name,fileType_list=fileType_list,current_dir=current_dir)
        for del_path in del_path_list:
            os.remove(del_path)
            count+=1
        print('delete successfully!'+'共删除'+str(count)+'个文件')


    #按照文件种类匹配复制到目标文件夹下
    def match_copy(self,dir_path,Target_Dir_Path,name=None,fileType_list=['all'],current_dir=True):
        count=0
        src_path_list = self.get_name_filetype_match_filelist(dir_path=dir_path,name=name,fileType_list=fileType_list,current_dir=current_dir)
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
            
        
        
def file_filter(func,*args, **kwargs):
    try:
        b=batch()
        filter_list=b.get_name_filetype_match_filelist(*args, **kwargs)
        for file_path in filter_list:
            func(file_path)
    except:
        print('args erro')
                    
                
         


