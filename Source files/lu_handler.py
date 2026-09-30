from PyQt6.QtWidgets import QMessageBox
import lu_decomposition
from validation import validate_3x3_matrix, show_singular_error, populate_linear_solver_table, show_input_error

def run_lu(ui):
    try:
        precision = ui.round_spinbox.value()

        matrix = [
            [
                float(ui.a11_lu_decomposition.text() or 0),
                float(ui.a12_lu_decomposition.text() or 0),
                float(ui.a13_lu_decomposition.text() or 0),
                float(ui.sol_lu_decomposition.text() or 0)
            ],
            [
                float(ui.a21_lu_decomposition.text() or 0),
                float(ui.a22_lu_decomposition.text() or 0),
                float(ui.a23_lu_decomposition.text() or 0),
                float(ui.sol_lu_decomposition_2.text() or 0)
            ],
            [
                float(ui.a31_lu_decomposition.text() or 0),
                float(ui.a32_lu_decomposition.text() or 0),
                float(ui.a33_lu_decomposition.text() or 0),
                float(ui.sol_lu_decomposition_3.text() or 0)
            ]
        ]

        if not validate_3x3_matrix(ui, matrix):
            return

        result = lu_decomposition.calculate_lu(matrix, precision)
        if result[0] == "Error":
            show_singular_error(ui)
            return

        solutions, final_matrix = result
        populate_linear_solver_table(ui.table_lu_decomposition, final_matrix, precision)

        ui.X1_result_lu_decomposition.setText(f"{solutions[0]:.{precision}f}")
        ui.X2_result_lu_decomposition.setText(f"{solutions[1]:.{precision}f}")
        ui.X3_result_lu_decomposition.setText(f"{solutions[2]:.{precision}f}")

    except ValueError:
        show_input_error(ui, "Invalid numeric input.")