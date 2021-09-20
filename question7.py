#task7

def f_to_c(x): #Far to Cel
    far = ((x - 32) * (5/9))
    return far

print(f_to_c(15),"\xb0C")

def c_to_f(y): #Cel to far
    cel = ((y * 9/5) + 32 )
    return cel

print(c_to_f(15),"\xb0F")
