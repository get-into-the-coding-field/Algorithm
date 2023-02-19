from collections import defaultdict
def func(nums1, nums2):
    hash = defaultdict(int)

    while nums1:
        np1 = nums1.pop()
        hash[np1[0]] += np1[1]
    
    while nums2:
        np2 = nums2.pop()
        hash[np2[0]] += np2[1]
        
    return sorted([[key, value] for key, value in hash.items()])
    

    
    
nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]

print(func(nums1, nums2))
