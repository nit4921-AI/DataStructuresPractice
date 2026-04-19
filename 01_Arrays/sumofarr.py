'''Find the sum of all elements in an array.
Example
a = [1, 2, 3, 4, 5]
The sum of the elements is 1 + 2 + 3 + 4 + 5 = 15
Function Description
Complete the simpleArraySum function in the editor below.
simpleArraySum has the following parameter(s):
int ar[n]: an array of integers
Returns
'''
print(total)
def aVeryBigSum(ar):
    """
    Calculate the sum of very large integers in an array.

    Example Input:
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    Expected Output:
    5000000015
    """
    total=0
    for i in ar:
        total+=i
    return total


# Sample test case
ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))