from datetime import datetime

#Use datetime library and calculate the difference between both and get is in seconds
def time_delta(t1, t2):
    t1=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return (str(int(abs((t1-t2).total_seconds()))))