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
            n_sum[i] += estate[j][i-1]

    estate_total = n_sum[n_length] + m_sum[m_length]

def bisearchLeft(sorted_array:list, target:int) -> int:
    






estateSplit('Array/estate_split.txt')