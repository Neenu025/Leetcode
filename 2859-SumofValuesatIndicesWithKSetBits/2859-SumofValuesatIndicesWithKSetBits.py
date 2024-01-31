class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        value_sum = 0
        for i in range(len(nums)):
            if str(bin(i)).count('1') == k:
                value_sum +=nums[i]
        return value_sum

        
[
