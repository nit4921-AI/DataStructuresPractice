# between_two_sets.py

def getTotalX(a, b):

    count = 0

    # Check numbers from max(a) to min(b)

    for i in range(max(a), min(b) + 1):

        valid = True

        # Condition 1:
        # All elements in a should divide i

        for j in a:

            if i % j != 0:
                valid = False
                break

        # Condition 2:
        # i should divide all elements in b

        for j in b:

            if j % i != 0:
                valid = False
                break

        # If both conditions are true

        if valid:
            count += 1

    return count


# Predefined arrays

a = [2, 4]
b = [16, 32, 96]


# Function call

result = getTotalX(a, b)

print("Total numbers between two sets:", result)