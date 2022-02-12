# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
import os
import json
import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
#from shufflenetv2.model import shufflenet_v2_x0_5



def batch_predict(dir_path_list,json_path='./classes.json',model_weight_path = r"model/shufflenetv2_x0.5-f707e7126e.pth"):
    data_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)

    #load json
    json_file = open(json_path, "r")
    class_indict = json.load(json_file)


    # create model
    model = shufflenet_v2_x0_5(num_classes=1000).to(device)

    # load model weights
    model.load_state_dict(torch.load(model_weight_path, map_location=device))
    model.eval()
    file_class_path_dic={}
    with torch.no_grad():
        for img_path in dir_path_list:
            # load image
            assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
            img = Image.open(img_path)
            # [N, C, H, W]
            img = data_transform(img)
            # expand batch dimension
            img = torch.unsqueeze(img, dim=0)
                   
            # predict class
            output = torch.squeeze(model(img.to(device))).cpu()
            predict = torch.softmax(output, dim=0)
            predict_cla = torch.argmax(predict).numpy()

            print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
                                                         predict[predict_cla].numpy())
            print(print_res)
            file_class_path_dic[img_path]=class_indict[str(predict_cla)]
    return file_class_path_dic
    

    
import exifread
img=exifread.process_file(open(r'F:\ASUS\Desktop\A_python_script\Utils\utils\test\IMG_0002.JPG','rb'))
time=img['Image DateTime']
print(time)
