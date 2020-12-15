import pygame
from pygame.locals import *
import sys
import os
import time

pygame.init()
pygame.display.set_caption("game")
SCREEN_RECT = Rect(0, 0, 640, 480)
screen = pygame.display.set_mode(SCREEN_RECT.size)
font = pygame.font.Font('ロゴたいぷゴシック.otf',30)
clock = pygame.time.Clock()
CS = 32
SCREEN_NCOL = SCREEN_RECT.width//CS
SCREEN_NROW = SCREEN_RECT.height//CS
SCREEN_CENTER_X = SCREEN_RECT.width//2//CS
SCREEN_CENTER_Y = SCREEN_RECT.height//2//CS

playerstatas=[]

def load_image(filename):
    filename = os.path.join("data", filename)
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image

def load_image_color(filename):
    filename = os.path.join("data", filename)
    image = pygame.image.load(filename)
    image = image.convert()
    colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey, RLEACCEL)
    return image

def get_image(sheet, x, y, width, height, useColorKey=False):
    image = pygame.Surface([width, height])
    image.blit(sheet, (0, 0), (x, y, width, height))
    image = image.convert()
    if useColorKey:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    #image = pygame.transform.scale(image, (32*2, 32*2))
    return image

def bigin():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
          if event.key == K_SPACE:
            return
      title=load_image("title.png")
      rect_title=title.get_rect()
      screen.blit(title,rect_title)
      text=font.render("スペースキーでゲーム開始",True,(0,0,0),300)
      screen.blit(text,[150,350])
      pygame.display.update()
      clock.tick(30)

def charamake():
  global playerstatas,player
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
          if event.key == K_1:
            playerstatas += [20,10,10,10,10,10,10,10,10]
            while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      playerstatas=[]
                      main()
                  if event.key == K_1:
                    player=Player("$yuhinamv146.png")
                    return player
                  if event.key == K_2:
                    player=Player("$yuhinamv218.png")
                    return player
              race=load_image("race.png")
              rect_race=race.get_rect()
              screen.blit(race,rect_race)
              note_h=load_image_color("note_h.png")
              (x,y)=(5,106)
              screen.blit(note_h,(x,y))
              text=font.render("主人公の性別を入力してください",True,(0,0,0),70)
              text2=font.render("1.男性",True,(0,0,0))
              text3=font.render("2.女性",True,(0,0,0))              
              screen.blit(text,[85,50])
              screen.blit(text2,[350,130])
              screen.blit(text3,[480,130])
              human_m=load_image("yh146.png")
              (x,y)=(305,190)
              screen.blit(human_m,(x,y))
              human_f=load_image("yh218.png")
              (x,y)=(430,203)
              screen.blit(human_f,(x,y))
              pygame.display.update()
              clock.tick(30)
          if event.key == K_2:
            playerstatas += [15,15,10,5,15,15,5,10,10]
            while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      playerstatas=[]
                      main()
                  if event.key == K_1:
                    player=Player("$yuhinamv042.png")
                    return player
                  if event.key == K_2:
                    player=Player("$yuhinamv043.png")
                    return player
              race=load_image("race.png")
              rect_race=race.get_rect()
              screen.blit(race,rect_race)
              note_e=load_image_color("note_e.png")
              (x,y)=(5,106)
              screen.blit(note_e,(x,y))
              text=font.render("主人公の性別を入力してください",True,(0,0,0),70)
              text2=font.render("1.男性",True,(0,0,0))
              text3=font.render("2.女性",True,(0,0,0))              
              screen.blit(text,[85,50])
              screen.blit(text2,[370,130])
              screen.blit(text3,[500,130])
              elf_f=load_image("yh043.png")
              (x,y)=(450,190)
              screen.blit(elf_f,(x,y))
              elf_m=load_image("yh042.png")
              (x,y)=(325,190)
              screen.blit(elf_m,(x,y))
              pygame.display.update()
              clock.tick(30)
          if event.key == K_3:
            playerstatas += [25,5,15,20,5,5,15,5,5]
            while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      playerstatas=[]
                      main()
                  if event.key == K_1:
                    player=Player("$yuhinamv019.png")
                    return player
                  if event.key == K_2:
                    player=Player("$yuhinamv064.png")
                    return player
              race=load_image("race.png")
              rect_race=race.get_rect()
              screen.blit(race,rect_race)
              note_d=load_image_color("note_d.png")
              (x,y)=(5,106)
              screen.blit(note_d,(x,y))
              text=font.render("主人公の性別を入力してください",True,(0,0,0),70)
              text2=font.render("1.男性",True,(0,0,0))
              text3=font.render("2.女性",True,(0,0,0))              
              screen.blit(text,[85,50])
              screen.blit(text2,[370,130])
              screen.blit(text3,[500,130])
              dwarf_f=load_image("yh064.png")
              (x,y)=(450,190)
              screen.blit(dwarf_f,(x,y))
              dwarf_m=load_image("yh019.png")
              (x,y)=(325,190)
              screen.blit(dwarf_m,(x,y))
              pygame.display.update()
              clock.tick(30)
          if event.key == K_5:
            playerstatas += [30,20,5,5,20,5,5,5,5]
            while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      playerstatas=[]
                      main()
                  if event.key == K_1:
                    player=Player("$yuhinamv156.png")
                    return player
                  if event.key == K_2:
                    player=Player("$yuhinamv296.png")
                    return player
              race=load_image("race.png")
              rect_race=race.get_rect()
              screen.blit(race,rect_race)
              note_p=load_image_color("note_p.png")
              (x,y)=(5,106)
              screen.blit(note_p,(x,y))
              text=font.render("主人公の性別を入力してください",True,(0,0,0),70)
              text2=font.render("1.男性",True,(0,0,0))
              text3=font.render("2.女性",True,(0,0,0))              
              screen.blit(text,[85,50])
              screen.blit(text2,[350,130])
              screen.blit(text3,[480,130])
              plantman_f=load_image("yh296.png")
              (x,y)=(430,190)
              screen.blit(plantman_f,(x,y))
              plantman_m=load_image("yh156.png")
              (x,y)=(305,190)
              screen.blit(plantman_m,(x,y))
              pygame.display.update()
              clock.tick(30)
          if event.key == K_4:
            playerstatas += [20,10,10,15,0,5,10,20,10]
            while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      playerstatas=[]
                      main()
                  if event.key == K_1:
                    player=Player("$yuhinamv237.png")
                    return player
                  if event.key == K_2:
                    player=Player("$yuhinamv341.png")
                    return player
              race=load_image("race.png")
              rect_race=race.get_rect()
              screen.blit(race,rect_race)
              note_b=load_image_color("note_b.png")
              (x,y)=(5,106)
              screen.blit(note_b,(x,y))
              text=font.render("主人公の性別を入力してください",True,(0,0,0),70)
              text2=font.render("1.男性",True,(0,0,0))
              text3=font.render("2.女性",True,(0,0,0))              
              screen.blit(text,[85,50])
              screen.blit(text2,[370,130])
              screen.blit(text3,[500,130])
              beastman_f=load_image("yh341.png")
              (x,y)=(450,200)
              screen.blit(beastman_f,(x,y))
              beastman_m=load_image("yh237.png")
              (x,y)=(310,168)
              screen.blit(beastman_m,(x,y))
              pygame.display.update()
              clock.tick(30)
          if event.key == K_6:
            playerstatas += [20,10,25,10,5,10,10,5,5]
            while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      playerstatas=[]
                      main()
                  if event.key == K_1:
                    player=Player("$yuhinamv329.png")
                    return player
                  if event.key == K_2:
                    player=Player("$yuhinamv073.png")
                    return player
              race=load_image("race.png")
              rect_race=race.get_rect()
              screen.blit(race,rect_race)
              note_dra=load_image_color("note_dra.png")
              (x,y)=(5,106)
              screen.blit(note_dra,(x,y))
              text=font.render("主人公の性別を入力してください",True,(0,0,0),70)
              text2=font.render("1.男性",True,(0,0,0))
              text3=font.render("2.女性",True,(0,0,0))              
              screen.blit(text,[85,50])
              screen.blit(text2,[370,130])
              screen.blit(text3,[500,130])
              dragonoid_f=load_image("yh073.png")
              (x,y)=(450,200)
              screen.blit(dragonoid_f,(x,y))
              dragonoid_m=load_image("yh329.png")
              (x,y)=(305,180)
              screen.blit(dragonoid_m,(x,y))
              pygame.display.update()
              clock.tick(30)
          if event.key == K_7:
            playerstatas += [15,10,10,5,15,15,10,15,5]
            while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      playerstatas=[]
                      main()
                  if event.key == K_1:
                    player=Player("$yuhinamv084.png")
                    return player
                  if event.key == K_2:
                    player=Player("$yuhinamv085.png")
                    return player
              race=load_image("race.png")
              rect_race=race.get_rect()
              screen.blit(race,rect_race)
              note_w=load_image_color("note_w.png")
              (x,y)=(5,106)
              screen.blit(note_w,(x,y))
              text=font.render("主人公の性別を入力してください",True,(0,0,0),70)
              text2=font.render("1.男性",True,(0,0,0))
              text3=font.render("2.女性",True,(0,0,0))              
              screen.blit(text,[85,50])
              screen.blit(text2,[370,130])
              screen.blit(text3,[500,130])
              wedy_f=load_image("yh085.png")
              (x,y)=(450,180)
              screen.blit(wedy_f,(x,y))
              wedy_m=load_image("yh084.png")
              (x,y)=(315,180)
              screen.blit(wedy_m,(x,y))
              pygame.display.update()
              clock.tick(30)
    charamake=load_image("charamake.png")
    rect_charamake=charamake.get_rect()
    screen.blit(charamake,rect_charamake)
    text=font.render("主人公の種族を入力して下さい",True,(0,0,0),70)
    text2=font.render("1.ヒューマン",True,(0,0,0),70)
    text3=font.render("2.エルフ",True,(0,0,0),70)
    text4=font.render("3.ドワーフ",True,(0,0,0),70)
    text5=font.render("4.獣人",True,(0,0,0),70)
    text6=font.render("5.植物人",True,(0,0,0),70)
    text7=font.render("6.竜人",True,(0,0,0),70)
    text8=font.render("7.ウェディ",True,(0,0,0),70)
    screen.blit(text,[110,50])
    screen.blit(text2,[250,90])
    screen.blit(text3,[250,130])
    screen.blit(text4,[250,170])
    screen.blit(text5,[250,210])
    screen.blit(text6,[250,250])
    screen.blit(text7,[250,290])
    screen.blit(text8,[250,330])
    pygame.display.update()
    clock.tick(30)

def menu():
  while True:
    text=font.render("メニュー",True,(255,255,255),30)
    text2=font.render("1ステータス",True,(255,255,255),30)
    pygame.draw.rect(screen, (0,0,0), (20,20,200,120))
    screen.blit(text,[25,25])
    screen.blit(text2,[25,60])
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == QUIT:          
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_z:
          return
        if event.key == K_1:
            print("[HP,MP,耐性,筋力,魔力,知力,技巧,速さ,幸運]=",playerstatas)
DIR_DOWN = 0
DIR_LEFT = 1
DIR_RIGHT = 2
DIR_UP = 3
ANIM_WAIT_COUNT = 8

class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        sheet = load_image(filename)
        self.images = [[], [], [], []]
        for row in range(0, 4):
            for col in [0, 1, 2, 1]:
                self.images[row].append(get_image(sheet, 0 + 32 * col, 0 + 32 * row, 32, 32, True))
        self.image = self.images[DIR_DOWN][0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_CENTER_X * CS
        self.rect.y = SCREEN_CENTER_Y * CS
        self.frame = 0
        self.anim_count = 0
        self.dir = DIR_DOWN
        self.wx, self.wy = 1, 1
    def update(self):
        self.anim_count += 1
        if self.anim_count >= ANIM_WAIT_COUNT:
            self.anim_count = 0
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
        self.image = self.images[self.dir][self.frame]

class Map:
    def __init__(self, screen, filename, player):
        self.ncol = 0
        self.nrow = 0
        self.screen = screen
        self.player = player
        self.mapData = []
        self.readMap(filename)
        self.sheet0 = load_image("pipo-map001.png")
        self.sheet1 = load_image("pipo-map001_at-umi.png")
        self.sheet2 = load_image("pipo-map001_at-yama2.png")
        self.sheet3 = load_image("base.png")
        self.images = []
#平和な大陸
        self.images.append([self.sheet1, 0, 0])  # naraku(0)
        self.images.append([self.sheet0, 0, 0])  # shiba (1)
        self.images.append([self.sheet0, 2, 9])  # gate (2)
        self.images.append([self.sheet1, 0, 4])  # umi (3)
        self.images.append([self.sheet0, 1, 1])  # mori (4)
        self.images.append([self.sheet0, 1, 7])  # town_left (5)
        self.images.append([self.sheet0, 2, 7])  # town_right (6)


        
    def readMap(self, filename):
        with open(filename) as fi:
            line = fi.readline()
            self.ncol, self.nrow = [int(tok) for tok in line.split(",")]
            for row in range(self.nrow):
                line = fi.readline()
                self.mapData.append([int(tok) for tok in line.split(",")])
    def drawImage(self, idx, sx, sy):
        sheet, x, y = self.images[idx]
        self.screen.blit(sheet, (sx * 32, sy * 32), (x * 32, y * 32, 32, 32))
    def draw(self):
        screen_wx = self.player.wx - SCREEN_CENTER_X
        screen_wy = self.player.wy - SCREEN_CENTER_Y
        for sy in range(SCREEN_NROW):
            for sx in range(SCREEN_NCOL):
                wx = screen_wx + sx
                wy = screen_wy + sy
                if not (0 <= wx < self.ncol) or not (0 <= wy < self.nrow):
                    self.drawImage(0, sx, sy)  # naraku
                else:
                    idx = self.mapData[wy][wx]
                    self.drawImage(1, sx, sy)  # shiba
                    self.drawImage(idx, sx, sy)
    def can_move_at(self, wx, wy):
        if not (0 <= wx < self.ncol) or not (0 <= wy < self.nrow):
            return False
        idx = self.mapData[wy][wx]
        if idx == 0 or idx == 3:  # naraku umi
            return False
        return True

def main():
    bigin()
    charamake()
    group = pygame.sprite.RenderUpdates()
    group.add(player)
    fieldMap = Map(screen, "field01.map", player)
    player.wx += 5
    player.wy += 5

    
    while True:
        clock.tick(60)
        screen.fill((0, 255, 0))
        fieldMap.draw()
        group.update()
        group.draw(screen)
        pygame.display.update()
        clock.tick(30)
        pressed_key=pygame.key.get_pressed()



        if pressed_key[K_s]:
            if fieldMap.can_move_at(player.wx, player.wy + 1):
                player.dir = DIR_DOWN
                player.wy += 1
                time.sleep(0.12)
        if pressed_key[K_a]:
            if fieldMap.can_move_at(player.wx - 1, player.wy):
                player.dir = DIR_LEFT
                player.wx -= 1
                time.sleep(0.12)
        if pressed_key[K_d]:
            if fieldMap.can_move_at(player.wx + 1, player.wy):
                player.dir = DIR_RIGHT
                player.wx += 1
                time.sleep(0.12)
        if pressed_key[K_w]:
            if fieldMap.can_move_at(player.wx, player.wy - 1):
                player.dir = DIR_UP
                player.wy -= 1
                time.sleep(0.12)
        if pressed_key[K_x]:
            menu()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
if __name__ == '__main__':
    main()
