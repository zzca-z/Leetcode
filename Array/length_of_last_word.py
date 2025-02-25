class solution:
    def lenthOfLastWord(self, s:str) -> int:
        s_list = s.split(' ')
        lenth_last = len(s_list[-1])
        return lenth_last