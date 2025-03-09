from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n  for _ in range(n)]

        moving_steps = (2*n-1) * [0]
        moving_steps[0] = n - 1
        for i in range(1, 2*n-1):
            quotient = i // 2
            remainder = i % 2
            moving_steps[i] = n - quotient - remainder
        #print(moving_steps)

        direction_list = ['right', 'down', 'left', 'up']
        direction = (2*n-1) * [0]
        for i in range(2*n-1):
            index = i % 4
            direction[i] = direction_list[index]
        #print(direction)
        
        def moving(start_point, direction):
            if direction == 'right':
                start_point[1] += 1 
            elif direction == 'down':
                start_point[0] += 1
            elif direction == 'left':
                start_point[1] -= 1
            else:
                start_point[0] -= 1
        
        
        
        start_point = [0, 0]
        value = 1
        for i in range(2*n - 1):
            for j in range(moving_steps[i]):
                matrix[start_point[0]][start_point[1]] = value
                value += 1
                moving(start_point, direction=direction[i])
                #print(start_point)
        return matrix
    


        
"""
- Conclusion
1. when generating matrix, /* [[0] * n for _ in range(n)] */ is needed. /* row = 0 * [n], matrix = n * row */ just 
return a single list.
2. be careful about /* for i in list */ and /* for i in len(list) */, they are very different.
3. When there's a start point and moving, be careful about the very first move. Do we need a move to get the wanted start point? 
Or we start from the wanted point then move. 

"""

class Solution1:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]


        def moving(start_point, direction):
            if direction == 'right':
                start_point[1] += 1 
            elif direction == 'down':
                start_point[0] += 1
            elif direction == 'left':
                start_point[1] -= 1
            else:
                start_point[0] -= 1
            
        
        def turn_check(position, turn, filled_row, filled_column):
            next_position = position.copy()
            moving(next_position,direction_list[turn%4])
            if (next_position[0] in filled_row) or (next_position[1] in filled_column):
                turn += 1
                if (turn%4 == 0) or (turn%4 == 2):
                    filled_column.add(position[1])
                elif (turn%4 == 1) or (turn%4 == 3):
                    filled_row.add(position[0])

            return turn, filled_row, filled_column


        direction_list = ['right', 'down', 'left', 'up']
        position = [0, 0]
        turn = 0
        filled_row = {-1,n}
        filled_column = {-1,n}
        
        for i in range(n**2):
            matrix[position[0]][position[1]] = i+1
            turn, filled_row, filled_column = turn_check(position, turn, filled_row, filled_column)
            moving(position, direction_list[turn%4])
            
        return matrix

"""
- Conclusion
1. decide whether to return a value of chage in place.
2. pay attention to the range(n), range(n) means n times, but from 0 ~ n-1
3. n^2 is not n power 2 but n bitwise or with 2.

"""

class Solution3:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix =[[0]*n for _ in range(n)]
        n_list = list(range(n,0,-2))
        n_list.append(0)
        circle = 0
        for current_n in n_list:
            matrix[circle][circle] = 1 + 4*



n = 1
s = Solution1()
m = s.generateMatrix(n)
for i in range(n):
    print(m[i])     
        