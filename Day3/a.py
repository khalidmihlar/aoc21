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
    values = []
    with open(file) as f:
        for line in f:
            values.append(str(line))
    zero = [0] * (len(values[0])-1)
    one = [0] * (len(values[0])-1)
    for i in range (0, len(values)):
        temp = values[i];
        for j in range (0, len(temp)-1): 
            if (values[i][j] == '1'):
                one[j]+=1
            else:
                zero[j]+=1         
    ans = ""
    other = ""
    for i in range(0, len(zero)):
        if (zero[i]<one[i]):
            ans+="1"
            other+="0"
        else:
            ans+="0"
            other+="1"
    fun = binaryToDecimal(int(ans))*binaryToDecimal(int(other))
    print(zero, one)
    
a = submarine("input.txt")