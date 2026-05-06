# apples_oranges.py

def countApplesAndOranges(s, t, a, b, apples, oranges):

    apple_count = 0
    orange_count = 0

    # Count apples
    for i in apples:
        position = a + i

        if s <= position <= t:
            apple_count += 1

    # Count oranges
    for i in oranges:
        position = b + i

        if s <= position <= t:
            orange_count += 1

    print("Apples on house:", apple_count)
    print("Oranges on house:", orange_count)


# Predefined values

# House starts at 7 and ends at 11
s = 7
t = 11

# Apple tree position
a = 5

# Orange tree position
b = 15

# Distances apples fall
apples = [-2, 2, 1]

# Distances oranges fall
oranges = [5, -6]


# Function call
countApplesAndOranges(s, t, a, b, apples, oranges)