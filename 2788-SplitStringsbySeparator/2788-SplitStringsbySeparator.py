class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                if nums[i] == -(nums[j]):
                    return abs(nums[j])
        return -1
            
[
