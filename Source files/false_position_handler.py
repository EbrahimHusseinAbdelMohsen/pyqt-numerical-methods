from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
import false_position
from validation import show_input_error, show_calculation_error

def run_false_position(ui):
    try:
        f_txt = ui.fx_input_false_position.text()
        xl_val = float(ui.xl_input_false_position.text())
        xu_val = float(ui.xu_input_false_position.text())
        precision = ui.round_spinbox.value()

        if ui.es_radio_btn_false_position.isChecked():
            is_es = True
            t_val = float(ui.es_input_false_position.text())
        else:
            is_es = False
            t_val = int(ui.maxi_input_false_position.text())

        results = false_position.calculate_false_position(f_txt, xl_val, xu_val, is_es, t_val, precision)

        if results == "No root":
            show_calculation_error(ui, "No root found! f(Xl) and f(Xu) must have different signs.")
            return

        headers = ["iter.", "Xl", "f(xl)", "Xu", "f(xu)", "Xr", "f(xr)", "Ea"]
        ui.table_false_position.setColumnCount(len(headers))
        ui.table_false_position.setHorizontalHeaderLabels(headers)
        ui.table_false_position.setRowCount(0)

        for row_data in results:
            row_pos = ui.table_false_position.rowCount()
            ui.table_false_position.insertRow(row_pos)
            for col, value in enumerate(row_data):
                if value is None:
                    formatted_val = ""
                elif isinstance(value, float):
                    formatted_val = f"{value:.{precision}f}"
                else:
                    formatted_val = str(value)
                ui.table_false_position.setItem(row_pos, col, QTableWidgetItem(formatted_val))

        root_val = results[-1][5]
        last_ea = results[-1][7]
        ui.root_result_false_position.setText(f"{root_val:.{precision}f}")
        ui.error_result_false_position.setText(f"{last_ea:.{precision}f}" if last_ea is not None else "---")

    except ValueError:
        show_input_error(ui, "Please fill all boxes with valid numbers!")
    except Exception as e:
        show_calculation_error(ui, f"Something went wrong: {e}")