def fun(file):
    words = []
    dir = []
    dist = []
    depth = 0
    hori = 0
    with open(file) as f:
        for line in f:
            words.append(line)
    for n in words:
        for m in n.split():
            if m.isdigit():
                dist.append(int(m))
            else:
                dir.append(m)
    counter = 0;
    for i in dir:
        if i == "forward":
            hori+=dist[counter]
        elif i == "down":
            depth+=dist[counter]
        else:
            depth-=dist[counter]
        counter+=1
    return depth*hori


a = fun("input.txt")
print(a)