# encoding=utf8
'''
import datetime
from IsYear import DATE
i = datetime.datetime.now()

DATE.time()
DATE.isyear(int(i.year))
DATE.chineseera()

'''
#--coding:utf-8--
import sys, pygame, math, random
from pygame.locals import *
from datetime import datetime
#from time import sleep



def print_text(font, x, y, text, color=(0, 0, 0)):
    imgtext = font.render(text, True, color)
    screen.blit(imgtext, (x, y))


def time():
    #print("%s年%s月%s日" % (i.year, i.month, i.day))
    #print ("%s:%s:%s" % ( i.hour, i.minute,i.second) )
    print_text(font, 600, 180, str(years) + "年"+str(months)+"月"+str(days)+"日")
    #print_text(font, 600, 180,u"年")

    m = int(minutes)
    h = int(hours)
    s = int(seconds)
    if h < 10:
        #print("0%s" % i.hour, end=":")
        print_text(font, 600, 250, "0"+str(hours) + ":")
    else:
        #print("%s" % i.hour, end=":")
        print_text(font, 600, 250, str(hours)+":")
    if m < 10:
        #print("0%s" % i.minute, end=":")
        print_text(font, 680, 250, "0"+str(minutes)+":")
    else:
        #print("%s" % i.minute, end=":")
        print_text(font, 680, 250, str(minutes)+":")
    if s < 10:
        #print("0%s" % i.second)
        print_text(font, 760, 250, "0"+str(seconds))
    else:
        #print("%s" % i.second)
        print_text(font, 760, 250, str(seconds))


def wrap_angle(angle):
    return abs(angle % 360)

def printclock():
    time()
    # draw the minutes hand
    min_angle = wrap_angle(minutes * (360 / 60) - 90)
    min_angle = math.radians(min_angle)
    min_x = math.cos(min_angle) * (radius - 60)
    min_y = math.sin(min_angle) * (radius - 60)
    target = (pos_x + min_x, pos_y + min_y)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 10)

    # draw the seconds hand
    sec_angle = wrap_angle(seconds * (360 / 60) - 90)
    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius - 30)
    sec_y = math.sin(sec_angle) * (radius - 30)
    target = (pos_x + sec_x, pos_y + sec_y)
    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 8)

    # draw the hours hand
    hour_angle = wrap_angle(hours * (360 / 12) - 90) + (wrap_angle(minutes * (360 / 60)))/12
    hour_angle = math.radians(hour_angle)
    hour_x = math.cos(hour_angle) * (radius - 120)
    hour_y = math.sin(hour_angle) * (radius - 120)
    target = (pos_x + hour_x, pos_y + hour_y)
    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 10)

def isyear(year):
    if (year%4 == 0) & (year%100 != 0):
        #print("%d年是闰年" %year, end=" ")
        print_text(font1, 600, 320, "闰年")
    elif year%400 == 0:
        #print("%d年是闰年" %year, end=" ")
        print_text(font1, 600, 320, "闰年")
    else:
        #print("%d年不是闰年" %year, end=" ")
        print_text(font1, 600, 320, "不是闰年")
# main


pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("CLOCK")
font = pygame.font.SysFont('SimHei', 60)
font1 = pygame.font.SysFont('SimHei', 40)
orange = 250, 128, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100
black = 0,0,0

pos_x = 300
pos_y = 300
radius = 250
angle = 360
s=1
# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_s]:
        s = 0
        years=input("请输入年：")
        months=input("请输入月：")
        days=input("请输入日：")
        hours= input("请输入时：")
        minutes = input("请输入分：")
        seconds= input("请输入秒：")
        seconds = int(seconds)
        minutes=int(minutes)
        hours=int(hours)

    screen.fill(white)

    # draw circle
    pygame.draw.circle(screen, black, (pos_x, pos_y), radius, 8)

    # draw the clock number 1-12
    for n in range(1, 13):
        angle = math.radians(n * (360 / 12) - 90)
        x = math.cos(angle) * (radius - 25) - 15
        y = math.sin(angle) * (radius - 25) - 15
        print_text(font1, pos_x + x, pos_y + y, str(n))
    i = datetime.now()
    # get the time of day
    if(s):

        hours = i.hour % 12
        minutes = i.minute
        seconds = i.second
        years=i.year
        months=i.month
        days=i.day
        printclock()

    else:
        printclock()
        if i.second!=last:
            seconds+=1

        #时间操作
        if(seconds>59):
            minutes+=1
            seconds=0

        #pygame.time.Clock().tick(1)
        #sleep(1)

    last=i.second
    isyear(int(years))
    # draw the center
    pygame.draw.circle(screen, black, (pos_x, pos_y), 10)

    #print_text(font, 600, 150, str(hours) + ":" + str(minutes) + ":" + str(seconds))


    print_text(font1, 600, 390, "按S进行设置")
    pygame.display.update()

