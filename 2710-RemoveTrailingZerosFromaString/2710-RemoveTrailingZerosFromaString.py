class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] == '0':
            num = num.rstrip(num[-1])
            return (num)
        return num
        
"
