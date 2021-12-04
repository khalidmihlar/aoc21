def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal   


def submarine(file):
    leastcommon = []
    mostcommon = []
    with open(file) as f:
        leastcommon = f.read().splitlines()
    mostcommon = leastcommon[:]
    zero = [0] * (len(leastcommon[0]))
    one = [0] * (len(mostcommon[0]))
    check = ''
    lcint = []
    mcint = []
    #least common remover
    for i in range (0, 12):
        if len(leastcommon)==1:
            break;
        for j in range (0, len(leastcommon)): 
            if leastcommon[j][i] == '1':
                one[i]+=1
            else:
                zero[i]+=1 
        if (one[i]<zero[i]):
            check = '0'
        else:
            check = '1'
        for j in range (0, len(leastcommon)):
            if leastcommon[j][i] == check:
                lcint.append(j)
        for j in reversed(lcint):
            leastcommon.pop(j)   
        lcint = []
          
    zero = [0] * (len(leastcommon[0]))
    one = [0] * (len(mostcommon[0]))
    for i in range (0, 12):
        if len(mostcommon)==1:
            break;
        for j in range (0, len(mostcommon)): 
            if mostcommon[j][i] == '1':
                one[i]+=1
            else:
                zero[i]+=1 
        print(zero[i],one[i])
        print(i)
        if (one[i]>=zero[i]):
            check = '0'
        else:
            check = '1'
        for j in range (0, len(mostcommon)):
            if mostcommon[j][i] == check:
                mcint.append(j)
        for j in reversed(mcint):
            mostcommon.pop(j)   
        mcint = []
        print(mostcommon)
        print(len(mostcommon))
        print("")
    
    ayo = int(mostcommon[0], base=2)
    ayo2 = int(leastcommon[0], base=2)
    print(ayo*ayo2)
    
    
a = submarine("input.txt")