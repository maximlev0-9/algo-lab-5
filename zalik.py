
def compute(rows, cols, matrix:list):
    distance = [ 0 for i in range(cols)]
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == '.':
                distance[col] +=1
            else:
                if(matrix[col-1]=='X'):
                    if distance[col-1]<distance[col]:
                        distance[col] = distance[col-1]
        
        for col in range(cols-1, 0, -1):
            if distance[col]<distance[col-1] and matrix[row][col]=='X' and matrix[row][col-1]=='X':
                
                distance[col-1] = distance[col]

    return min(distance)
