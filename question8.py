def number_to_time(number):
    a = "hour"
    b = "hours"
    c = "minutes"
    d = "minute"
    hour = number // 60
    minutes = number % 60
    
    if hour > 1 and minutes == 1:
        print(str(hour), b + ", " + str(minutes), d)

    if (hour > 1 or hour == 0) and (minutes > 1 or minutes == 0):
        print(str(hour), b + ", " + str(minutes), c)

    if  hour == 1 and (minutes >1 or minutes == 0):
        print(str(hour), a + ",  "+ str(minutes), c) 

    if hour == 1 and minutes == 1:
        print(str(hour), a + ", " + str(minutes), d)


number_to_time(4)
