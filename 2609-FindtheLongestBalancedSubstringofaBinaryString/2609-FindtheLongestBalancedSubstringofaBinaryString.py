class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
            
        pattern = '01'
        while pattern in s:
            pattern = '0'+ pattern + '1'
        return (len(pattern)-2)
        
"
