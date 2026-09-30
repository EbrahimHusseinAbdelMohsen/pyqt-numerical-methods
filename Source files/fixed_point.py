from math import *

def calculate_fixed_point(func_txt, x0, is_es, target_val, precision):

    def g(x):
        try:
            val = eval(func_txt, {"x": x, "sin": sin, "cos": cos, "exp": exp, "log": log, "tan": tan, "sqrt": sqrt})
            return round(val, precision)
        except:
            return None
    data = []
    xi = x0
    for i in range(1, 101):
        g_xi = g(xi)
        if g_xi is None:
            return "Error"
        if g_xi != 0:
            ea = round(abs((g_xi - xi) / g_xi) * 100, precision)
        else:
            ea = 0.0
        data.append([i, xi, g_xi, ea])
        if is_es:
            if ea < target_val:
                break
        else:
            if i >= target_val:
                break
        xi = g_xi
    return data 