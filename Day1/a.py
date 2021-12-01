def fun(file):
    lit = []
    with open(file) as f:
        for line in f:
            lit.append(int(line))
    counter = 0
    for i in range (1, len(lit)):
        if lit[i]>lit[i-1]:
            counter+=1
    return counter

file = "input.txt"
a = fun(file)
print(a)
    