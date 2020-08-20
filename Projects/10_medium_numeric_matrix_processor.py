def matrix_size(func):
    def wrapper():
        matrix_size = input().split(' ')
        n = int(matrix_size[0])
        m = int(matrix_size[1])
        # func(n,m)
        return func(n, m)
    return wrapper

# check if m of matrixA == n of matrixB -> TRUE can be multiplied
# columns of matrixA == rows of matrixB
# but we multiplu rows of matrixA by columns of matrixB

@matrix_size
def create_matrix(n, m):
    matrix = []
    print('Enter matrix: ')
    for x in range(1, n+1):
        row = list(map(float, input().split(' ')))
        matrix.append(row)
    return matrix

def sum_matrix(m1, m2):
    el_matrix = []
    if [len(x) for x in m1] == [len(x) for x in m2]:
        for i in range(len(m1)):
            el_matrix.append([])
            for j in range(len(m1[i])):
                el_matrix[i].append(m1[i][j] + m2[i][j])
    else:
        print('ERROR')
    return el_matrix

def multiply_matrix(m, *constant):
    if len(constant) > 0:
        mult_no = constant[0]
    else:
        mult_no = input('Enter constant: ')
    el_matrix = []
    for i in range(len(m)):
        el_matrix.append([])
        for j in range(len(m[i])):
            el_matrix[i].append(float(m[i][j]) * float(mult_no))
    return el_matrix


def multiply_matrices(m1, m2):
    el_matrix = []
    test = 0
    i = 0
    k = 0
    for i in range(len(m1)):
        el_matrix.append([])
        for k in range(len(m2[0])):
            for j in range(len(m1[0])):
                test += m1[i][j] * m2[j][k]
            el_matrix[i].append(test)
            test = 0
    return el_matrix


def transpose_matrix(m, transp_type):
    m_range = range(len(m))
    m_range_reverse = range(len(m)-1, -1, -1)
    el_matrix = []
    if transp_type == 1: # main diagonal
        for i in range(len(m)):
            el_matrix.append([])
            for j in range(len(m[i])):
                el_matrix[i].append(m[j][i])
        return el_matrix
    elif transp_type == 2: # diagonal
        k = 0
        for i in range(len(m)-1, -1, -1):
            el_matrix.append([])
            for j in range(len(m[i])-1, -1, -1):
                el_matrix[k].append(m[j][i])
            k += 1
        return el_matrix
    elif transp_type == 3: # vertical line
        for i in range(len(m)):
            el_matrix.append([])
            for j in range(len(m)-1, -1, -1):
                el_matrix[i].append(m[i][j])
        return el_matrix
    elif transp_type == 4: # horizontal line
        k = 0
        for i in range(len(m)-1, -1, -1):
            el_matrix.append([])
            for j in range(len(m)):
                el_matrix[k].append(m[i][j])
            k += 1
        return el_matrix


def matrix_determinant(matrix):
    determinant = 0
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return determinant
    if len(matrix) >= 3:
        for i in range(len(matrix)):
            k = 0
            smaller_matrix = []
            for x in range(1, len(matrix)):
                smaller_matrix.append([])
                for y in range(0, len(matrix)):
                    if y == i:
                        continue
                    else:
                        smaller_matrix[k].append(matrix[x][y])
                k += 1
            if i == 0:
                determinant = matrix[0][i] * matrix_determinant(smaller_matrix)
            elif i % 2 == 0:
                determinant += matrix[0][i] * matrix_determinant(smaller_matrix)
            else:
                determinant -= matrix[0][i] * matrix_determinant(smaller_matrix)
        return determinant


def find_cofactors(matrix):
    def minor(matrix, i, j):
        minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
        return minor

    new_matrix = []
    p = 0
    a = 1
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            minor_mat = minor(matrix, i, j)
            if (i + j) % 2 == 0:
                row.append(matrix_determinant(minor_mat))
            else:
                row.append((-1) * matrix_determinant(minor_mat))
            p += 1
        new_matrix.append(row)
    return new_matrix

def find_inverse(matrix):
    if matrix_determinant(matrix) == 0:
        return "This matrix doesn't have an inverse."
    else:
        cofactor_matrix = find_cofactors(transpose_matrix(matrix, 1))
        return multiply_matrix(cofactor_matrix, (1 / matrix_determinant(matrix)))


def display_matrix(matrix):
    print('The result is:')
    for i in range(len(matrix)):
        onerow = ''.join(str(x) for x in matrix[i::len(matrix)])
        print(onerow[1:-1].replace(',', ''))

def menu():
    print('''\n1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    choice = int(input('Your choice: '))
    if choice == 1:
        print('Enter size of first matrix: ')
        matrixA = create_matrix()
        print('Enter size of second matrix: ')
        matrixB = create_matrix()
        display_matrix(sum_matrix(matrixA, matrixB))
    elif choice == 2:
        print('Enter size of matrix: ')
        matrixA = create_matrix()
        display_matrix(multiply_matrix(matrixA))
    elif choice == 3:
        print('Enter size of first matrix: ')
        matrixA = create_matrix()
        # matrixA = [[5,4], [9,5], [2,3]]
        print('Enter size of second matrix: ')
        matrixB = create_matrix()
        # matrixB = [[1,2], [3,4], [2,2]]
        if len(matrixA[0]) == len(matrixB):
            display_matrix(multiply_matrices(matrixA, matrixB))
        else:
            print('The operation cannot be performed.\n')
    elif choice == 4:
        print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        choice_transp = int(input('Your choice: '))
        print('Enter size of second matrix: ')
        matrixA = create_matrix()
        display_matrix(transpose_matrix(matrixA, choice_transp))
    elif choice == 5:
        print('Enter size of matrix: ')
        matrixA = create_matrix()
        print(matrix_determinant(matrixA))
    elif choice == 6:
        print('Enter size of matrix: ')
        matrixA = create_matrix()
        if find_inverse(matrixA) == "This matrix doesn't have an inverse.":
            print("This matrix doesn't have an inverse.")
        else:
            display_matrix(find_inverse(matrixA))
    elif choice == 0:
        exit()

while True:
    menu()