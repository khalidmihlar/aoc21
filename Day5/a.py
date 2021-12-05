import re

def five(file):
    temp = []
    first = []
    second = []
    f = open(file)
    input = f.read()
    cords = input.split("\r\n")
    for i in range(len(cords)):
        cords[i] = map(int,re.findall(r"\d+", cords[i]))
    for i in cords:
        temp = [i[0],i[1]]
        first.append(temp)
        temp = [i[2],i[3]]
        second.append(temp)
   
    maxX = 0;
    maxY = 0;
    for i in range(len(first)):
        if (max(first[i][0], second[i][0])>maxX):
            maxX = max(first[i][0], second[i][0])
        if (max(first[i][1], second[i][1])>maxY):
            maxY = max(first[i][1], second[i][1])
    maxX+=1
    maxY+=1
    arr = [[0]*maxX for _ in range(maxY)] 
   
    for i in range(len(first)):
        if first[i][0]==second[i][0]:
            for j in range(min(first[i][1],second[i][1]), max(first[i][1],second[i][1])+1):
                arr[j][first[i][0]]+=1
        elif first[i][1]==second[i][1]:
            for j in range(min(first[i][0],second[i][0]), max(first[i][0],second[i][0])+1):
                arr[first[i][1]][j]+=1
        else:
            continue
        
    count = 0
    for i in arr:
        for j in i:
            if j>1:
              count+=1  
    return count
        
        
    
print(five("input.txt"))