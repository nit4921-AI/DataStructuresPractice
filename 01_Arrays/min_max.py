def miniMaxSum(arr):
    total = sum(arr)
    min_sum = float('inf')
    max_sum = float('-inf')

    for n in arr:
        current = total - n
        min_sum = min(min_sum, current)
        max_sum = max(max_sum, current)

    print(min_sum, max_sum)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]   # ✅ predefined array
    miniMaxSum(arr)