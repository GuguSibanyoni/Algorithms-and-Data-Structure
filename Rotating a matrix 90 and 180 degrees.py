

def rotate_90_deg(matrix):
    rotated_matrix = []

    for i in range(len(matrix)):
        rotated_matrix.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            rotated_matrix[i].insert(0, matrix[j].pop(0))

            # comment the above line and uncomment the below line to rotate 90 degrees anticlockwise
            #rotated_matrix[i].insert(0, matrix[j].pop(-1))
    return rotated_matrix


new_matrix = rotate_90_deg([[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]])
#print(new_matrix)

for i in new_matrix:
    print(i)


n= 4

def rotate_180_deg(matrix):

    i = n - 1
    while (i >= 0):
        j = n - 1
        while (j >= 0):
            print(matrix[i][j], end= " ")
            j = j - 1
        print()
        i = i - 1


# Driver code
matrix = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

rotate_180_deg(matrix)