class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        for i in range(16):
            power_of_four = 4**i

            if power_of_four == n:
                return True
           
        return False


        # // 4^16 will give us integer overflow.
        
        
1
