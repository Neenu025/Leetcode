class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_in_order = iter(t)
        for letter in s:
            if letter not in t_in_order:
                return False
        return True

        
"
