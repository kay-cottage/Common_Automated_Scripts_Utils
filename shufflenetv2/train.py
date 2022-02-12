# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
import os
import math
import argparse

import torch
import torch.optim as optim
from torchvision import transforms
import torch.optim.lr_scheduler as lr_scheduler

from model import shufflenet_v2_x1_0,shufflenet_v2_x0_5
from my_dataset import MyDataSet
from utils import train_one_epoch, evaluate
from pre_dataset import make_label,make_label_index,get_train_val,dic_classes
import sys 
sys.path.append("..") 
import batch



def main(args):
    
    
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")

    print(args)

    if os.path.exists("./weights") is False:
        os.makedirs("./weights")

    b = batch.batch()
    # 遍历总目录下的所有file 路径列表
    images_path_list = b.get_file_list(dir_path=args.dir_path,current_dir=False)
    # 得到所有分类文件夹列表（get classes)
    dir_list,num_class=make_label(images_path_list)
    # 生成classes.json
    dic_classes(classes_list=dir_list)
    

    # 按8:2划分数据集，得到train list val list 列表
    train_images_path, val_images_path = get_train_val(dir_list,scale=0.8)
    # 得到标签
    train_images_label = make_label_index(train_images_path)
    val_images_label = make_label_index(val_images_path)


    print('Found train_images number:',len(train_images_path))
    print('Found val_images number:',len(val_images_path))
    data_transform = {
        "train": transforms.Compose([transforms.RandomResizedCrop(224),
                                     transforms.RandomHorizontalFlip(),
                                     transforms.ToTensor(),
                                     transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        "val": transforms.Compose([transforms.Resize(256),
                                   transforms.CenterCrop(224),
                                   transforms.ToTensor(),
                                   transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])}

    # 实例化训练数据集
    train_dataset = MyDataSet(images_path=train_images_path,
                              images_class=train_images_label,
                              transform=data_transform["train"])

    # 实例化验证数据集
    val_dataset = MyDataSet(images_path=val_images_path,
                            images_class=val_images_label,
                            transform=data_transform["val"])


    #print('train_dataset',train_dataset)
    batch_size = args.batch_size
    nw = min([os.cpu_count(), batch_size if batch_size > 1 else 0, 8])  # number of workers
    print('Using {} dataloader workers every process'.format(nw))
    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=batch_size,
                                               shuffle=True,
                                               pin_memory=True,
                                               num_workers=nw,
                                               collate_fn=train_dataset.collate_fn)

    val_loader = torch.utils.data.DataLoader(val_dataset,
                                             batch_size=batch_size,
                                             shuffle=False,
                                             pin_memory=True,
                                             num_workers=nw,
                                             collate_fn=val_dataset.collate_fn)

    # 如果存在预训练权重则载入
    model = shufflenet_v2_x0_5(num_classes=args.num_classes).to(device)
    if args.weights != "":
        if os.path.exists(args.weights):
            weights_dict = torch.load(args.weights, map_location=device)
            load_weights_dict = {k: v for k, v in weights_dict.items()
                                 if model.state_dict()[k].numel() == v.numel()}
            print(model.load_state_dict(load_weights_dict, strict=False))
        else:
            raise FileNotFoundError("not found weights file: {}".format(args.weights))

    # 是否冻结权重
    if args.freeze_layers:
        for name, para in model.named_parameters():
            # 除最后的全连接层外，其他权重全部冻结
            if "fc" not in name:
                para.requires_grad_(False)

    pg = [p for p in model.parameters() if p.requires_grad]
    optimizer = optim.SGD(pg, lr=args.lr, momentum=0.9, weight_decay=4E-5)
    # Scheduler https://arxiv.org/pdf/1812.01187.pdf
    lf = lambda x: ((1 + math.cos(x * math.pi / args.epochs)) / 2) * (1 - args.lrf) + args.lrf  # cosine
    scheduler = lr_scheduler.LambdaLR(optimizer, lr_lambda=lf)

    for epoch in range(args.epochs):
        # train
        mean_loss = train_one_epoch(model=model,
                                    optimizer=optimizer,
                                    data_loader=train_loader,
                                    device=device,
                                    epoch=epoch)

        scheduler.step()

        # validate
        acc = evaluate(model=model,
                       data_loader=val_loader,
                       device=device)

        print("[epoch {}] accuracy: {}".format(epoch, round(acc, 3)))
        torch.save(model.state_dict(), "./weights/model-{}.pth".format(epoch))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_classes', type=int, default=4)
    parser.add_argument('--epochs', type=int, default=30)
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--lr', type=float, default=0.01)
    parser.add_argument('--lrf', type=float, default=0.1)

    #需要分类的文件根目录（必填）
    parser.add_argument('--dir_path', type=str,
                        default=r'F:\ASUS\Desktop\class_pic')

    # shufflenetv2_x1.0 官方权重下载地址
    # https://download.pytorch.org/models/shufflenetv2_x1-5666bf0f80.pth
    # 模型文件路径（必填）
    parser.add_argument('--weights', type=str, default=r"F:\ASUS\Desktop\A_python_script\Utils\utils\shufflenetv2\weights\shufflenetv2_x0.5-f707e7126e.pth",
                        help='initial weights path')
    # 是否冻结层训练
    parser.add_argument('--freeze-layers', type=bool, default=False)
    parser.add_argument('--device', default='cuda:0', help='device id (i.e. 0 or 0,1 or cpu)')
    opt = parser.parse_args()
    main(opt)
