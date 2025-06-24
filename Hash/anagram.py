class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        list_word = list(s)
        for char in t:
            if char in list_word:
                list_word.remove(char)
            else:
                return False
        
        return True

    def isAnagram_hash(self, s: str, t: str) -> bool:
        list_number = [0] * 26

        for i in s:
            list_number[ord(i) - ord('a')] += 1
        for j in t:
            list_number[ord(j) - ord('a')] -= 1
        
        if list_number == [0] * 26:
            return True
        else:
            return False
        
        
        

'''
1. the first implementation of list.remove() is by iterating and shifting, so the time complexity is
O(n), so this solution is equal to brute forth with O(n^2) complexity.
'''

    