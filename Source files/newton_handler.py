from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
import newton
from validation import show_input_error, show_calculation_error

def run_newton(ui):
    try:
        f_txt = ui.fx_input_newton.text()
        df_txt = ui.dfx_input_newton.text()
        x0_val = float(ui.x0_input_newton.text())
        precision = ui.round_spinbox.value()

        if ui.es_radio_btn_newton.isChecked():
            is_es = True
            t_val = float(ui.es_input_newton.text())
        else:
            is_es = False
            t_val = int(ui.maxi_input_newton.text())

        results = newton.calculate_newton(f_txt, df_txt, x0_val, is_es, t_val, precision)

        if results == "Error":
            show_calculation_error(ui, "Mathematical error in f(x) or f'(x).")
            return

        headers = ["i", "Xi", "Xi+1", "f(xi)", "f'(xi)", "Ea"]
        ui.table_newton.setColumnCount(len(headers))
        ui.table_newton.setHorizontalHeaderLabels(headers)
        ui.table_newton.setRowCount(0)

        for row_data in results:
            row_pos = ui.table_newton.rowCount()
            ui.table_newton.insertRow(row_pos)
            for col, value in enumerate(row_data):
                if value is None:
                    formatted_val = ""
                elif isinstance(value, (float, int)):
                    if col == 0:
                        formatted_val = str(value)
                    else:
                        formatted_val = f"{value:.{precision}f}"
                else:
                    formatted_val = str(value)
                ui.table_newton.setItem(row_pos, col, QTableWidgetItem(formatted_val))

        if results:
            root_val = results[-1][2]
            error_val = results[-1][5]
            ui.root_result_newton.setText(f"{root_val:.{precision}f}")
            if error_val is None:
                ui.error_result_newton.setText("---")
            else:
                ui.error_result_newton.setText(f"{error_val:.{precision}f}")

    except ValueError:
        show_input_error(ui, "Invalid numeric input!")
    except Exception as e:
        show_calculation_error(ui, f"Execution failed: {e}")