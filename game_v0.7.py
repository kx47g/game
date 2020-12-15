import pygame
from pygame.locals import *
import sys
import os
import time
from random import randint

pygame.init()
pygame.display.set_caption("game")
SCREEN_RECT = Rect(0, 0, 640, 480)
screen = pygame.display.set_mode(SCREEN_RECT.size)
pygame.mixer.init(frequency = 44100)
font = pygame.font.Font('ロゴたいぷゴシック.otf',30)
clock = pygame.time.Clock()
CS = 32
SCREEN_NCOL = SCREEN_RECT.width//CS
SCREEN_NROW = SCREEN_RECT.height//CS
SCREEN_CENTER_X = SCREEN_RECT.width//2//CS
SCREEN_CENTER_Y = SCREEN_RECT.height//2//CS
T1,T2=1,150
potion = 1


def load_sound(filename):
    filename = os.path.join("data",filename)
    sound = pygame.mixer.music.load(filename)

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


#playerstatas = [最大HP MAXHP,HP,最大MP MAXMP,MP,耐性 RES,筋力 STR,魔力 MGC,知力 INT,技巧 TEC,速さ QUI,幸運 LUK]
class playerstatas:
    MAXHP = 0
    MAXMP = 0
    HP = 0
    MP = 0
    RES = 0
    STR = 0
    MGC = 0
    INT = 0
    TEC = 0
    QUI = 0
    LUK = 0
class humanstatas:
    MAXHP = 20
    MAXMP = 10
    HP = 20
    MP = 10
    RES = 10
    STR = 10
    MGC = 10
    INT = 10
    TEC = 10
    QUI = 10
    LUK = 10
class elfstatas:
    MAXHP = 15
    MAXMP = 15
    HP = 15
    MP = 15
    RES = 10
    STR = 5
    MGC = 15
    INT = 15
    TEC = 5
    QUI = 10
    LUK = 10
class dowarfstatas:
    MAXHP = 25
    MAXMP = 5
    HP = 25
    MP = 5
    RES = 15
    STR = 20
    MGC = 5
    INT = 5
    TEC = 15
    QUI = 5
    LUK = 5
class beastmanstatas:
    MAXHP = 20
    MAXMP = 10
    HP = 20
    MP = 10
    RES = 10
    STR = 15
    MGC = 0
    INT = 5
    TEC = 10
    QUI = 20
    LUK = 10
class plantmanstatas:
    MAXHP = 30
    MAXMP = 20
    HP = 30
    MP = 20
    RES = 5
    STR = 5
    MGC = 20
    INT = 5
    TEC = 5
    QUI = 5
    LUK = 5
class dragonoidstatas:
    MAXHP = 20
    MAXMP = 10
    HP = 20
    MP = 10
    RES = 25
    STR = 10
    MGC = 5
    INT = 10
    TEC = 10
    QUI = 5
    LUK = 5
class wedystatas:
    MAXHP = 15
    MAXMP = 10
    HP = 15
    MP = 10
    RES = 10
    STR = 5
    MGC = 15
    INT = 15
    TEC = 10
    QUI = 15
    LUK = 5


class slime:
    HP = 10
    MP = 5
    RES = 8
    STR = 7
    MGC = 0
    INT = 2
    TEC = 5
    QUI = 5
    LUK = 5
    NAME = "スライム"
    IMAGE=load_image("slime.png")

class wolf:
    HP = 15
    MP = 5
    RES = 8
    STR = 10
    MGC = 0
    INT = 2
    TEC = 5
    QUI = 7
    LUK = 5
    NAME = "ウルフ"
    IMAGE=load_image("wolf.png")
    


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
            playerstatas=humanstatas
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
            playerstatas=elfstatas
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
            playerstatas=dowarfstatas
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
          if event.key == K_4:
            playerstatas=beastmanstatas
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
          if event.key == K_5:
            playerstatas=plantmanstatas
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
          if event.key == K_6:
            playerstatas=dragonoidstatas
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
            playerstatas=wedystatas
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

def gameover():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    pygame.draw.rect(screen, (0,0,0), (0,0,640,480))
    text=font.render("GAMEOVER…",True,(255,255,255),70)
    screen.blit(text,[230,100])
    pygame.display.update()
    time.sleep(5)
    return main()
    
def battle():
    global monsterstatas,X,Y,potion,playerstatas
    battle_image = load_image("charamake.png")
    rect_battleimg=battle_image.get_rect()
    screen.blit(battle_image,rect_battleimg)
    monsterimg= monsterstatas.IMAGE
    monstername=str(monsterstatas.NAME)
    rect_monster=monsterimg.get_rect()
    rect_monster.move_ip(X,Y)
    screen.blit(monsterimg,rect_monster)
    pygame.draw.rect(screen, (0,0,0), (20,360,470,110))
    pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
    monstername=str(monsterstatas.NAME)
    text = font.render(monstername,True,(255,255,255))
    screen.blit(text,[25,370])
    text2 = font.render("があらわれた！",True,(255,255,255))
    screen.blit(text2,[225,370])
    pygame.display.update()
    time.sleep(1.2)
    while True:
        rect_battleimg=battle_image.get_rect()
        screen.blit(battle_image,rect_battleimg)
        monsterimg= monsterstatas.IMAGE
        rect_monster=monsterimg.get_rect()
        rect_monster.move_ip(X,Y)
        screen.blit(monsterimg,rect_monster)

        pygame.draw.rect(screen, (0,0,0), (20,280,130,80))
        pygame.draw.rect(screen, (0,0,0), (20,360,470,110))
        pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
        monstername=str(monsterstatas.NAME)
        playerHP=str(playerstatas.HP)
        playerMP=str(playerstatas.MP)
        text = font.render(playerHP,True,(255,255,255))
        screen.blit(text,[90,285])
        text4 = font.render(playerMP,True,(255,255,255))
        screen.blit(text4,[90,325])
        text5 = font.render("HP",True,(255,255,255))
        screen.blit(text5,[30,285])
        text6 = font.render("MP",True,(255,255,255))
        screen.blit(text6,[30,325])
        text2 = font.render("1 攻撃",True,(255,255,255))
        screen.blit(text2,[505,370])
        text3 = font.render("2 逃げる",True,(255,255,255))
        screen.blit(text3,[505,400])
        text3 = font.render("3 薬草",True,(255,255,255))
        screen.blit(text3,[505,430])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_2:
                    pQUI,mQUI=playerstatas.QUI,monsterstatas.QUI
                    escape=pQUI/mQUI
                    if  escape <= 1:
                        pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                        pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                        text = font.render("逃げられなかった！",True,(255,255,255))
                        screen.blit(text,[25,370])
                        pygame.display.update()
                        time.sleep(1.2)
                    if  escape > 1 and escape <= 1.5:
                        escape2 = randint(1,2)
                        if escape2 == 1:
                            pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                            pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                            text = font.render("逃げられなかった！",True,(255,255,255))
                            screen.blit(text,[25,370])
                            pygame.display.update()
                            time.sleep(1.2)
                        else:
                            return playerstatas
                    if escape > 1.5 and escape <= 2:
                        escape2 = randint(1,4)
                        if escape2 == 1:
                            pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                            pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                            text = font.render("逃げられなかった！",True,(255,255,255))
                            screen.blit(text,[25,370])
                            pygame.display.update()
                            time.sleep(1.2)
                        else:
                            return playerstatas
                    if escape > 2:
                        return playerstatas
                if event.key == K_1:

                    pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                    pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                    text4 = font.render("あなたの攻撃！",True,(255,255,255))
                    screen.blit(text4,[25,370])
                    pygame.display.update()
                    time.sleep(1)
                    
                    STR,RES,TEC,QUI,LUKp,LUKm=playerstatas.STR,monsterstatas.RES,playerstatas.TEC,monsterstatas.QUI,playerstatas.LUK,monsterstatas.LUK
                    ATK = STR
                    DEF = RES
                    AVO = QUI+LUKm/100
                    HIT = (100-AVO)+TEC+LUKp/100
                    DMG = ATK-DEF//5
                    monsterstatas.HP-=DMG
                    damage=str(DMG)
                    
                    pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                    pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                    monstername=str(monsterstatas.NAME)
                    text3 = font.render(monstername,True,(255,255,255))
                    screen.blit(text3,[25,370])
                    text6 = font.render("に　　のダメージを与えた!",True,(255,255,255))
                    screen.blit(text6,[225,370])
                    text7 = font.render(damage,True,(255,255,255))
                    screen.blit(text7,[265,370])
                    pygame.display.update()
                    time.sleep(1)
                    
                    if monsterstatas.HP <= 0:
                      while True:
                        for event in pygame.event.get():
                          if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                        pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                        monstername=str(monsterstatas.NAME)
                        text3 = font.render(monstername,True,(255,255,255))
                        screen.blit(text3,[25,370])
                        text6 = font.render("を倒した!",True,(255,255,255))
                        screen.blit(text6,[225,370])
                        pygame.display.update()
                        Sound = "sound_win.mp3"
                        load_sound(Sound)
                        pygame.mixer.music.play(1)
                        time.sleep(5)
                        return playerstatas
                    
                    STR,RES,TEC,QUI,LUKp,LUKm=monsterstatas.STR,playerstatas.RES,monsterstatas.TEC,playerstatas.QUI,monsterstatas.LUK,playerstatas.LUK
                    pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                    pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                    text8 = font.render(monstername,True,(255,255,255))
                    screen.blit(text8,[25,370])
                    text9 = font.render("の攻撃！",True,(255,255,255))
                    screen.blit(text9,[225,370])
                    pygame.display.update()
                    time.sleep(1)
                    
                    ATK = STR
                    DEF = RES
                    AVO = QUI+LUKm/100
                    HIT = (100-AVO)+TEC+LUKp/100
                    DMG = ATK-DEF//5
                    playerstatas.HP-=DMG
                    pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                    pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                    damage=str(DMG)
                    text10 = font.render("あなたに　　のダメージを与えた!",True,(255,255,255))
                    screen.blit(text10,[25,370])
                    text11 = font.render(damage,True,(255,255,255))
                    screen.blit(text11,[145,370])
                    pygame.display.update()
                    time.sleep(1)

                if event.key == K_3:
                        pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                        pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                        potion -= 1
                        if potion < 0:
                            potion = 0
                            text4 = font.render("薬草を持っていない…",True,(255,255,255))
                            screen.blit(text4,[25,370])
                            pygame.display.update()
                            time.sleep(1)

                        else:
                          text4 = font.render("薬草の効果でHP20回復！",True,(255,255,255))
                          screen.blit(text4,[25,370])
                          pygame.display.update()
                          time.sleep(1)
                          playerstatas.HP += 20
                          if playerstatas.MAXHP < playerstatas.HP:
                            playerstatas.HP = playerstatas.MAXHP

                        

                        STR,RES,TEC,QUI,LUKp,LUKm=monsterstatas.STR,playerstatas.RES,monsterstatas.TEC,playerstatas.QUI,monsterstatas.LUK,playerstatas.LUK
                        pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                        pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                        text8 = font.render(monstername,True,(255,255,255))
                        screen.blit(text8,[25,370])
                        text9 = font.render("の攻撃！",True,(255,255,255))
                        screen.blit(text9,[225,370])
                        pygame.display.update()
                        time.sleep(1)
                    
                        ATK = STR
                        DEF = RES
                        AVO = QUI+LUKm/100
                        HIT = (100-AVO)+TEC+LUKp/100
                        DMG = ATK-DEF//5
                        playerstatas.HP-=DMG
                        pygame.draw.rect(screen, (0,0,0), (20,360,480,110))
                        pygame.draw.rect(screen, (0,0,0), (500,360,130,110))
                        damage=str(DMG)
                        text10 = font.render("あなたに　　のダメージを与えた!",True,(255,255,255))
                        screen.blit(text10,[25,370])
                        text11 = font.render(damage,True,(255,255,255))
                        screen.blit(text11,[145,370])
                        pygame.display.update()
                        time.sleep(1)

def shop_w():
    global W
    playerstatas.STR = playerstatas.STR-W
    while True:
        bukiya=load_image("bukiya.png")
        rect_bukiya=bukiya.get_rect()
        rect_bukiya.move_ip(290,105)
        screen.blit(bukiya,rect_bukiya)

        pygame.draw.rect(screen, (0,0,0), (20,375,280,160))
        text=font.render("ここは武器の店だ",True,(255,255,255),30)
        screen.blit(text,[25,400])
        text2=font.render("何を買うかね",True,(255,255,255),30)
        screen.blit(text2,[25,440])
        pygame.display.update()
    
        for event in pygame.event.get():
          if event.type == QUIT:          
            pygame.quit()
            sys.exit()
          if event.type == KEYDOWN:
            if event.key == K_SPACE:
              pygame.draw.rect(screen, (0,0,0), (20,125,300,140))
              text=font.render("1 木の剣 +5",True,(255,255,255),30)
              screen.blit(text,[25,130])
              text2=font.render("2 名刀・斬鉄 +10",True,(255,255,255),30)
              screen.blit(text2,[25,170])
              text3=font.render("3 フラガラッハ +20",True,(255,255,255),30)
              screen.blit(text3,[25,210])
              pygame.display.update()
            if event.key == K_1:
                W = 5
                playerstatas.STR = playerstatas.STR+W
                pygame.draw.rect(screen, (255,255,255), (100,150,350,60))
                text=font.render("木の剣を購入した",True,(0,0,0),30)
                screen.blit(text,[110,170])
                pygame.display.update()
                time.sleep(1.5)
                return playerstatas,W
            if event.key == K_2:
                W = 10
                playerstatas.STR = playerstatas.STR+W
                pygame.draw.rect(screen, (255,255,255), (100,150,350,60))
                text=font.render("名刀・斬鉄を購入した",True,(0,0,0),30)
                screen.blit(text,[110,170])
                pygame.display.update()
                time.sleep(1.5)
                return playerstatas,W
            if event.key == K_3:
                W = 20
                playerstatas.STR = playerstatas.STR+W
                pygame.draw.rect(screen, (255,255,255), (100,150,350,60))
                text=font.render("フラガラッハを購入した",True,(0,0,0),30)
                screen.blit(text,[110,170])
                pygame.display.update()
                time.sleep(1.5)
                return playerstatas,W
            if event.key == K_z:
              return

def shop_d():
    global potion
    while True:
        douguya=load_image("douguya.png")
        rect_douguya=douguya.get_rect()
        rect_douguya.move_ip(290,105)
        screen.blit(douguya,rect_douguya)

        pygame.draw.rect(screen, (0,0,0), (20,375,280,160))
        text=font.render("ここは道具店だよ",True,(255,255,255),30)
        screen.blit(text,[25,400])
        text2=font.render("何が必要かな",True,(255,255,255),30)
        screen.blit(text2,[25,440])
        pygame.display.update()
    
        for event in pygame.event.get():
          if event.type == QUIT:          
            pygame.quit()
            sys.exit()
          if event.type == KEYDOWN:
            if event.key == K_SPACE:
              pygame.draw.rect(screen, (0,0,0), (20,125,300,50))
              text=font.render("1 薬草",True,(255,255,255),30)
              screen.blit(text,[25,130])
              pygame.display.update()
            if event.key == K_1:
                pygame.draw.rect(screen, (255,255,255), (100,150,350,60))
                text=font.render("薬草を購入した",True,(0,0,0),30)
                potion += 1
                screen.blit(text,[110,170])
                pygame.display.update()
                time.sleep(1.5)
                return potion
            if event.key == K_z:
              return
        

def menu():
  while True:
    text=font.render("メニュー",True,(255,255,255),30)
    text2=font.render("1ステータス",True,(255,255,255),30)
    pygame.draw.rect(screen, (0,0,0), (20,20,200,110))
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
          while True:
            plmaxhp = str(playerstatas.MAXHP)
            plhp = str(playerstatas.HP)
            plmaxmp = str(playerstatas.MAXMP)
            plmp = str(playerstatas.MP)
            plres = str(playerstatas.RES)
            plstr = str(playerstatas.STR)
            plmgc = str(playerstatas.MGC)
            plint = str(playerstatas.INT)
            pltec = str(playerstatas.TEC)
            plqui = str(playerstatas.QUI)
            plluk = str(playerstatas.LUK)
            pygame.draw.rect(screen, (0,0,0), (70,140,560,230))
            text3=font.render('最大HP　HP　最大MP　MP　耐性　筋力',True,(255,255,255))
            screen.blit(text3,[75,150])
            text4=font.render('魔力　知力　技巧　速さ　幸運',True,(255,255,255))
            screen.blit(text4,[75,250])
            text5=font.render(plmaxhp,True,(255,255,255))
            screen.blit(text5,[105,200])
            text6=font.render(plhp,True,(255,255,255))
            screen.blit(text6,[205,200])
            text7=font.render(plmaxmp,True,(255,255,255))
            screen.blit(text7,[300,200])
            text8=font.render(plmp,True,(255,255,255))
            screen.blit(text8,[405,200])
            text9=font.render(plres,True,(255,255,255))
            screen.blit(text9,[485,200])
            text9=font.render(plstr,True,(255,255,255))
            screen.blit(text9,[575,200])
            text10=font.render(plmgc,True,(255,255,255))
            screen.blit(text10,[90,300])
            text11=font.render(plint,True,(255,255,255))
            screen.blit(text11,[180,300])
            text12=font.render(pltec,True,(255,255,255))
            screen.blit(text12,[270,300])
            text13=font.render(plqui,True,(255,255,255))
            screen.blit(text13,[360,300])
            text14=font.render(plluk,True,(255,255,255))
            screen.blit(text14,[450,300])
            pygame.display.update()
            for event in pygame.event.get():
              if event.type == QUIT:          
                pygame.quit()
                sys.exit()
              if event.type == KEYDOWN:
                if event.key == K_z:
                    return
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
        self.images.append([self.sheet0, 1, 9])  # sinden (7)
        self.images.append([self.sheet0, 6, 2])  # doukutu (8)
#町
        self.images.append([self.sheet3, 0, 46])  # yuka (9)
        self.images.append([self.sheet3, 1, 46])  # renga (10)
        self.images.append([self.sheet3, 0, 98])  # table (11)
        self.images.append([self.sheet3, 2, 112])  # bedue (12)
        self.images.append([self.sheet3, 2, 113])  # bedsita (13)
        self.images.append([self.sheet3, 0, 95])  # bukiya (14)
        self.images.append([self.sheet3, 1, 95])  # bouguya (15)
        self.images.append([self.sheet3, 2, 95])  # douguya (16)
        self.images.append([self.sheet3, 1, 115])  # isu (17)
        self.images.append([self.sheet3, 3, 98])  # tablesita (18)
        self.images.append([self.sheet3, 0, 1])   # bukiya (19)
        self.images.append([self.sheet3, 1, 1])   # douguya (20)

      
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
        if idx == 0 or idx == 3 or idx == 10 or idx ==11 or idx == 18:  # naraku umi renga table
            return False
        return True

def main():
    global monsterstatas,X,Y,T1,T2,B,Sound,W
    W = 0
    bigin()
    charamake()
    group = pygame.sprite.RenderUpdates()
    group.add(player)
    fieldMap = Map(screen, "field01.map", player)
    player.wx += 10
    player.wy += 5
    B=100
    Sound = "bgm_field.mp3"
    load_sound(Sound)
    pygame.mixer.music.play(1)
    
    while True:
        clock.tick(30)
        screen.fill((0, 255, 0))
        fieldMap.draw()
        group.update()
        group.draw(screen)
        pygame.display.update()
        monstertable=randint(T1,T2)
        
        if monstertable <= 70:
            monsterstatas = slime()
            X,Y = 100,100
        if monstertable > 70 and monstertable <= 100:
            monsterstatas = wolf()
            X,Y = 160,20
            
        battlestart=randint(1,B)
        if battlestart == 1:
            Sound = "bgm_battle.mp3"
            load_sound(Sound)
            pygame.mixer.music.play(1)
            battle()
            Sound = "bgm_field.mp3"
            load_sound(Sound)
            pygame.mixer.music.play(1)
        
        pressed_key=pygame.key.get_pressed()
        if player.wx == 29 and player.wy == 33 or player.wx == 30 and player.wy == 33:
            player.wy += 89
            B = 100000000
            Sound = "bgm_toun.mp3"
            load_sound(Sound)
            pygame.mixer.music.play(1)
        if player.wx == 28 and player.wy == 127 or player.wx == 29 and player.wy == 127 or player.wx == 30 and player.wy == 127 or player.wx == 31 and player.wy == 127:
            player.wy -= 93
            T1,T2 = 1,200
            B = 100
            Sound = "bgm_field.mp3"
            load_sound(Sound)
            pygame.mixer.music.play(1)

        if player.wx == 19 and player.wy == 124 and pressed_key[K_SPACE]:
            playerstatas.HP += 999
            playerstatas.MP += 999
            Sound = "sound_inn.mp3"
            load_sound(Sound)
            pygame.mixer.music.play(1)
            time.sleep(5)
            Sound = "bgm_toun.mp3"
            load_sound(Sound)
            pygame.mixer.music.play(1)
            
        if playerstatas.HP > playerstatas.MAXHP:
            playerstatas.HP = playerstatas.MAXHP
        if playerstatas.MP > playerstatas.MAXMP:
            playerstatas.MP = playerstatas.MAXMP
        if player.wx == 45 and player.wy == 120 and pressed_key[K_SPACE]:
            shop_w()
        if player.wx == 37 and player.wy == 120 and pressed_key[K_SPACE]:
            shop_d()


  

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
