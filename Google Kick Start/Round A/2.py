T = int(input()) # 2
for i in range(T):
    input2 = input()
    N,K,P = input2.split(' ') #2 4 5 
    N = int(N)
    K = int(K)
    P = int(P)
    for i in range(N):
        temp = input()  #10 10 100 30
        temp = temp.split(' ')
        beauty=[]
        for i in range(K):
            beauty.append(int(temp[i]))
        #print(beauty)
        ind_max_beaut = beauty.index(max(beauty))
        print(ind_max_beaut)
    #find index of max number 
    
    count = 0
    #print('Case #'+ str(i+1)+ ': ' + str(count))