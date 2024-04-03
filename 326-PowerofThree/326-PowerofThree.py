class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(21):
            power_of_three = 3**i
            if power_of_three == n:
                return True
        return False

2
