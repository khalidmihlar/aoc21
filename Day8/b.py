def num(file):
    f = open(file)
    input = f.read()
    output = []
    count = 0
    for x in input.splitlines():
        fun = x.split("|")
        output.append(fun[1].split(" "))
    for x in output:
        for y in range(1, len(x)):
            if len(x[y])==2 or len(x[y])==3 or len(x[y])==4 or len(x[y])==7:
                count+=1
    print(count)
funny = num("input.txt")    