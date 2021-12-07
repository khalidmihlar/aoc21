def fish(file):
    f = open(file)
    input = f.read()
    input = input.split(',')
    fish = []
    for i in input:
        fish.append(int(i))
    
    count = 0
    for i in range(80):    
        for j in range(len(fish)):
            fish[j]-=1
            if (fish[j]==-1):
                fish[j]=6
                fish.append(8)
    print(len(fish))

yo = fish("dummy.txt")