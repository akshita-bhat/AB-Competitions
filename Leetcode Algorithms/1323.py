

num = 9999

def max69num(num):
    x = [int(i) for i in list(str(num))]
    for i in range(len(x)):
        if x[i]==6:
            x[i] = 9
            break
    
    p = ''.join(str(i) for i in x)
    return int(p)

print(max69num(num))
    




