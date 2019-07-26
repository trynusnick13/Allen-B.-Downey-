"""

Power

"""

def ispower(a, b):

    if a % b == 1 and a == 1:

        return True

    elif a % b == 0:

        return(ispower(a/b, b))
    else:

        return False

print(ispower(9, 3))