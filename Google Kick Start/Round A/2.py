T = int(input()) # 2
for i in range(T):
    input2 = input()
    N,K,P = input2.split(' ') #2 4 5 
    N = int(N)
    K = int(K)
    P = int(P)
    for i in range(N):
        temp = input()  #10 10 100 30
        beauty = temp.split(' ')
        print(beauty)
    #find index of max number 
    
    count = 0
    #print('Case #'+ str(i+1)+ ': ' + str(count))