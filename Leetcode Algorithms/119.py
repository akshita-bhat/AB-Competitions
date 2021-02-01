rowIndex = 1
#print(temp)
'''
n = 0 => [1]
n = 1 => [1,1]
n = 2 => [1,2,__1] 
n = 3 => [1,3,__3,1]
n = 4 => [1,4,6,__4,1]
n = 5 => [1,5,10,10,__5,1]
n = 6 => [1,6,15,20,__15,6,1]

if n is even 
-> odd number of elements in list
    exactly half + 1 elements can be generated n = 4, [1,4,6], then [4,1] combine => [1,4,6,4,1]  
    
if n if odd 
-> even number of elements in list 
    exactly half numbers can be generated if n = 3, [1,3] then [3,1] combine => [1,3,3,1]
'''

grid = [[0 for i in range(rowIndex+1)] for j in range(rowIndex+1)]

for i in range(rowIndex+1):
    for j in range(rowIndex+1):
        if i<=j:
           grid[i][j]=1
        else:
            grid[i][j] = grid[i-1][j-1] + grid[i-1][j]  
    
print(grid)
temp = grid[-2]
temp.insert(0,1)
temp.pop()
print(temp)

