import statistics

def crabby(file):
    f = open(file)
    input = f.read()
    input = list(map(int,open(file).read().split(',')))
    print(input)
    media = statistics.median(input)
    bruh = sum(abs(i-media) for i in input)
    print(bruh)
    
yo = crabby("dummy.txt")