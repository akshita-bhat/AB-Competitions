num_test = int(input())
for i in range(num_test):
    input2 = input()
    N,B = input2.split(' ')
    N = int(N)
    B = int(B)
    count = 0
    prices = input()
    temp = prices.split(' ')
    x = []
    for z in temp:
        x.append(int(z))
    x.sort()
    for d in range(N):
        bal = B-int(x[d]) 
        if bal>=0:
            count+=1
            B=bal          
    print('Case #'+ str(i+1)+ ': ' + str(count))