class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:  
        concat = 0  
        if len(nums)==1:
            return nums[0]
        concat_value = 0
        while len(nums) > 0:
            a = str(nums.pop(0))
            if len(nums) >0:
                b = str(nums.pop()) 
                result = a + b
                print(result)
                concat = int(result)
                a = ""
[
