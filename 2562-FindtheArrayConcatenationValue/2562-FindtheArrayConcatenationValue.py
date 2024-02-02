class Solution:
    def findComplement(self, num: int) -> int:
        new = ""
        b_num = bin(num)[2:]
        for i in str(b_num):
            if i=='1':
                new +='0'
            elif i=='0':
                new +='1'
        return int(new,2)
            
            
        
5
