class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        index_end = 0
        index_start = 0
        min_length = len(nums) + 1
        new_length = len(nums) + 1
        sum_sub = 0

        while index_end < len(nums):
            sum_sub += nums[index_end]
            while sum_sub >= target:
                new_length = index_end - index_start + 1
                sum_sub -= nums[index_start]
                index_start += 1

            if new_length < min_length:
                    min_length = new_length
            
            index_end += 1
        
        if min_length == len(nums) + 1:
            min_length = 0

        return min_length
    
    #conclusion
    '''
    1. distinct between subarray, subsequence and subset. Subarray is continuous, subsequence is in order, while subset doesn't have other limits.
    2. sliding window to handle subarray. Only need to find out the qualified shortest subarray for each index_end. No need to iterate every items, 
        because the qualified subarrays with a smaller index_start must have a longer length than exsiting qualified subarrays, thus the scale is 
        decreased.
    3. Use the length + 1 as intial value to solve the problem of finding the minimal value and check weather there is a success shot. 
    '''





    
