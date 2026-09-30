from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
import bisection
from validation import show_input_error, show_calculation_error

def run_bisection(ui):
    try:
        f_txt = ui.fx_input_bisection.text()
        xl_val = float(ui.xl_input_bisection.text())
        xu_val = float(ui.xu_input_bisection.text())
        precision = ui.round_spinbox.value()

        if ui.es_radio_btn.isChecked():
            is_es = True
            t_val = float(ui.es_input_bisection.text())
        else:
            is_es = False
            t_val = int(ui.maxi_input_bisection.text())

        results = bisection.calculate_bisection(f_txt, xl_val, xu_val, is_es, t_val, precision)

        if results == "No root":
            show_calculation_error(ui, "No root found! f(Xl) and f(Xu) must have different signs.")
            return

        headers = ["i", "Xl", "f(xl)", "Xu", "f(xu)", "Xr", "f(xr)", "Ea"]
        ui.table_bisection.setColumnCount(len(headers))
        ui.table_bisection.setHorizontalHeaderLabels(headers)
        ui.table_bisection.setRowCount(0)

        for row_data in results:
            row_pos = ui.table_bisection.rowCount()
            ui.table_bisection.insertRow(row_pos)
            for col, value in enumerate(row_data):
                if value is None:
                    formatted_val = ""
                elif isinstance(value, float):
                    formatted_val = f"{value:.{precision}f}"
                else:
                    formatted_val = str(value)
                ui.table_bisection.setItem(row_pos, col, QTableWidgetItem(formatted_val))

        root_val = results[-1][5]
        error_val = results[-1][7]
        ui.root_result_bisection.setText(f"{root_val:.{precision}f}")
        ui.error_result_bisection.setText(f"{error_val:.{precision}f}" if error_val is not None else "---")

    except ValueError:
        show_input_error(ui, "Please fill all boxes with valid numbers!")
    except Exception as e:
        show_calculation_error(ui, f"Something went wrong: {e}")