from PyQt6.QtWidgets import QMessageBox
import gauss_jordan
from validation import validate_3x3_matrix, show_singular_error, populate_linear_solver_table, show_input_error

def run_gauss_jordan(ui):
    try:
        precision = ui.round_spinbox.value()

        matrix = [
            [
                float(ui.a11_gauss_jordan.text() or 0),
                float(ui.a12_gauss_jordan.text() or 0),
                float(ui.a13_gauss_jordan.text() or 0),
                float(ui.sol_gauss_jordan.text() or 0)
            ],
            [
                float(ui.a21_gauss_jordan.text() or 0),
                float(ui.a22_gauss_jordan.text() or 0),
                float(ui.a23_gauss_jordan.text() or 0),
                float(ui.sol_gauss_jordan_2.text() or 0)
            ],
            [
                float(ui.a31_gauss_jordan.text() or 0),
                float(ui.a32_gauss_jordan.text() or 0),
                float(ui.a33_gauss_jordan.text() or 0),
                float(ui.sol_gauss_jordan_3.text() or 0)
            ]
        ]

        if not validate_3x3_matrix(ui, matrix):
            return

        result = gauss_jordan.calculate_gauss_jordan(matrix, precision)
        if result[0] == "Error":
            show_singular_error(ui)
            return

        solutions, final_matrix = result
        populate_linear_solver_table(ui.table_gauss_jordan, final_matrix, precision)
        
        if hasattr(ui, 'x1_gauss_jordan'):
            ui.x1_gauss_jordan.setText(f"{solutions[0]:.{precision}f}")
            ui.x2_gauss_jordan.setText(f"{solutions[1]:.{precision}f}")
            ui.x3_gauss_jordan.setText(f"{solutions[2]:.{precision}f}")
        
        elif hasattr(ui, 'X1_result_gauss_jordan'):
            ui.X1_result_gauss_jordan.setText(f"{solutions[0]:.{precision}f}")
            ui.X2_result_gauss_jordan.setText(f"{solutions[1]:.{precision}f}")
            ui.X3_result_gauss_jordan.setText(f"{solutions[2]:.{precision}f}")
        
        elif hasattr(ui, 'x1_result_gauss_jordan'):
            ui.x1_result_gauss_jordan.setText(f"{solutions[0]:.{precision}f}")
            ui.x2_result_gauss_jordan.setText(f"{solutions[1]:.{precision}f}")
            ui.x3_result_gauss_jordan.setText(f"{solutions[2]:.{precision}f}")
        
        else:
            print("Warning: Could not find Gauss-Jordan result boxes")

    except ValueError:
        show_input_error(ui, "Invalid numeric input.")