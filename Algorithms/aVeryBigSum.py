def aVeryBigSum(ar):
    sum = 0

    for int in ar:
        sum += int

    return sum

if __name__ == '__main__':
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    result = aVeryBigSum(ar)

    print(result)
