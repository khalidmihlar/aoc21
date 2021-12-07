def fish(file):
    f = open(file)
    input = f.read()
    input = input.split(',')
    fish = []
    for i in input:
        fish.append(int(i))
    
    track = [0 for i in range(9)]
    for i in fish:
        track[i]+=1
    
    for _ in range(256):
        temp = [0 for _ in range(9)]
        for i in range(len(track)):
            if i==0:
                temp[8]+=track[0]
                temp[6]+=track[0]
            else:
                temp[i-1]+=track[i]
        track = temp   
    sum = 0
    for x in track:
        sum+=x
    return sum

yo = fish("input.txt")
print(yo)