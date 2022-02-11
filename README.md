# Common_Automated_Scripts_Utils


*注意：禁止用于商业用途，欢迎个人学习交流！*


## 描述 (Description)

一个应用广泛，功能强大，并伴有AI技术辅助的整合了多种常用Python脚本的工具箱；能够在办公自动化批量处理，游戏辅助，文件多模态AI管理等多个领域发挥作用。旨在做到方便快捷、拿来即用。该项目多为个人原创想法的简单实现，后续会不定期继续不断完善功能，敬请期待！



## 环境 (Environment)

* CPU友好型！无须特地安装CUDA 等GPU驱动支持
* CUDA CUDNN(非必须）
* Flask-sqlalchemy
* python 3.7
* Pythorch
* pyautogui
* pycrypto
* Pillow
* opencv



## 功能基本介绍：


### 多模态智能文件管理模块（本地AI相册）：

    * 基于shuffleNet、YOLOX等优秀轻量级神经网络，后续还可能会引入GPT、transformer等技术辅助处理；
    * 能够在本地自动根据使用者个人文件分类习惯进行学习，并帮助使用者进行自动相册归档操作且几乎无需对神经网络的训练进行额外操作；
    * 通过多模态搜索，使用者可以根据描述找到相应符合类型的图片；


### 智能输入操作模块：

    * 支持引入神经网络，使用者可以根据自身需求进行设计，实现自动点击、打卡、刷课、游戏辅助等等操作；  


### 文件批量处理模块：
> batch.py

    * 能够批量对各种类型的文件进行精细化的增删查改操作；
    


### 文件加密模块：

    * 基于AES-cfb高级加密，使用者可以轻松对需要加密的文件进行精细化的批量加解密操作，保护隐私安全；


### 文件批量读写处理模块：

    * 后续将在计划文件批量读写，制图绘图、等方面努力


## 如何使用：
> batch.py
```python
class batch()
 |  文件批量增删查改类下常用方法
 |  
 |  Methods defined here:
 |  
 |  __init__(self,startNumber=0, )
 |      初始化方法
 |      :param startNumber=startNumber
 |  
 |  rename_with_num(self,dir_path,name='',fileType='.png')
 |      目标文件夹下按照自定义规则匹配批量重命名文件
 |      :param dir_path: 目标目录   必填
 |      :param name: 文件名修改为name 选填
 |      :param fileType: 需要修改的文件类型  选填
 |      :return: 无
 |  
 |  match_remove(self,dir_path,name=None,fileType_list=['all'],current_dir=True)
 |      目标文件夹下按照自定义规则删除文件
 |      :param dir_path: 目标目录  必填
 |      :param name: 文件名修改为name 选择填
 |      :param fileType_list: 需要删除的的文件类型列表，默认'all' 选择填
 |      :param current_dir: 默认True只处理dir_path当前目录下的所有文件，False则处理当前文件夹及其子文件夹下所有文件  选择填
 |      :return: 无
 |
 |  match_copy(self,dir_path,Target_Dir_Path,name=None,fileType_list=['all'],current_dir=True)
 |       按照文件匹配规则复制到目标文件夹下
 |      :param dir_path: 源文件目录  必填
 |      :param Target_Dir_Path: 目标文件目录  必填
 |      :param name: 文件名修改为name  选择填
 |      :param fileType_list: 需要删除的的文件类型列表，默认'all'  选择填 
 |      :param current_dir: 默认True只处理dir_path当前目录下的所有文件，False则处理当前文件夹及其子文件夹下所有文件  选择填
 |      :return: 无
 |
 |  get_filename_txt(self,dir_path,output_filename='output.txt')
 |      得到默认目录下所有文件路径并写入到.txt文件中 
 |      :param dir_path: 目标目录   必填
 |      :param output_filename: 默认结果输出到output.txt  选择填
 |      :return: 无
 |
 |  move_file(self,src_path, dst_path, file)
 |      文件移动
 |      :param src_path: 源目录  必填
 |      :param dst_path: 目标目录  必填
 |      :param file: 文件名  必填
 |      :return: 无
 |
 |
 |  get_name_filetype_match_filelist(self,dir_path,name=None,fileType_list=['all'],current_dir=True)
 |      程序文件匹配列表遍历操作总入口
 |      :param dir_path: 源文件目录  必填
 |      :param name: 文件名含有name关键字  选择填
 |      :param fileType_list: 需要删除的的文件类型列表，默认'all'，例：['.jpg','.png']  选择填 
 |      :param current_dir: 默认True只处理dir_path当前目录下的所有文件，False则处理当前文件夹及其子文件夹下所有文件  选择填
 |      :return: list
 |

# example
import batch
b = batch()
#筛选文件，得到对应文件路径的列表
chosen_file_list=b.get_name_filetype_match_filelist(dir_path=r'F:\ASUS\Desktop')

#批量删除某文件夹下的文件
b.match_remove(dir_path=r'F:\ASUS\Desktop')
```





## 更多信息：

* 欢迎关注我的bilibili主页：https://space.bilibili.com/362186371

* 更多信息，相关视频会在那里更新

* 不喜勿喷，谢谢哈
