import itertools as it
'''
n = 15
# METHOD 1
count = 0
print('n: ', n)
dic= {1:0, 2:0}
for i in range(2,n//2):
    y = [x for x in list(it.combinations(range(n), i)) if sum(x)==n and 0 not in x]
    count+=len(y)
    print(y)
    #print(i, len(y))
print('count: ', count)
# METHOD 2

def partitions(n): 
    p = [0] * (n + 1) 
    p[0] = 1
    for i in range(1, n + 1): 
        k = 1
        while ((k * (3 * k - 1)) / 2 <= i) : 
            p[i] += ((1 if k % 2 else -1) * 
                    p[i - (k * (3 * k - 1)) // 2]) 
            if (k > 0): 
                k *= -1
            else: 
                k = 1 - k 
    return p
print(partitions(3))
# METHOD 3
def f(n):
    di = [0]
    for i in range(1,n):
        if i%2==0:
            x = (n//i)+1
            print(x)
            di.append(x)
        else:
            x = n//i+n%i
            print(x)
            di.append(x)
    return di
print(f(3))

def solution(n):
    count = 0
    two_pair_dictionary = {1:0,2:0}
    
    for i in range(3,n+1):
        if i%2==0:
            x = int(i//2)-1
            two_pair_dictionary[i] = x
        else:
            x = int(i//2)        
            two_pair_dictionary[i] = x
    count=two_pair_dictionary[n]
    print(two_pair_dictionary)
    if n%2== 0:
        for i in range(3, int(n/2)+1):
            count+=two_pair_dictionary[i]
        #for i in reversed(range(int(n/2)+1),3):
            
    else:
        for i in range(3, int(i//2)+1):
            count+=two_pair_dictionary[i]
    return count    
'''

def helper(height, step, grid):
    if step < 1:
        return 1
    if grid[height][step]:
        return grid[height][step]
    if height > step:
        return 0
    grid[height][step] = helper(height + 1, step, grid) + helper(height + 1, step - height, grid) 
    return grid[height][step]

def solution(n):
    grid = [[0 for x in range(n + 2)] for x in range(n + 2)]
    return helper(1, n, grid) - 1

print(solution(200))









