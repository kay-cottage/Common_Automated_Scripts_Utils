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

from model import shufflenet_v2_x1_0,shufflenet_v2_x0_5


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    data_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    # load image
    img_path = r"3.jpg"
    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path)
    plt.imshow(img)
    # [N, C, H, W]
    img = data_transform(img)
    # expand batch dimension
    img = torch.unsqueeze(img, dim=0)

    # read class_indict
    json_path = './classes1.json'
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)

    json_file = open(json_path, "r")
    class_indict = json.load(json_file)

    # create model
    model = shufflenet_v2_x0_5(num_classes=4).to(device)
    # load model weights
    model_weight_path = r"F:\ASUS\Desktop\A_python_script\Utils\utils\shufflenetv2\weights\model-13.pth"
    model.load_state_dict(torch.load(model_weight_path, map_location=device))
    model.eval()
    with torch.no_grad():
        # predict class
        output = torch.squeeze(model(img.to(device))).cpu()
        predict = torch.softmax(output, dim=0)
        print('predeict',predict.numpy())
        predict_cla = torch.argmax(predict).numpy()

    print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
                                                 predict[predict_cla].numpy())
    print(print_res)
    plt.title(print_res)
    #for i in range(len(predict)):
        #print("class: {:10}   prob: {:.3}".format(class_indict[str(i)],
                                                  #predict[i].numpy()))
    plt.show()


if __name__ == '__main__':
    main()
