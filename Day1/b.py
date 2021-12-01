def fun(file):
    lit = []
    fake = []
    with open(file) as f:
        for line in f:
            lit.append(int(line))
    counter = 0
    for i in range (2, len(lit)):
        fake.append(lit[i]+lit[i-1]+lit[i-2])
    for i in range (1, len(fake)):
        if fake[i]>fake[i-1]:
            counter+=1
    return counter

file = "input.txt"
a = fun(file)
print(a)
    