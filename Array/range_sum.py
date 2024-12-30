class Solution():
    def rangeSum(self, file_read: str, file_write:str):
        with open(file_read, 'r') as file:
            content = file.read()

        lines = content.split('\n')
        length_array = int(lines[0])
        array_read = list(map(int,(lines[1:length_array+1])))

        array_rest = lines[length_array+1:]
        array_write = []
        for i in array_rest:
            array_write.append(list(map(int,i.split())))
        
        pre_sum = [0] * (length_array + 1)
        for i in range(1,(length_array + 1)):
            pre_sum[i] = pre_sum[i-1] + array_read[i-1]

        with open(file_write, 'w') as file:
            for i in array_write:
                number_write = pre_sum[i[1]+1] - pre_sum[i[0]]
                file.write(f'{number_write}\n')
                print(number_write)


sl = Solution()
sl.rangeSum('Array/range_sum.txt', 'Array/range_sum_result.txt')

#conclusion
'''
1. use map to handle reveriting str to int.
'''
        