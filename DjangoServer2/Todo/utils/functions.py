from datetime import datetime as dt

def getDate():
    now = dt.now()
    date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    return date

def getTimeNow():
    pass

def getDateTime():
    now = dt.now()
    dateTime = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute)
    return dateTime

def getTimeMillis():
    pass

if __name__ == '__main__':
    print(getDateTime())