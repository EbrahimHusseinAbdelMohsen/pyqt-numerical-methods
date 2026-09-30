def calculate_gauss_jordan(matrix, precision):
    n = len(matrix)
    
    try:
        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                    max_row = k
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

            if abs(matrix[i][i]) < 1e-12:
                return "Error", None

            pivot = matrix[i][i]
            for j in range(i, n + 1):
                matrix[i][j] /= pivot

            for k in range(n):
                if k != i:
                    factor = matrix[k][i]
                    for j in range(i, n + 1):
                        matrix[k][j] -= factor * matrix[i][j]

        solutions = [round(row[n], precision) for row in matrix]
        final_matrix = [[round(val, precision) for val in row] for row in matrix]
        
        return solutions, final_matrix
        
    except ZeroDivisionError:
        return "Error", None