class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_poped=[]


        while s_list:
            s_pop = s_list.pop()
            s_poped.append(s_pop)
        return ' '.join(s_poped)


        

        
"the sky is blue"
