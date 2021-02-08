entries = int(input())
while (entries > 0):
    point = int(input())
    for i in range(1, point+1):
        if(i * (i+1) >= 2*point):
            break
    currentPoint = ((i * (i+1))/2)
    if(currentPoint == point+1):
        i += 1
    print(i)
    entries -= 1
