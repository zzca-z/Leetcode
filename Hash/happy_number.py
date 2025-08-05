class Solution:
    def isHappy(self, n:int) -> bool:
        result_history = []
        num = n

        while num != 1:
            
            new_num = 0
            for d in str(num):
                new_num += (int(d) ** 2)
            
            if new_num in result_history:
                return False
            else:
                result_history.append(new_num)
            
            num = new_num
        
        return True
    
    def isHappyc(self, n:int) -> bool:
        record = []
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in record:
                return False
            else:
                record.append(n)
        return True
    

test = Solution()
print(test.isHappyc(19))
            