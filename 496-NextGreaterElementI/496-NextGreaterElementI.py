    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        opt = []
        for i in nums1:
            found = False
            for j in range(nums2.index(i), len(nums2)):
                if nums2[j] > i:
                    opt.append(nums2[j])
class Solution:
                    found = True
                    break
            if not found:
                opt.append(-1)
        return opt



        
[
