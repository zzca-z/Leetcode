class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        index_negative = 0
        nonnegative_squares = []
        negative_squares = []

        while nums[index_negative] < 0:
            negative_squares.append(nums[index_negative]**2)
            index_negative += 1
            if index_negative >= len(nums):
                break
        
        negative_squares.reverse()

        nonnegative_squares = [x**2 for x in nums[len(negative_squares):]]
        
        index_neg = 0
        index_nonneg = 0
        index_sorted = 0
        sorted_squares = nums.copy()

        while index_neg < len(negative_squares) and index_nonneg < len(nonnegative_squares):
            if negative_squares[index_neg] < nonnegative_squares[index_nonneg]:
                sorted_squares[index_sorted] = negative_squares[index_neg]
                index_neg += 1
                index_sorted += 1
            else:
                sorted_squares[index_sorted] = nonnegative_squares[index_nonneg]
                index_nonneg += 1
                index_sorted += 1
        
        while index_neg < len(negative_squares):
            sorted_squares[index_sorted] = negative_squares[index_neg]
            index_neg += 1
            index_sorted += 1
        
        while index_nonneg < len(nonnegative_squares):
            sorted_squares[index_sorted] = nonnegative_squares[index_nonneg]
            index_nonneg += 1
            index_sorted += 1
        
        return sorted_squares
    

#conclusion
'''
1. when using index, be careful about the empty list; also, when the index changes, be careful about the index exceeding the boud.
2. insert(location, value), the first arg is location, and the second arg is value.
3. 
'''