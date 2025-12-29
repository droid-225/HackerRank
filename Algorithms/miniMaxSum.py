def miniMaxSum(arr):
    total = sum(arr)
    min = total - max(arr)
    max = total - min(arr)

    print(min, max)

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
