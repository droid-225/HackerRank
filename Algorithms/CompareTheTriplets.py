def compareTriplets(a, b):
    score = [0, 0]
    i = 0

    while i < 3:
        if a[i] < b[i]:
            score[1] += 1
        elif a[i] > b[i]:
            score[0] += 1
        i += 1

    return score

if __name__ == '__main__':
    a = [5, 6, 7]

    b = [3, 6, 10]

    result = compareTriplets(a, b)

    print(result)
