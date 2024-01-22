        #         return False
        new_n = str(n) + str(2 * n) + str(3 * n)
        for i in range(1, 10):
            if new_n.count(str(i)) != 1 or '0' in new_n:
                return False
        return True
        
        #     if new_n.count(str(i)) == 1 and '0' not in new_n:
        #         return True
        #     else:
1
