class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vovels = ['a','e','i','o','u']
        count_a = 0
        count_b = 0
        s_list = list(s.lower())
        n = len(s_list)
        a = s_list[:(n//2)]
        b = s_list[n//2:]
        
        for i in a:
            if i in vovels:
                count_a += 1
        for i in b:
            if i in vovels:
                count_b += 1
        if count_a == count_b:
"
