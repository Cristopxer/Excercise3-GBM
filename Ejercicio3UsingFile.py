f = open('Input.txt')
entries = int(f.readline())
while (entries > 0):
    n = int(f.readline())
    for i in range(1, n+1):
        if(i * (i+1) >= 2*n):
            break
    k = ((i * (i+1))/2)
    if(k == n+1):
        i += 1
    print(f'for input: {n} Number of Jumps = {i}')
    entries -= 1
