#Tkinter_Pygame.py
#Made a GUI library by Pygame

import pygame
import os
import sys
import random
import tkinter

class unit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bg=(100,149,237)
        self.target_screen=0
        self.image = False
        self.rect = pygame.Rect(0,0,0,0)
        self.attach_list=[]
        self.mode="none"
    
    def get_size(self):
        return self.rect.size

    #def pack():
    #I think we dont need the function!

    def place(self,x=0,y=0):
        self.rect.left,self.rect.top = x,y

    def site_format(self,mode=self.mode):
        if mode == "center":
            self.place(self.target_screen.rect.centerx\
                -self.rect.width/2,self.target_screen.rect.centery)
        elif mode == "left":
            self.place(self.target_screen.rect.left,\
                self.target_screen.rect.centery)

    def add_attach(self,unit,site=(0,0)):
        self.attach_list.append(unit)
        if site != (0,0):
            unit.rect.right,unit.rect.top = site

    def del_attach(self,unit):
        attach_list.remove(unit)
    
    def update(self,current_time, rate=100):
        if not self.image:
            self.image.fill(self.bg)
        else:
            self.target_screen.blit(self.image,self.rect)
        for _ in self.attach_list:
            self.image.blit(_.image,_.rect)

    def combine_txt(self):
        pass


class Txt_Label(unit):
    def __init__(self,target_screen,text="",size=30):
        super().__init__()
        self.fg=(0,0,0)
        self.target_screen=target_screen
        self.font_size=size
        self.font="C:\\Windows\\Fonts\\seguihis.ttf"
        self.text=text
        self.image = pygame.font.Font(self.font,\
            self.font_size).render(self.text,True,self.fg,self.bg)
        self.rect = self.image.get_rect()

    def change_txt(self,change_tup):
        change_dir={"size":self.size,"text":self.text,\
            "x":self.rect.right,"y":self.rect.top,"font":self.font}
        change_dir[change_tup[0]]=change_tup[1]
        self.image = pygame.font.Font(self.font,self.font_size).\
            render(self.text,True,self.fg,self.bg)

    #def txt_site_format(self,x=0,y=0):
    #    self.txt_rect.width,self.txt_rect.height = x,y


class Image_Label(unit):
    def __init__(self,target_screen,image_file_adr,size=30):
        super().__init__()
        self.fg=(0,0,0)
        self.target_screen=target_screen
        self.image = pygame.image.load(image_file_adr).convert_alpha()
        self.rect = self.image.get_rect()


class Button(unit):
    def __init__(self,target_screen,text="",size=(0,0),command=nothing):
        super().__init__()
        self.target_screen=target_screen
        if text:
            self.add_attach(Txt_Label(self.target_screen,text=text))
        self.command=command

    #1 每个单独检测鼠标事件
    #2 将所有需要判断的区域放在一个集合
    def update(self,current_time, rate=100):
        super().update(current_time, rate=100)
        if mouse_judge(self.rect):
            #停留反应函数
            #if pygame.event.get().type == pygame.MOUSEBUTTONDOWN
            #需要优化!
            self.command()


class Entry(unit):
    def __init__(self,target_screen, show='*'):
        super().__init__()
        pass

    def update(self, current_time, rate=100):
        pass


class Canvas(unit):
    pass


class Checkbutton(unit):
    pass


class Menu(unit):
    pass


class Menubutton(unit):
    pass


class Message(unit):
    pass


class Radiobutton(unit):
    pass


class Scale(unit):
    pass



class Tk():
    def __init__(self,size=(600,400)):
        pygame.init()
        self.fps = 150
        self.fclock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size)
        self.background = False
        self.unit_group = pygame.sprite.Group()

    def title(self,title_name):
        pygame.display.set_caption(title_name)

    #def geometry(self,size):
    #    self = pygame.display.set_mode(size)

    def change_fps(self,fps):
        self.fps=fps

    def change_background(self,file_adr):
        self.background=pygame.image.load(file_adr).convert_alpha()

    def add_unit(self,unit):
        self.unit_group.add(unit)
    
    def remove_entity(self,unit):
        self.unit_group.remove(unit)

    def update(self,ticks):
        #+鼠标反应
        self.screen.fill((251,251,251))
        if self.background:
            self.screen.blit(self.background, (0, 0))
        self.unit_group.update(ticks)
        self.unit_group.draw(self.screen)

    def blit(self,image,image_rect):
        self.screen.blit(image,image_rect)


def mouse_judge(rect):
    x, y = pygame.mouse.get_pos()
    rx,ry,rw,rh = rect.left,rect.top,rect.width,rect.height
    if (rx <= x <=rx+rw)and(ry <= y <= ry +rh):
        return True
    return False


#all_command
def nothing():
    pass


#we can use "change_txt" here
#def command_change_txt(unit,text):
#    pass


def command_change_thing(unit,change_tup):
    change_dir={"size":unit.size,"text":unit.text,"font":unit.font,\
        "x":unit.rect.right,"y":unit.rect.top,"image":unit.image,\
            "x,y":(unit.rect.left,unit.rect.top)}
    change_dir[change_tup[0]]=change_tup[1]


def command_show_thing(unit,target_unit):
    pass


def command_cover(unit,target_unit):
    pass


def command_add_action_list(unit,action_list):
    pass


def start_screen(screen):
    while True:
        screen.fclock.tick(screen.fps)
        ticks=pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.update(ticks)
        #screen.blit(mouse_cursor, (x, y))
        pygame.display.update()


#tmp
def tmp_data():
    pass


def demo(screen):
    screen.title('My Tkinter')
    play=Txt_Label(screen,text="PLAY",size=100)

    screen.add_unit(play)



def main():
    screen=Tk()
    #测试函数
    demo(screen)
    start_screen(screen)


if __name__ == "__main__":
    main()