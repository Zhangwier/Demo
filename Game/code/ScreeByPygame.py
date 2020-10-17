# ScreenByPygame.py
"""
界面(背景，所有元件,交互集*4)
-不可交互元件(界面,相对位置,图像)
--不变元件
--可变元件
-可交互的元件(界面,相对位置,图像,反应)
--反应(反应方法，事件)
--位置非关联交互(*,反应位置)

更新方法
-需要更新的界面(底层界面,交互界面,上层渲染界面)
--交互判断
--交互产生
--元件更新
-鼠标更新(本体,浮游物-?)

交互判断(存在,点击,右键,滑轮)
-鼠标是否在可交互集
-反应函数

界面切换
-缩略图
-淡出淡入(透明度-时间)

CG
-临时界面

模拟4D背景
-基于鼠标位置

界面管理器
-当前界面
-切换状态
-临时界面(界面,时间)
"""
import os
import pygame
import random
import sys
from pygame.locals import *
from pygame import Vector2
from abc import abstractclassmethod, ABCMeta


# 基本元件,基本方法
class MySprite(pygame.sprite.Sprite, metaclass=abc.ABCMeta):

    @abstractclassmethod
    def __init__(cls):
        super().__init__()
        pass

    @abstractclassmethod
    def update(cls, current_time, rate=200):
        pass

    @abstractclassmethod
    def load(cls, adr):
        pass


# 元件
class Unit(MySprite):

    def __init____(self):
        super().__init__()

    def update(self):
        pass

    def load(self):
        pass


# 可操作元件
class Unit_action(Unit):
    pass


# GUI
class Screen():
    pass

    def __init__(self):
        super.__init__()
        all_unit = {}
        unit_mouseexist_action_list = {}
        unit_mouseclick_left_action_list = {}
        unit_mouseclick_right_action_list = {}
        unit_mouserollow_action_list = {}

    def Screen_setting(self):
        pass

    def update(self, time=0):
        pass

    # GUI转换
    def Screen_change(self, goal_screen, setting="none"):
        pass

    def video_play(self, videa_adr, video_play_site):
        pass


# 工厂
def Factory(object, object_class, *args):
    pass


# 建造者/错误处理
def Builder(object, object_action, *args):
    pass


# 操作端
class Client():
    pass


# 传递器
class Transfer():
    pass

    #接口调配器
    def adapter_pattern(self):
        pass


# 服务器终端
class Server():
    pass

    def initial_setting(self):
        pass

    def brain(self):
        pass

    def data_update(self,data):
        pass

    def data_load(self, data_adr):
        pass

    def data_save(self, data, save_adr):
        pass


#观察者
class Observer():
  pass