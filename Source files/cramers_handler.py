from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
import cramers
from validation import validate_3x3_matrix, show_singular_error, show_input_error

def run_cramers(ui):
    try:
        precision = ui.round_spinbox.value()

        matrix = [
            [
                float(ui.a11_cramers.text() or 0),
                float(ui.a12_cramers.text() or 0),
                float(ui.a13_cramers.text() or 0),
                float(ui.sol_cramers.text() or 0)
            ],
            [
                float(ui.a21_cramers.text() or 0),
                float(ui.a22_cramers.text() or 0),
                float(ui.a23_cramers.text() or 0),
                float(ui.sol_cramers_2.text() or 0)
            ],
            [
                float(ui.a31_cramers.text() or 0),
                float(ui.a32_cramers.text() or 0),
                float(ui.a33_cramers.text() or 0),
                float(ui.sol_cramers_3.text() or 0)
            ]
        ]

        if not validate_3x3_matrix(ui, matrix):
            return

        result = cramers.calculate_cramers(matrix, precision)
        if result[0] == "Error":
            show_singular_error(ui)
            return

        solutions, dets = result

        ui.table_cramers.setRowCount(0)
        ui.table_cramers.setColumnCount(2)
        ui.table_cramers.setHorizontalHeaderLabels(["Component", "Determinant"])
        labels = ["Main (D)", "D_x1", "D_x2", "D_x3"]
        for i, val in enumerate(dets):
            row_pos = ui.table_cramers.rowCount()
            ui.table_cramers.insertRow(row_pos)
            ui.table_cramers.setItem(row_pos, 0, QTableWidgetItem(labels[i]))
            ui.table_cramers.setItem(row_pos, 1, QTableWidgetItem(f"{val:.{precision}f}"))

        ui.X1_result_cramers.setText(f"{solutions[0]:.{precision}f}")
        ui.X2_result_cramers.setText(f"{solutions[1]:.{precision}f}")
        ui.X3_result_cramers.setText(f"{solutions[2]:.{precision}f}")

    except ValueError:
        show_input_error(ui, "Invalid numeric input.")