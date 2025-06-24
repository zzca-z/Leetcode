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
    
'''

'''