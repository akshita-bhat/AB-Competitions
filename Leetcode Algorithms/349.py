from collections import Counter
nums1 = [3,2]
nums2 = [9,4,9,8,4]

def intersection(nums1, nums2):
    temp = []
    a = Counter(nums1)
    if len(nums1)==0 or len(nums2) == 0:
        return []    
    for i in range(len(nums2)):
        if nums2[i] not in temp:
            if nums2[i] in a.keys():
                temp.append(nums2[i])
    
    return temp

print(intersection(nums1, nums2))

