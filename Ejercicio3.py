entries = int(input())
while (entries > 0):
    n = int(input())
    for i in range(1, n+1):
        if(i * (i+1) >= 2*n):
            break
    k = ((i * (i+1))/2)
    if(k == n+1):
        i += 1
    print(i)
    entries -= 1
