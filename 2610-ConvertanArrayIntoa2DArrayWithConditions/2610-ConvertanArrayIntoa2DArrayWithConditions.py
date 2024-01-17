class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        output=[]
        while(len(nums)>0):

            row=[]
            for i in range(len(nums)-1,-1,-1):
                if nums[i] not in row:
                    row.append(nums[i])
                    nums.remove(nums[i])
            output.append(row)
        return output


        
[
