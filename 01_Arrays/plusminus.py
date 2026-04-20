''' Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.'''

def plusMinus(arr):
    n = len(arr)
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    zero = n - pos - neg

    return pos/n, neg/n, zero/n


# Example test
arr = [-4, 3, -9, 0, 4, 1]
a, b, c = plusMinus(arr)

print(f"{a:.6f}")
print(f"{b:.6f}")
print(f"{c:.6f}")