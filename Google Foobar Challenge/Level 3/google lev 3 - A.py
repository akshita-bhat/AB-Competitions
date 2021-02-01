def sol(n): 
    bit = 0
    while n>0: 
        bit = bit+ n%2
        n = n//2
    return bit 

def solution(n): 
    n = int(n)
    steps = 0
    while n!=1: 
        if n%2 == 0: 
            n = n//2
        elif n == 3: 
            n = n-1
        elif sol(n-1)<sol(n+1):
            n = n-1
        else: 
            n = n+1
        steps = steps+1
    return steps 

