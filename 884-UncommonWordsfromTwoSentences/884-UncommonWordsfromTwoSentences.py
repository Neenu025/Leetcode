class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list=s1.split()
        s2_list=s2.split()
        count=0
        op=[]

        for i in s1_list:
            if i not in s2_list and s1_list.count(i)==1:
                op.append(i)
        for i in s2_list:
            if i not in s1_list and s2_list.count(i)==1:
                op.append(i)
        return op

        
        
"
