class Solution:
    def isFascinating(self, n: int) -> bool:
        new_n = str(n) + str(2 * n) + str(3 * n)
        for i in range(1, 10):
            if new_n.count(str(i)) != 1 or '0' in new_n:
                return False
        return True
        
1
