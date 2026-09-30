from math import *

def calculate_newton(f_txt, df_txt, x0, is_es, target_val, precision):
    def evaluate(txt, val):
        try:
            context = {"x": val, "sin": sin, "cos": cos, "exp": exp, "log": log, "tan": tan, "sqrt": sqrt}
            return eval(txt, context)
        except:
            return None

    data = []
    xi = x0
    
    for i in range(1, 101):
        f_xi = evaluate(f_txt, xi)
        df_xi = evaluate(df_txt, xi)
        
        if f_xi is None or df_xi is None or df_xi == 0:
            return "Error"

        xi_next = round(xi - (f_xi / df_xi), precision)
        
        if xi_next != 0:
            ea = round(abs((xi_next - xi) / xi_next) * 100, precision)
        else:
            ea = 0.0
        
        data.append([
            i, 
            round(xi, precision), 
            xi_next, 
            round(f_xi, precision), 
            round(df_xi, precision), 
            ea
        ])

        if is_es:
            if ea < target_val:
                break 
        else:
            if i >= target_val:
                break 
        
        xi = xi_next
        
    return data