import math
n = 100

ctr = 0
    
for num in range(n+1):
    if num <= 1:
        continue
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        ctr += 1
        
        
print(ctr, n-ctr)        

result = math.factorial(ctr)*math.factorial(n-ctr)
offset = 10**9 + 7 
print(result%offset)

