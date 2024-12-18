class Solution:
    def binary_search(self, nums: list[int], target:int) -> int:
        index = -1
        begin_index = 0
        end_index = len(nums) - 1

        while begin_index <= end_index:
            middle_index = int(begin_index+(end_index - begin_index)/2)
            if target == nums[middle_index]:
                index = middle_index
                return index
            elif target < nums[middle_index]:
                end_index = middle_index - 1
            else:
                begin_index = middle_index + 1
        
        return index


                


solution = Solution()
print(solution.binary_search([-2,1,5,9],0))

#conclusion
'''
1. Bacause the beginning and ending parameters are not inlcuded in the variable, so recursive calling is not solvable.
2. Use index, so the end_index should be len - 1.
3. Then remember, middle return, less m-1, more m+1.
4. the middle shoule inlcude the begin_index, which is not always 0.
'''