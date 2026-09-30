from math import *

def calculate_bisection(func_txt, xl, xu, is_es, target_val, precision):
    def f(x):
        try:
            val = eval(func_txt, {"x": x, "sin": sin, "cos": cos, "exp": exp, "log": log, "tan": tan, "sqrt": sqrt})
            return round(val, precision)
        except:
            return 0.0

    if f(xl) * f(xu) >= 0:
        return "No root"

    data = []
    xr_old = None  
    
    for i in range(1, 100): 
        xr = round((xl + xu) / 2, precision)
        
        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)
        
        if xr_old is not None and xr != 0:
            ea = round(abs((xr - xr_old) / xr) * 100, precision)
        else:
            ea = None 
        
        data.append([i, xl, fxl, xu, fxu, xr, fxr, ea])

        if is_es:
            if ea is not None and ea < target_val:
                break 
        else:
            if i >= target_val:
                break 

        if fxl * fxr < 0:
            xu = xr
        else:
            xl = xr
            
        xr_old = xr
        
    return data