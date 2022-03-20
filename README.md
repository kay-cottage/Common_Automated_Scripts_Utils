# Common_Automated_Scripts_Utils


*注意：禁止用于商业用途，欢迎个人学习交流！*


## 描述 (Description)

一个应用广泛，功能强大，并伴有AI技术辅助的整合了多种常用Python脚本的工具箱；能够在办公自动化批量处理，游戏辅助，文件多模态AI管理等多个领域发挥作用。旨在做到方便快捷、拿来即用。该项目多为个人原创想法的简单实现，后续会不定期继续不断完善功能，敬请期待！



## 环境 (Environment)

* CPU友好型！无须特地安装CUDA 等GPU驱动支持
* CUDA CUDNN(非必须）
* pywin32 win32api
* Flask-sqlalchemy
* python 3.7
* pyautogui
* Windows
* Pythorch
* pycrypto
* opencv
* Pillow





## 功能基本介绍：


### 多模态智能文件管理模块（本地AI相册）：
>请见 yolox shufflenetv2 
    
    * 基于shuffleNet、YOLOX等优秀轻量级神经网络，后续还可能会引入GPT、transformer等技术辅助处理；
    * 能够在本地自动根据使用者个人文件分类习惯进行学习，并帮助使用者进行自动相册归档操作且几乎无需对神经网络的训练进行额外操作；
    * 通过多模态搜索，使用者可以根据描述找到相应符合类型的图片；



### 智能输入操作模块：
>请见FindClick.py
    
    * 支持引入神经网络，使用者可以根据自身需求进行设计，实现自动点击、打卡、刷课、游戏辅助等等操作；  



### 文件批量处理模块：
>请见batch.py
    
    * 能够批量对各种类型的文件进行精细化的增删查改操作；

    


### 文件加密模块：
>请见AesEncrypt.py
    
    * 基于AES-cfb高级加密，使用者可以轻松对需要加密的文件进行精细化的批量加解密操作，保护隐私安全；


 


### 文件批量读写处理模块：

    * 能够自动将题库题目的正确答案自动匹配到原题中
   
    * 能够检测分离出题库题目与正确答案自动生成出复习提纲


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
 |      :param dir_path: 目标目录  必填
 |      :param name: 文件名修改为name    选填
 |      :param fileType: 需要修改的文件类型  选填
 |      :return: 无
 |  
 |  match_remove(self,dir_path,name=None,fileType_list=['all'],current_dir=True)
 |      目标文件夹下按照自定义规则删除文件
 |      :param dir_path: 目标目录  必填
 |      :param name: 文件名修改为name    选择填
 |      :param fileType_list: 需要删除的的文件类型列表,默认'all'        选择填
 |      :param current_dir: 默认True只处理dir_path当前目录下的所有文件
 |                          False则处理当前文件夹及其子文件夹下所有文件    选择填
 |      :return: 无
 |
 |  match_copy(self,dir_path,Target_Dir_Path,name=None,fileType_list=['all'],current_dir=True)
 |       按照文件匹配规则复制到目标文件夹下
 |      :param dir_path: 源文件目录  必填
 |      :param Target_Dir_Path: 目标文件目录  必填
 |      :param name:文件名修改为name  选择填
 |      :param fileType_list: 需要删除的的文件类型列表，默认'all'    选择填 
 |      :param current_dir:默认True只处理dir_path当前目录下的所有文件
 |                         False则处理当前文件夹及其子文件夹下所有文件    选择填
 |      :return: 无
 |
 |  get_filename_txt(self,dir_path,output_filename='output.txt')
 |      得到默认目录下所有文件路径并写入到.txt文件中 
 |      :param dir_path:        目标目录  必填
 |      :param output_filename: 默认结果输出到output.txt  选择填
 |      :return: 无
 |
 |  move_file(self,src_path, dst_path, file)
 |      文件移动
 |      :param src_path: 源目录                    必填
 |      :param dst_path: 目标目录                  必填
 |      :param file:     文件名                    必填
 |      :return: 无
 |
 |
 |  get_name_filetype_match_filelist(self,dir_path,name=None,fileType_list=['all'],current_dir=True)
 |      程序文件匹配列表遍历操作总入口
 |      :param dir_path: 源文件目录    必填
 |      :param name: 文件名含有name关键字    选择填
 |      :param fileType_list: 需要删除的的文件类型列表,默认'all',例：['.jpg','.png']  选择填 
 |      :param current_dir: 默认True只处理dir_path当前目录下的所有文件
 |                          False则处理当前文件夹及其子文件夹下所有文件        选择填
 |      :return: list
 |

# example
import batch
b = batch()
#筛选文件，得到对应文件路径的列表
chosen_file_list=b.get_name_filetype_match_filelist(dir_path=r'F:\ASUS\Desktop')

#批量删除某文件夹下的文件
b.match_remove(dir_path=r'F:\ASUS\Desktop')

# 当然如果你熟悉开发工作，遇到需要批量文件操作的工作，你完全是可以通过自定义函数完成一系列的操作
# file_filter方法支持您将自定义函数传入进行操作
# example
from batch import file_filter

# 过滤批量删除
def filter_remove(file_path):
    os.remove(file_path)

# file_filter 传入参数同get_name_filetype_match_filelist()
file_filter(filter_remove,dir_path=r'F:\python_script\click_script')
```



> AesEncrypt.py   ([效果演示请见]( https://b23.tv/GgKn2dO))
```python
class AesEncrypt()
 |  常用AES加解密方法，对特定文件做高级加解密
 |  
 |  Methods defined here:
 |  
 |  __init__(self, key, mode=AES.MODE_CFB)
 |      初始化方法 AES-cfb需要iv值与key进行操作
 |      :param mode = mode
 |      :param key = key
 |      :param iv = Random.new().read(AES.block_size)
 |  
 |  encrypt_file(self,dir_file_list)
 |      对传入的路径列表中对应的文件做AES-cfb流加密
 |      :param dir_file_list : 文件路径列表   必填
 |      :return: 无
 |  
 |  decrypt_file(self,dir_file_list)
 |      对传入的路径列表中对应的文件做AES-cfb逆向解密
 |      :param dir_file_list : 文件路径列表   必填
 |      :return: 无
 |
 |

# example
key = '1234567890123456'
dir_path = r"F:\ASUS\Desktop\test"
aes = AesEncrypt(key)
b = batch()
b = b.get_name_filetype_match_filelist(dir_path = dir_path,fileType_list=['all'])

#encrypt
aes.encrypt_file(b)

#decrypt
aes.decrypt_file(b)
```

> FindClick.py    ([自动化微信跳一跳](https://b23.tv/xo3cwfI))
```python
class FindClick()
 |  匹配鼠标点击键盘操作方法
 |  
 |  Methods defined here:
 |  
 |  __init__(self, Use_AI)
 |      初始化方法
 |      :param Use_AI = Use_AI
 |  
 |  match_click(self,dir_file_list)
 |     点击操作脚本控制
 |      :param match_pic_path :               需需要匹配的图象路径   必填
 |      :param click : 'click'/'doubleclick'  单双击可选            选择填
 |      :param confidence:                    匹配置信度            选择填
 |      :param mousedown_last_time :          鼠标按下多少秒后弹起   选择填
 |      :return: 无
 |  
 |  demo_action(self,dir_file_list)
 |      自行设计
 |      :return: 无
 |

# example in action
import yolox.predict 
yolox.predict.dectect()

```

### Quick Start！

### 对于多模态智能文件管理模块分别是yolox/shufflenetv2我会在另外的仓库对他们分别进行详细的介绍（未完待续哈）：


> yolox 的电脑屏幕实时目标检测的使用参照以上的example  ([效果演示请见](https://b23.tv/sxKezze))
```python

import yolox.predict 
# 返回目标检测信息的二维列表与image
yolox.predict.dectect()



```


> yolox 的多模态检索，通过文字关键词找到符合描述的相关图片,以下是一个简单demo
```python
# yolox\predict.py

import yolox.predict 

#初次使用先建立先在DB.py建数据库,dir_detect_db对图片进行遍历建库
dir_detect_db(dir_path='F:\ASUS\Desktop')

# 返回符合条件的图片路径
filepath=get_classes_path(keyword='car'):

```

> shufflenet AI本地相册分类程序的使用。学习你的分类习惯！ 
```python
# demo example
# 在shufflenetv2\train.py下，初次使用你只需要注意以下参数，其他参数非必须调整：


#1.需要分类的所有文件的根目录（必填）
parser.add_argument('--dir_path', type=str,
                        default=r'F:\ASUS\Desktop\class_pic')

# 模型文件路径（迁移学习必填否则可不填）
parser.add_argument('--weights', type=str, default="weights\shufflenetv2_x0.5-f707e7126e.pth",
                        help='initial weights path')


```

> 学习完成后的AI相册自动分类使用demo
```python
# demo example
# shufflenetv2\predict.py

# 自动将class_pic无需的照片按照你以往的分类习惯进行归类
main(dir_path=r'F:\ASUS\Desktop\class_pic',model_weight_path = r"F:\ASUS\Desktop\Utils\utils\shufflenetv2\weights\model-13.pth",json_path = './classes1.json)

```


> 根据题库自动生成复习复习提纲代码使用demo
```python
# yolox\batch.py

from batch import make_q_a_doc

#question_filepath='question.txt'  必填 该文件装单选题目 不含答案
#answer_filepath='answer.txt',     必填 该文件装单选答案 
#output_filepath='output.txt'      必填 该文件为题库生成提纲的输出路径
doc_dic=make_q_a_doc(question_filepath='question.txt',answer_filepath='answer.txt',output_filepath='output.txt')

# 返回符合条件的图片路径
filepath=get_classes_path(keyword='car'):

```




## 更多信息：

* 欢迎关注我的bilibili主页：https://space.bilibili.com/362186371

* 更多信息，相关视频会在那里更新

* 不喜勿喷，谢谢哈

