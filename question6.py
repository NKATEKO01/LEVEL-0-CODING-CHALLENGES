#Task6


def max_num(a,b,c,):#print max number
    if (a > b and a > c):
        return a
    if (c > b and c > a):
       return c
    if (b > a and b > c):
      return b

print (max_num(1,33,8))

#bonus
def maximus(*t):#print max number
    max=t[0]
    for i in t:
        if i > t:
            t=i
    return max

print(max(1,288.5547,21,3))