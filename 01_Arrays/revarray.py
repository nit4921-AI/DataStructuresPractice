# Reverse an Array
# Given an array of integers, return the array in reverse order as a list.
# Example:
# Input: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]

def reverseArray(a):
    result = []

    # Insert each element at the beginning of the new list
    for i in a:
        result.insert(0, i)

    return result


# Main program
if __name__ == "__main__":
    # Number of elements in array
    arr_count = int(input("Enter number of elements: "))

    # Input array elements
    arr = list(map(int, input("Enter array elements separated by space: ").split()))

    # Reverse the array
    res = reverseArray(arr)

    # Print reversed array
    print("Reversed Array:", res)