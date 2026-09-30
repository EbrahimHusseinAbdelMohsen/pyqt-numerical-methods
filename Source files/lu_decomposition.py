def calculate_lu(matrix, precision):
    n = 3
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    B = [row[3] for row in matrix]
    A = [row[:3] for row in matrix]

    try:
        for i in range(n):
            for k in range(i, n):
                sum_val = sum(L[i][j] * U[j][k] for j in range(i))
                U[i][k] = A[i][k] - sum_val
            
            for k in range(i, n):
                if i == k:
                    L[i][i] = 1.0
                else:
                    sum_val = sum(L[k][j] * U[j][i] for j in range(i))
                    L[k][i] = (A[k][i] - sum_val) / U[i][i]

        y = [0.0] * n
        for i in range(n):
            sum_val = sum(L[i][j] * y[j] for j in range(i))
            y[i] = B[i] - sum_val

        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            sum_val = sum(U[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (y[i] - sum_val) / U[i][i]

        final_state = []
        for i in range(n):
            final_state.append(U[i] + [y[i]])

        return [round(val, precision) for val in x], final_state
    except ZeroDivisionError:
        return "Error", None