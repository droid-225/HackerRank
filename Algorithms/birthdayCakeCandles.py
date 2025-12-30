def birthdayCakeCandles(candles):
    max_val = max(candles)
    i = 0

    for candle in candles:
        if candle == max_val:
            i += 1
    
    return i

if __name__ == '__main__':
    candles = [3, 2, 1, 3]

    result = birthdayCakeCandles(candles)

    print(result)