nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
temp = []


def removeDuplicates1(nums):
    if len(nums) == 1:
        return 1
    else:
        for i in range(len(nums)):
            if nums[i] not in temp:
                if nums[i-1]==nums[i]:    
                    temp.append(nums[i])
                else:
                    temp.append(nums[i])
                
        for i in range(len(temp)):
            nums[i] = temp[i]      
                
        return len(temp)

print(removeDuplicates1(nums2))


























