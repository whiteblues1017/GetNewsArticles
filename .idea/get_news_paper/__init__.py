from nikkei import *
# from mainichi import *
# from asahi import *

ID=''
PASSWORD=''

def timestamp_separate():
    date ='2018/3/3'
    time='21:37'
    year=date[0:4]
    month=date[5:date.rfind('/')]
    date=date[date.rfind('/')+1:date.find(' ')]
    hour=time[0:time.find(':')]
    #minitus=date[date.find(':')+1:-1]

    print(date.find(' '))
    print(year+month+date)
    print(hour)


if __name__ == '__main__':
    date ='2018/3/3 21:37'
    nikkei.nikkei(ID,PASSWORD)
    #print(timestamp(date))
