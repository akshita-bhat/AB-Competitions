n = [2,3,4,5,1]
length = len(n)
low = 0
high = length-1

while low<=high:
    mid = int((low+high)/2)
    mid_element = n[mid]
    print(mid, mid_element, low, high)
    # mid element is target element
    if mid-1>=0 and mid-1<=length-1 and mid+1<=0 and mid+1<=length-1 and mid_element<=n[mid-1] and mid_element<=n[mid+1]:
        print(mid_element)
        break
    # Mountain A    
    elif mid_element>=n[low] and mid_element>=n[high]:
        print('Mountain A')
        low = mid+1
    else: # Mountain B
        print('Mountain B')
        high = mid-1 

#print(n[low])   
    
    
        
        
        
        
    
    




