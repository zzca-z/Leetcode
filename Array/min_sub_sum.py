import bisect
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
    
    def minSubArrayLenSort(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        acceleration = [0] * (n + 1)
        min_length = n + 1
        for i in range(1,n+1):
            acceleration[i] = acceleration[i-1]+nums[i-1]


        for i in range(0, n):
            index_end = bisect.bisect_left(acceleration, acceleration[i]+target)
            if index_end < n+1:
                min_length = min(min_length, index_end - i)
        
        if min_length == n + 1:
            min_length = 0 
        
        return min_length
                  
             
         
    #conclusion
    '''
    1. distinct between subarray, subsequence and subset. Subarray is continuous, subsequence is in order, while subset doesn't have other limits.
    2. sliding window to handle subarray. Only need to find out the qualified shortest subarray for each index_end. No need to iterate every items, 
        because the qualified subarrays with a smaller index_start must have a longer length than exsiting qualified subarrays, thus the scale is 
        decreased.
    3. Use the length + 1 as intial value to solve the problem of finding the minimal value and check weather there is a success shot. 
    4. Positive arrays can form accumulated sorted subarrays, then binary search can be used to find the index for the least qualified length. Then,
        to search in subarrays with different start, only need to adjust the target by adding the prefix sums, so that don't need to generate the 
        searching area for every start.
    5. When forming the acceleration sum, range is 0:n+1, while seaching,the start index range is 0:n, because if acceleration[n] added, then no 
        qualified subarrays exist. But the result index should be in range[0:n+1], it's searching within the accleation, so accleation[n] should
        be included.
    '''





    
