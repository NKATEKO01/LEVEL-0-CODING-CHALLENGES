def far_to_cel(x):
    far = (x - 32) * (5 / 9)
    return far

print(far_to_cel(15), "\xb0C")

def cel_to_far(y):
    cel = (y * 9 /5 ) + 32
    return cel

print(cel_to_far(15), "\xb0F")
