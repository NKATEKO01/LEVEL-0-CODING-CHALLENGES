def max_num(a,b,c,):
    if (a > b and a > c):
        return a
    if (c > b and c > a):
       return c
    if (b > a and b > c):
      return b

print (max_num(1,33,8))
