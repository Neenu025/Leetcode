class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        final_count = 0
        sum_count = 0
        for num, count in counts.items():
            if count == 1:
                sum_count = -1
                break
            if count%3 == 0:
                final_count = count//3
            elif count%3 == 1: 
                final_count = (count//3) + 1
            else:
                count%3 == 2
                final_count = (count//3) + 1

[
