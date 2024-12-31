def estateSplit(file_read:str) -> int:
    with open(file_read,'r') as file:
        content = file.read()
    
    lines = content.split()

    n_length = int(lines[0])
    m_length = int(lines[1])

    estate = []
    
    for i in range(0, n_length):
        estate.append(list(map(int, lines[(2+3*i):(5+3*i)])))
    
    
    n_sum = [0] * (n_length+1)
    for i in range(1, n_length+1):
        n_sum[i] += n_sum[i-1]
        for j in range(0, m_length):
            n_sum[i] += estate[i-1][j]

    m_sum = [0] * (m_length+1)
    for i in range(1, m_length+1):
        m_sum[i] += m_sum[i-1]
        for j in range(0, n_length):
            m_sum[i] += estate[j][i-1]    

    estate_total = n_sum[n_length] + m_sum[m_length]
    difference = 0

    print(n_sum, m_sum, estate_total)

    if n_length > 1:
        divide = bisearchLeft(n_sum, estate_total/2)
        if divide == 1:
            divide = 2
        difference_1 = abs(2*n_sum[divide-1]-estate_total)
        difference_2 = abs(2*n_sum[divide]-estate_total)
        difference_n = min(difference_1, difference_2)
    
    if m_length > 1:
        divide = bisearchLeft(m_sum, estate_total/2)
        if divide == 1:
            divide = 2
        difference_1 = abs(2*m_sum[divide-1]-estate_total)
        difference_2 = abs(2*m_sum[divide]-estate_total)

        difference_m = min(difference_1, difference_2)

    difference = min(difference_m, difference_n)

    return difference

def bisearchLeft(sorted_array:list, target:int) -> int:
    start_index = 0
    end_index = len(sorted_array)
    target_index = 0
    while start_index < end_index:
        middle_index = (start_index + end_index) // 2
        if sorted_array[middle_index] == target:
            target_index = middle_index
            break
        elif target > sorted_array[middle_index]:
            start_index = middle_index + 1
        else:
            end_index = middle_index
    return target_index


print(estateSplit('Array/estate_split.txt'))



#conclusion
'''
1. When copy code to similar uses, make sure all the variable name has been changed, especially for the m and n. Maybe using replace is better.
'''