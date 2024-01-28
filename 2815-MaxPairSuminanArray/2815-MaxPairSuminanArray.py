            num1 = max(str(nums[i]))
            for j in range(i+1, l):
                num2 = max(str(nums[j]))
                if num1 == num2:
                    temp = max(temp, nums[i] + nums[j])
        return -1 if temp == 0 else temp
        
            
    
              


        

[
