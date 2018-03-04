from nikkei import *
# from mainichi import *
# from asahi import *


if __name__ == '__main__':
    #nikkei.nikkei(ID,PASSWORD)
    date ='2018/3/3 21:37'
    year=date[0:4]
    month=date[5:date.rfind('/')]
    date=date[date.rfind('/')+1:date.find(' ')]
    hour=date[date.find(' '):-1]
    minitus=date[date.find(':')+1:-1]

    print(date.find(' '))
    print(year+month+date+hour)
