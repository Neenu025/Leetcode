        
      
        intersection_list = []
        
      
        for num in intersection_set:
            count = min(nums1.count(num), nums2.count(num))
            intersection_list.extend([num] * count)
        intersection_set = set1.intersection(set2)
        
        return intersection_list
        set2 = set(nums2)
        set1 = set(nums1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
[
