def staircase(n):
    for i in range(n):
        for y in range(n-i-1):
            print(' ', end='')
        for x in range(i + 1):
            print('#', end='')
        print('\n')            

if __name__ == '__main__':
    staircase(6)
