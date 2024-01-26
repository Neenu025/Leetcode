class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        _sum = 0
        balance = k - numOnes
        if numOnes >= k:
            _sum = k
        elif numOnes < k and k<=(numOnes+numZeros):
            _sum = numOnes + balance*0
        elif k > (numOnes + numZeros) and balance >numZeros:
            neg_count = balance-numZeros
            _sum = numOnes + balance*0 + neg_count*(-1)
            print(neg_count)
        
        return _sum


3
