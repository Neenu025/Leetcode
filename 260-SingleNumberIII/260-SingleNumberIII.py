class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        for i in range(len(s)):
            if part in s:
                s = s.replace(part,"",1)
        return s
        
"
