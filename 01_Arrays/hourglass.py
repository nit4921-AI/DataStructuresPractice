# Hourglass Sum Problem
# Given a 6x6 2D array, calculate the maximum hourglass sum.
#
# Hourglass pattern:
# a b c
#   d
# e f g

def hourglassSum(arr):
    maxsum = float('-inf')  # Handles negative values

    # Check all possible hourglasses
    for i in range(4):
        for j in range(4):

            # Calculate sum of current hourglass
            sumglass = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2]
                + arr[i+1][j+1]
                + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )

            # Update maximum sum
            if sumglass > maxsum:
                maxsum = sumglass

    return maxsum


# Main Program
if __name__ == "__main__":
    arr = []

    print("Enter 6 rows with 6 integers each:")

    # Input 6x6 array
    for _ in range(6):
        row = list(map(int, input().split()))
        arr.append(row)

    # Find maximum hourglass sum
    result = hourglassSum(arr)

    print("Maximum Hourglass Sum:", result)