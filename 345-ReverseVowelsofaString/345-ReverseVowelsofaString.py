class Solution:
    def reverseVowels(self, s: str) -> str:
        v_string = ["A","a","E","e","I","i","O","o","U","u"]
        for i in range(len(s)):
            if s[i] in v_string:

        store = []

                store.append(s[i])
               
        for i in range(len(s)):
            if s[i] in v_string:
                s = s[:i] + store.pop() + s[i+1:]
        return s
        
"
