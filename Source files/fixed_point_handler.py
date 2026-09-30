from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
import fixed_point
from validation import show_input_error, show_calculation_error

def run_simple_fixed_point(ui):
    try:
        g_txt = ui.gx_input_simple_fixed_point.text()
        x0_val = float(ui.x0_input_simple_fixed_point.text())
        precision = ui.round_spinbox.value()

        if ui.es_radio_btn_simple_fixed_point.isChecked():
            is_es = True
            t_val = float(ui.es_input_simple_fixed_point.text())
        else:
            is_es = False
            t_val = int(ui.maxi_input_simple_fixed_point.text())

        results = fixed_point.calculate_fixed_point(g_txt, x0_val, is_es, t_val, precision)

        if results == "Error":
            show_calculation_error(ui, "Mathematical error in g(x). Check your formula.")
            return

        headers = ["i", "Xi", "g(xi)", "Ea"]
        ui.table_simple_fixed_point.setColumnCount(len(headers))
        ui.table_simple_fixed_point.setHorizontalHeaderLabels(headers)
        ui.table_simple_fixed_point.setRowCount(0)

        for row_data in results:
            row_pos = ui.table_simple_fixed_point.rowCount()
            ui.table_simple_fixed_point.insertRow(row_pos)
            for col, value in enumerate(row_data):
                if value is None:
                    formatted_val = ""
                elif isinstance(value, float):
                    formatted_val = f"{value:.{precision}f}"
                else:
                    formatted_val = str(value)
                ui.table_simple_fixed_point.setItem(row_pos, col, QTableWidgetItem(formatted_val))

        root_val = results[-1][2]
        error_val = results[-1][3]
        ui.root_result_simple_fixed_point.setText(f"{root_val:.{precision}f}")
        ui.error_result_simple_fixed_point.setText(f"{error_val:.{precision}f}" if error_val is not None else "---")

    except ValueError:
        show_input_error(ui, "Invalid numeric input!")
    except Exception as e:
        show_calculation_error(ui, f"Execution failed: {e}")