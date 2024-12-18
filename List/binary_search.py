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
