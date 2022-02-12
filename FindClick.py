# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
import os
import sys
from PIL import ImageGrab
import pyautogui
import time


# yolox    label, top, left, bottom, right


class FindClick(object):
    #有默认值放后
    def __init__(self,Use_AI = False):
        self.Use_AI = Use_AI
        



    def mouse_press_without_ai(
                    self,
                    match_pic_path,
                    click='doubleclick',
                    click_times = 1,
                    confidence = 0.6,
                    mousedown_last_time = 0.025,
                    ):

        if click == 'click':
            try:
                img_location = pyautogui.locateCenterOnScreen(match_pic_path,confidence=confidence)
                for i in range(click_times):
                    pyautogui.click(x=img_location[0], y=img_location[1]) 
            except:
                print('Click Fail')

        elif click == 'doubleclick':
            try:                
                img_location = pyautogui.locateCenterOnScreen(match_pic_path,confidence=confidence)
                for i in range(click_times):
                    pyautogui.doubleClick(x=img_location[0], y=img_location[1])
            except:
                print('Doubleclick Fail')
        elif mousedown_last_time != 0.025:
            try:
                pyautogui. mouseDown()
                time.sleep(mousedown_last_time)
                pyautogui.mouseUp() 
            except:
                print('Click Fail')
            
            
        else:
            print('args error')


    def press_keyboard(self,keyboard_input_list):
        pyautogui.press(keyboard_input_list)


    def action(self,match_pic_path=None):
        if self.Use_AI == False:
            self.mouse_press_without_ai(match_pic_path)
        else:
            import yolox.predict 
            yolox.predict.dectect()
            #yolox.predict.dir_detect_db(r'F:\ASUS\Desktop\A_python_script\Utils\utils\yolox\img')
            
            

    
        


     
   


f = findclick(Use_AI = True)

#f.action()
f.action(match_pic_path = r'6.png' )
