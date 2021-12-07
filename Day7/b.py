import statistics
import math

def crabby(file):
    f = open(file)
    input = f.read()
    input = list(map(int,open(file).read().split(',')))
    bruh = int(min(sum(abs(i-j)*(abs(i-j)+1)/2 for i in input) for j in range(max(input))))
    print(bruh)   
    
        
    
yo = crabby("input.txt")