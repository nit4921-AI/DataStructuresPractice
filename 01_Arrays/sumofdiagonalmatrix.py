'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:
    1 2 3
    4 5 6
    9 8 9
The left-to-right diagonal = 1 + 5 + 9 = 15. The
right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.
Function Description
Complete the diagonalDifference function in the editor below.
diagonalDifference takes the following parameter(s):
int arr[n][m]: an array of integers .
Returns
int: the absolute diagonal difference
Input Format
The first line contains a single integer, n, the number of rows and columns in the squarematrix arr.
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
Constraints'''
def diagonalDifference(arr):
    n = len(arr)
    p = 0
    q = 0
    
    for i in range(n):
        p += arr[i][i]
        q += arr[i][n - i - 1]
    
    return abs(p - q)


# Input
n = int(input("Enter size of matrix: "))
arr = []

print("Enter matrix rows:")
for _ in range(n):
    arr.append(list(map(int, input().split())))

# Output
result = diagonalDifference(arr)
print("Diagonal Difference:", result)