    def findErrorNums(self, nums: List[int]) -> List[int]:
        L = len(nums)
        op = []
        nums_org = list(range(1, L + 1))
       
        duplicate = sum(nums) - sum(set(nums))
class Solution:


        missing = sum(nums_org) - sum(set(nums))

        op.append(duplicate)
        op.append(missing)
        
        return op

        
[
