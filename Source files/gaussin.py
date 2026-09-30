def calculate_gaussin(matrix, precision):
    n = 3

    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        if abs(matrix[i][i]) < 1e-12:
            return "Error"

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    final_matrix = [row[:] for row in matrix]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (matrix[i][n] - sum_ax) / matrix[i][i]

    return [round(val, precision) for val in x], final_matrix