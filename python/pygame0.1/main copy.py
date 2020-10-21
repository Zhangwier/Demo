#导入模块
import pygame
import sys
import random
from pygame.locals import *
from pygame import Vector2
#初始化
pygame.init()
fps = 150
fclock = pygame.time.Clock()
Time_screen=0
version=1.0
max_anim=20#最大生物容量
max_move_all=20#最大动态生物容量
max_mod=1#最大mod数
max_ctrs=6#最大按键数
max_num=12#最大生物词条
max_car=7#最大载具词条
max_goods=10#最大物品词条
#设置游戏窗口
size=  width,height = 600,400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game by 1.0")
#类
class Map():
    background=0
    square=0
    def load(self,filename):
        2
class MySprite(pygame.sprite.Sprite):
    def __init__(self, target,property=0):
        pygame.sprite.Sprite.__init__(self) #基类的init方法
        self.target_surface = target#暂无用
        self.image = None#前屏幕展示图
        self.master_image = None#原图
        self.rect = pygame.Rect(0,0,0,0)
        self.frame = 0#当前为第几图
        self.old_frame = -1#上次为第几图(用于判断是否更新)
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1#每行几个
        self.last_time = 0#上次更新时间
        self.frame_list={}
        self.update_way=0

        self.direction=[0,0]#面向
        self.speed=[0,0]
        self.speed_offset = 1
        self.id=0
        self.name='unknown'
        self.weight=random.randint(80,200)
        self.energy=self.weight*10*300*20
        self.integrity={}
        self.intelligence=0
        self.state=0
        self.run_state=0

        self.property=0
        self.signal=0
        #anim
        if self.property==1:
            self.talent={'memory':0,'learn':0,'fight':0,'logic':0,'beauty':0,'speech':0,'friend':0,'find':0}
            self.memory={}
            self.skills={}
            self.value={'speed':0,'option':0,'sight':0}#可变数值
            self.thing={}#当前所有物
            self.update_way = -1
        #car
        if self.property==2:
            self.active=''
            self.fuel={'type':0,'value':0}
            self.space={'passenger':[]}
            self.function={'passenger':0}
            self.update_way = -1
        #goods(不可踩)
        if self.property==0:
            self.use={'att':0,'eat':0,'space':[],'throw':0,'open':0,'kick':0,'kiss':0,'pick':0,'put':0}
            self.value={}
            self.nature={'maker':0,'stuff':0,'time':0,'site':0}
            self.update_way = 0

    def load(self,filename,width,height,columns,row=0):
        self.master_image = pygame.image.load(filename).convert_alpha()#保留透明，提高bilt速度
        if row != 0:
            f_w=row*width
            r_h=(row-1)*height
            rect = (0,r_h,f_w,height)
            self.master_image = self.master_image.subsurface(rect)
        self.frame_width = width
        self.frame_height = height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1
        self.rect=pygame.Rect(0,0,self.frame_width,self.frame_height)
        if columns > 0 :
            self.update_way=-1
        else:
            self.update_way=0
    #更新动画帧,rate:每rate更新一次图片
    def update(self,current_time, rate=200):
        #xy坐标
        global world
        self.action(current_time)
        self.rect = self.rect.move(self.speed[0],self.speed[1])
        collide_list = pygame.sprite.spritecollide(self,world.group,False)
        for i in collide_list:
            if i.property==3:
                self.rect = self.rect.move(-self.speed[0],-self.speed[1])
                self.speed=[0,0]
        if self.rect.left < 0:
            self.rect.left=0
        if self.rect.right > width:
            self.rect.left=width-self.rect.width
        if self.rect.top < 0:
            self.rect.top=0
        if self.rect.bottom > height:
            self.rect.top=height-self.rect.height
        if self.energy<0 :#死亡检测
            world.remove_entity(self)
        if self.update_way == 0 :#不更新
            screen.blit(self.image,self.rect)
            return 0
        elif self.update_way == -1:#永远循环
            if current_time > self.last_time + rate:#判断是否更新图片
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
                self.last_time = current_time
            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
                self.image = self.master_image.subsurface(rect)
                self.old_frame = self.frame
            screen.blit(self.image,self.rect)
            return 0
        elif self.update_way == -2:#左右方向
            if current_time > self.last_time + rate:
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
                self.last_time = current_time
            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
                self.image = self.master_image.subsurface(rect)
                if self.direction[0] == -1 or self.speed[0] == -self.speed_offset:
                    self.image=pygame.transform.flip(self.image, True, False)
                self.old_frame = self.frame
            screen.blit(self.image,self.rect)
            return 0
        elif self.update_way == -3:#循环则尽
            if current_time > self.last_time + rate:#判断是否更新图片
                self.frame += 1
                if self.frame > self.last_frame:
                    world.remove_entity(self)
                    return 0
                self.last_time = current_time
            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
                self.image = self.master_image.subsurface(rect)
                self.old_frame = self.frame
            screen.blit(self.image,self.rect)
            return 0
        elif self.update_way == 1:#移动循环,有朝向,未定义动作
            if self.direction == [0,0]:
                self.frame = 1
            elif self.speed == [0,0]:
                self.frame = self.frame % 4
            elif self.speed[0] != 0 and self.speed[1] != 0:#斜向前进
                1#还没做
            else :
                #变向检测
                if self.speed[0] == self.speed_offset and self.frame%4 != 3:
                    self.frame=3
                if self.speed[0] == -self.speed_offset and self.frame%4 != 0:
                    self.frame=0
                if self.speed[1] == self.speed_offset and self.frame%4 != 1:
                    self.frame=1
                if self.speed[1] == -self.speed_offset and self.frame%4 != 2:
                    self.frame=2
                if current_time > self.last_time + rate:
                    self.frame += 4
                    if self.frame > self.last_frame:
                        self.frame = self.frame % 4
                    self.last_time = current_time
            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
                self.image = self.master_image.subsurface(rect)
                self.old_frame = self.frame
            screen.blit(self.image,self.rect)
            return 0
        elif self.update_way == 2:#带有动作
            if self.state in self.frame_list:
                1
            else:
                2
            if self.direction == [0,0]:
                self.frame = 1
            elif self.speed == [0,0]:
                self.frame = self.frame % 4
            elif self.speed[0] != 0 and self.speed[1] != 0:#斜向前进
                1#还没做
            else :
                #变向检测
                if self.speed[0] == self.speed_offset and self.frame%4 != 3:
                    self.frame=3
                if self.speed[0] == -self.speed_offset and self.frame%4 != 0:
                    self.frame=0
                if self.speed[1] == self.speed_offset and self.frame%4 != 1:
                    self.frame=1
                if self.speed[1] == -self.speed_offset and self.frame%4 != 2:
                    self.frame=2
                if current_time > self.last_time + rate:
                    self.frame += 4
                    if self.frame > self.last_frame:
                        self.frame = self.frame % 4
                    self.last_time = current_time
            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
                self.image = self.master_image.subsurface(rect)
                self.old_frame = self.frame
            screen.blit(self.image,self.rect)
            return 0
    def action(self,current_time):
        rate=random.randint(150,400)
        moverate=random.randint(0,50)
        if self.intelligence == -1 :
            return 0
        if self.intelligence == 0:
            return 0
        if self.intelligence == 1 and current_time > self.last_time + rate:
            self.speed[0]=random.sample([0,-self.speed_offset,self.speed_offset],1)[0]
            self.speed[1]=random.sample([0,-self.speed_offset,self.speed_offset],1)[0]
            if moverate < 5:
                self.speed[0]=0
            if self.speed[0] > 0 :
                self.direction[0]=1
            elif self.speed[0] < 0:
                self.direction[0]=-1
            if moverate < 5:
                self.speed[1]=0
            if self.speed[1] > 0 :
                self.direction[1]=1
            elif self.speed[1] < 0:
                self.direction[1]=-1
    def manctr(self,kel):
        1
class World():
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.entities = {} # Store all the entities
        self.entity_id = 0 # Last entity id assigned
        self.background = pygame.surface.Surface(size).convert()
        self.background.fill((255, 255, 255))
    def mapload(self,filename,filename2,width,height,columns):
        self.cell = pygame.image.load(filename).convert_alpha()
        self.background = pygame.image.load(filename2).convert_alpha()
        self.cell_width = width
        self.cell_height = height
        self.cell_columns = columns
    def add_entity(self, entity,x='none',y='none'):
        # 增加一个新的实体
        self.entities[self.entity_id] = entity
        self.entity_id += 1
        self.group.add(entity)
        if x != 'none' :
            entity.rect=pygame.Rect(x,y,entity.frame_width,entity.frame_height)
    def add_cell(self,frame,x,y):
        cell=MySprite(screen)
        fx = (frame % self.cell_columns) * self.cell_width
        fy = (frame // self.cell_columns) * self.cell_height
        rect = ( fx, fy, self.cell_width, self.cell_height )
        cell.master_image = self.cell.subsurface(rect)
        cell.image=cell.master_image
        cell.rect=pygame.Rect(x,y,self.cell_width,self.cell_height)
        cell.property=3
        return cell
    def remove_entity(self, entity):
        #del self.entities[entity.id]
        self.group.remove(entity)
    def get(self, entity_id):
        # 通过id给出实体，没有的话返回None
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None
    def process(self, ticks):
        # 处理和绘制世界中的每一个实体
        screen.blit(self.background, (0, 0))
        self.group.update(ticks)
        self.group.draw(screen)
    def get_close_entity(self, name, location, range=100.):
        # 通过一个范围寻找之内的所有实体
        location = Vector2(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:
                    return entity
        return None
#函数
def is_rect(pos,rect):
    x,y =pos
    rx,ry,rw,rh = rect
    if (rx <= x <=rx+rw)and(ry <= y <= ry +rh):
        return True
    return False
def Mod():
    1
#数据
mouse_cursor = pygame.image.load('py\\pygame\\mics\\mouse.png')
def man():
    man = MySprite(screen,1)
    num=random.randint(1,16)
    if num < 10:
        num='0'+str(num)
    else:
        num=str(num)
    adr="py\\pygame\\character\\sample_character_num.png".replace('num',num)
    man.load(adr,16,32,columns=4)
    man.update_way=1
    man.intelligence=1
    return man
def gator():
    gator = MySprite(screen,1)
    adr='py\\pygame\\character\\gator.png'
    gator.load(adr,46,49,columns=4)
    gator.update_way=-2
    gator.intelligence=2
    gator.talent={'memory':5,'learn':3,'fight':10,'logic':3,'beauty':6,'speech':0,'friend':1,'find':0}
    gator.skills={'fire':7,'fly':4}
    gator.value={'speed':2,'option':0,'sight':100}
    return gator
def ant():
    ant = MySprite(screen,1)
    adr='py\\pygame\\character\\ant.png'
    ant.load(adr,37,31,columns=8)
    ant.update_way=-2
    ant.intelligence=1
    return ant
def worm():
    worm = MySprite(screen,1)
    adr='py\\pygame\\character\\characters.png'
    worm.load(adr,32,32,columns=4,row=4)
    worm.update_way=-2
    worm.intelligence=1
    return worm
def Priest():
    Priest = MySprite(screen,1)
    adr='py\\pygame\\character\\Buff Totem Sprite Sheet.png'
    Priest.load(adr,32,22,columns=8)
    Priestm.update_way=-2
    Priest.intelligence=1
    Priest.frame_list={'appear':(2,5),'dead':(4,8),'jump':(3,8),'other':(1,8)}
    return Priest
def boom():
    boom = MySprite(screen,0)
    adr='py\\pygame\\mics\\boom.png'
    boom.load(adr,24,23,columns=4)
    boom.update_way=-3
    return boom
def heart():
    heart = MySprite(screen,0)
    adr='py\\pygame\\mics\\heart.png'
    heart.load(adr,14,13,columns=8)
    heart.update_way=-3
    return heart
def shoot():
    shoot = MySprite(screen,0)
    adr='py\\pygame\\mics\\shoot.png'
    shoot.load(adr,12,7,columns=3)
    shoot.update_way=-1
    shoot.intelligence=1
    return shoot
def beginmap():
    begin = World()
    begin.mapload('py\\pygame\\cell\\sheet1.png','py\\pygame\\background\\country-platform-back.png',16,16,10)
    for i in range(39):
        exec(f'cell_{i}=begin.add_cell(51,(i-1)*16,280)')
        exec(f'begin.add_entity(cell_{i})')
    #for j in range(1,7):
    #    for i in range(39):
    #        exec(f'cell_{i*(j+1)}=begin.add_cell(51,(i-1)*16,280+j*16)')
    #        exec(f'begin.add_entity(cell_{i*(j+1)})')
    return begin

begin = beginmap()
man1=man()
gator1=gator()
gator1.run_state=1
gator2=gator()
begin.add_entity(man1)
begin.add_entity(gator1)
begin.add_entity(gator2)

#进程
while True:
    fclock.tick(fps)
    ticks=pygame.time.get_ticks()
    #人物界面设置
    play1=gator1
    play1.intelligence=0
    world=begin
    #指令接受
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                play1.speed[1] = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                play1.speed[0] = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                play1.speed[0] = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                play1.speed[1] = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                play1.speed[1] = -play1.speed_offset
                play1.direction[1] = -1
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                play1.speed[0] = -play1.speed_offset
                play1.direction[0] = -1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                play1.speed[0] = play1.speed_offset
                play1.direction[0] = 1
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                play1.speed[1] = play1.speed_offset
                play1.direction[1] = 1
    #物理规则
    #鼠标设置
    x, y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    if event.type == pygame.MOUSEBUTTONDOWN:
        1
    #屏幕刷新
    world.process(ticks)
    screen.blit(mouse_cursor, (x, y))
    pygame.display.update()

pygame.quit()