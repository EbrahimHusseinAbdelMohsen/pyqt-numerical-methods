from math import *

def calculate_secant(func_txt, x_minus_1, x_i, is_es, target_val, precision):
    def f(x):
        try:
            clean_func = func_txt.replace('^', '**')
            val = eval(clean_func, {"x": x, "sin": sin, "cos": cos, "exp": exp, "log": log, "tan": tan, "sqrt": sqrt})
            return round(val, precision)
        except:
            return None

    data = []
    
    f_xm1 = f(x_minus_1)
    f_xi = f(x_i)
    if f_xm1 is None or f_xi is None:
        return "Error"
        
    data.append([0, round(x_minus_1, precision), f_xm1, round(x_i, precision), f_xi, None])

    for i in range(1, 101):
        numerator = f_xi * (x_i - x_minus_1)
        denominator = f_xi - f_xm1
        
        if denominator == 0:
            break
            
        x_next = round(x_i - (numerator / denominator), precision)
        
        if x_next != 0:
            ea = round(abs((x_next - x_i) / x_next) * 100, precision)
        else:
            ea = 0.0
            
        x_minus_1 = x_i
        f_xm1 = f_xi
        x_i = x_next
        f_xi = f(x_i)
        
        if f_xi is None:
            return "Error"

        data.append([i, round(x_minus_1, precision), f_xm1, round(x_i, precision), f_xi, ea])

        if is_es:
            if ea <= target_val:
                break
        elif i >= target_val:
            break
                
    return data