from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words_len = len(words)
        char_list = [0] * 26
        
    
        for char in words[0]:
            char_list[ord(char) - ord('a')] += 1
        
        

        for i in range(1, words_len):
            new_char_list = [0] * 26
            for char in words[i]:
                new_char_list[ord(char) - ord('a')] += 1
                
            for j in range(26):
                char_list[j] = min(char_list[j], new_char_list[j])
                     
        
        common_char = []
        for i in range(26):
            while char_list[i] > 0 :
                common_char.append(chr(ord('a') + i))
                char_list[i] -= 1

        return common_char


words = ["bella","label","roller"]
sl = Solution()
print(sl.commonChars(words))

