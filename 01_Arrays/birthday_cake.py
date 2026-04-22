def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0

    for i in candles:
        if i == tallest:
            count += 1

    return count


if __name__ == "__main__":
    candles = [3, 2, 1, 3]   # ✅ predefined array
    result = birthdayCakeCandles(candles)
    print(result)