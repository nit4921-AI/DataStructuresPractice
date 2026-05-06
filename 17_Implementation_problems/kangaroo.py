# kangaroo.py

def kangaroo(x1, v1, x2, v2):

    # If one kangaroo is ahead
    # and also jumps farther,
    # they will never meet

    if (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
        return "NO"

    # Check positions after jumps

    for i in range(10000):

        if x1 == x2:
            return "YES"

        x1 = x1 + v1
        x2 = x2 + v2

    return "NO"


# Predefined values

x1 = 0
v1 = 3

x2 = 4
v2 = 2


# Function call

result = kangaroo(x1, v1, x2, v2)

print(result)