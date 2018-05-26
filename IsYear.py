import datetime


class DATE():
    def __init__(self):
        i = datetime.datetime.now()


    def isyear(year):
        if (year%4 == 0) & (year%100 != 0):
            print("%d年是闰年" %year, end=" ")
        elif year%400 == 0:
            print("%d年是闰年" %year, end=" ")
        else:
            print("%d年不是闰年" %year, end=" ")

    def time():
        i = datetime.datetime.now()
        print("%s年%s月%s日" % (i.year, i.month, i.day))
        # print ("%s:%s:%s" % ( i.hour, i.minute,i.second) )
        m = int(i.minute)
        h = int(i.hour)
        s = int(i.second)
        if h < 10:
            print("0%s" % i.hour, end=":")
        else:
            print("%s" % i.hour, end=":")
        if m < 10:
            print("0%s" % i.minute, end=":")
        else:
            print("%s" % i.minute, end=":")
        if s < 10:
            print("0%s" % i.second)
        else:
            print("%s" % i.second)

    def chineseera():
        i = datetime.datetime.now()
        y=int(i.year)
        k=(y-1984)%10
        #print(k)
        if k == 0:
            print("甲", end="")
        elif k == 1:
            print("乙", end="")
        elif k == 2:
            print("丙", end="")
        elif k == 3:
            print("丁", end="")
        elif k == 4:
            print("戊", end="")
        elif k == 5:
            print("己", end="")
        elif k == 6:
            print("庚", end="")
        elif k == 7:
            print("辛", end="")
        elif k == 8:
            print("壬", end="")
        elif k == 9:
            print("癸", end="")
        l=(y-1984)%12
        #print(l)
        if l == 0:
            print("子", end="")
        elif l == 1:
            print("丑", end="")
        elif l == 2:
            print("寅", end="")
        elif l == 3:
            print("卯    ", end="")
        elif l == 4:
            print("辰", end="")
        elif l == 5:
            print("巳", end="")
        elif l == 6:
            print("午", end="")
        elif l == 7:
            print("未", end="")
        elif l == 8:
            print("申", end="")
        elif l == 9:
            print("酉", end="")
        elif l == 10:
            print("戌", end="")
        elif l == 11:
            print("戌", end="")
