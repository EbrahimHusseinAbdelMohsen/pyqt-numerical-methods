from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
import secant
from validation import show_input_error, show_calculation_error

def run_secant(ui):
    try:
        f_txt = ui.fx_input_secant.text()
        xi_minus_1 = float(ui.xi_minus_input_secant.text())
        xi_val = float(ui.x0_input_secant.text())
        precision = ui.round_spinbox.value()

        if ui.es_radio_btn_secant.isChecked():
            is_es = True
            t_val = float(ui.es_input_secant.text())
        else:
            is_es = False
            t_val = int(ui.maxi_input_secant.text())

        results = secant.calculate_secant(f_txt, xi_minus_1, xi_val, is_es, t_val, precision)

        if results == "Error":
            show_calculation_error(ui, "Mathematical error. Check your function and guesses.")
            return

        headers = ["Iter", "x_i-1", "f(x_i-1)", "x_i", "f(x_i)", "Ea"]
        ui.table_secant.setColumnCount(len(headers))
        ui.table_secant.setHorizontalHeaderLabels(headers)
        ui.table_secant.setRowCount(0)

        for row_data in results:
            row_pos = ui.table_secant.rowCount()
            ui.table_secant.insertRow(row_pos)
            for col, value in enumerate(row_data):
                if value is None:
                    formatted = "---"
                elif isinstance(value, float):
                    formatted = f"{value:.{precision}f}"
                else:
                    formatted = str(value)
                ui.table_secant.setItem(row_pos, col, QTableWidgetItem(formatted))

        if results:
            final_root = results[-1][3]
            final_error = results[-1][5]
            ui.root_result_secant.setText(f"{final_root:.{precision}f}")
            if final_error is None:
                ui.error_result_secant.setText("---")
            else:
                ui.error_result_secant.setText(f"{final_error:.{precision}f}")

    except ValueError:
        show_input_error(ui, "Please enter valid numbers!")
    except Exception as e:
        show_calculation_error(ui, f"Execution failed: {e}")