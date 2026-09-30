from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

def show_input_error(ui, message):
    QMessageBox.critical(ui, "Input Error", message)

def show_calculation_error(ui, message):
    QMessageBox.warning(ui, "Calculation Error", message)

def validate_3x3_matrix(ui, matrix):

    eq_names = ["Equation 1", "Equation 2", "Equation 3"]
    for i, row in enumerate(matrix):
        if all(v == 0 for v in row[:3]):
            show_input_error(ui, f"Please enter {eq_names[i]}")
            return False
    return True

def show_singular_error(ui):
    show_calculation_error(ui, "The system has no unique solution (singular matrix).")

def populate_linear_solver_table(table_widget, final_matrix, precision):

    table_widget.setRowCount(0)
    table_widget.setColumnCount(4)
    table_widget.setHorizontalHeaderLabels(["x1", "x2", "x3", "b"])

    for row in final_matrix:
        row_pos = table_widget.rowCount()
        table_widget.insertRow(row_pos)
        for col_idx, val in enumerate(row):
            table_widget.setItem(row_pos, col_idx,
                                 QTableWidgetItem(f"{val:.{precision}f}"))