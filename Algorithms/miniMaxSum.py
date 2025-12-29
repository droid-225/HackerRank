def miniMaxSum(arr):
    for i in range(1, 5):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    min = arr[0] + arr[1] + arr[2] + arr[3]
    max = arr[1] + arr[2] + arr[3] + arr[4]

    print(arr)
    print(min, max)

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
