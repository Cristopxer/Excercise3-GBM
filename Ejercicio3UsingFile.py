f = open('Input.txt')
entries = int(f.readline())
while (entries > 0):
    point = int(f.readline())
    for i in range(1, point+1):
        if(i * (i+1) >= 2*point):
            break
    currentPoint = ((i * (i+1))/2)
    if(currentPoint == point+1):
        i += 1
    print(f'for input: {point} Number of Jumps = {i}')
    entries -= 1
