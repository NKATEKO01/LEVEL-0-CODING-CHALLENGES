x = 301
a = "hour"
b = "hours"
c = "minutes"
d = "minute"
hour = x//60
minutes = x%60

def number_convert(x):
    if hour > 1 and minutes<=1:
        print(str(hour,),(b) +", "+ str(minutes),(d))

    if hour > 1 and minutes>1:
        print(str(hour,),(b) +", "+ str(minutes),(c))

    if  hour < 2 and minutes >1:
        print(str(hour,),(a) +", "+ str(minutes),(c)) 

    if hour < 2 and minutes<=1:
        print(str(hour,),(a) +", "+ str(minutes),(d))


number_convert(x)
