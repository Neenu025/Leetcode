class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output =[]
        # diff = 0
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums and i!=nums.index(diff):
        #         output.append(i)
        #         output.append(nums.index(diff))
        #         break
        # return output



        
        num_map = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
[2,7,11,15]
