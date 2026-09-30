from PyQt6.QtWidgets import QMessageBox
import gaussin
from validation import validate_3x3_matrix, show_singular_error, populate_linear_solver_table, show_input_error

def run_gaussin(ui):
    try:
        precision = ui.round_spinbox.value()

        eq1 = [
            float(ui.a11_gaussin.text() or 0),
            float(ui.a12_gaussin.text() or 0),
            float(ui.a13_gaussin.text() or 0),
            float(ui.sol_gaussin.text() or 0)
        ]
        eq2 = [
            float(ui.a21_gaussin.text() or 0),
            float(ui.a22_gaussin.text() or 0),
            float(ui.a23_gaussin.text() or 0),
            float(ui.sol_gaussin_2.text() or 0)
        ]
        eq3 = [
            float(ui.a31_gaussin.text() or 0),
            float(ui.a32_gaussin.text() or 0),
            float(ui.a33_gaussin.text() or 0),
            float(ui.sol_gaussin_3.text() or 0)
        ]

        matrix = [eq1, eq2, eq3]
        if not validate_3x3_matrix(ui, matrix):
            return

        result = gaussin.calculate_gaussin(matrix, precision)
        if result == "Error":
            show_singular_error(ui)
            return

        solutions, final_matrix = result
        populate_linear_solver_table(ui.table_guassin, final_matrix, precision)

        ui.X1_result_gaussin.setText(f"{solutions[0]:.{precision}f}")
        ui.X2_result_gaussin.setText(f"{solutions[1]:.{precision}f}")
        ui.X3_result_gaussin.setText(f"{solutions[2]:.{precision}f}")

    except ValueError:
        show_input_error(ui, "Invalid numeric input.")