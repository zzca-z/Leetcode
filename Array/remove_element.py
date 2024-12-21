class Solution:
    def removeElementPy(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
               i = i + 1
        return len(nums)
    
    def removeElementN2(self,nums: list[int], val: int) -> int:
        l = len(nums)
        i = 0
        n = 0

        while i < l-n:
            if nums[i] == val:
                n = n + 1
                j = i
                while j < l-n:
                    nums[j] = nums[j+1]
                    j = j + 1
            else:
                i = i + 1
        
        return l - n
    
    def removeElement(self,nums: list[int], val: int) -> int:
        l = len(nums)
        i = 0
        n = 0

        while i < l-n:
            if nums[i] == val:
                nums[i] = nums[l-n-1]
                n = n + 1
            else:
                i = i + 1
        
        return l - n

            
                

rE = Solution()
nums = [4,6,7,1,2]
val = 2
print(rE.removeElement(nums, val))


#conclusion
'''
1. python uses dynamic memory management, so we can delete the original array. C doesn't support this, so we need to shift the values.
2. once using while-loop combined with if statement, be careful to make sure their is a terminate in all conditions.
'''