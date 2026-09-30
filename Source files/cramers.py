def calculate_cramers(matrix, precision):
    def get_det(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    A = [row[:3] for row in matrix]
    B = [row[3] for row in matrix]
    
    det_A = get_det(A)
    
    if abs(det_A) < 1e-12:
        return "Error", None

    results = []
    dets = [det_A]
    for i in range(3):
        Ai = [row[:3] for row in matrix]
        for row_idx in range(3):
            Ai[row_idx][i] = B[row_idx]
        
        di = get_det(Ai)
        dets.append(di)
        results.append(round(di / det_A, precision))
        
    return results, dets