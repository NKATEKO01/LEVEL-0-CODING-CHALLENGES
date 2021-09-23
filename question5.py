#Task5

def triangle_area(a,b,c):#print triangle area
    s = ((a + b + c)/2)
    area = ((s*(s-a)*(s-b)*(s-c))**0.5)
    return area
print(triangle_area(3,4,5))
