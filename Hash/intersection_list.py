from typing import List

class Solution:
    def intersection(self, nums1:List[int], nums2:List[int]) -> List[int]:
        table = {}
        for num in nums1:
            table[num] = 1
        
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
        
        return list(res)