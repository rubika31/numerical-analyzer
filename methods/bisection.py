import math

# Safely evaluate f(x)
def evaluate_function(expr, x):
    return eval(expr, {"x": x, **math.__dict__})

# Bisection Method
def bisection_method(expr, a, b, tol, N0):
    try:
        fa = evaluate_function(expr, a)
        fb = evaluate_function(expr, b)
    except Exception:
        return "Invalid function expression.", []

    if fa * fb > 0:
        return "f(a) and f(b) must have opposite signs. Method fails.", []

    steps = []

    for i in range(1, N0 + 1):
        p = (a + b) / 2
        try:
            fp = evaluate_function(expr, p)
        except Exception:
            return "Invalid function expression.", []

        steps.append((i, round(a, 6), round(b, 6), round(p, 10), round(fp, 10)))

        if fp == 0 or (b - a) / 2 < tol:
            break

        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p

    return f"Root approximation after {len(steps)} iterations: p ≈ {steps[-1][3]:.10f}", steps

def solve(inputs):
    expr = inputs['fx']
    a = float(inputs['x0'])
    b = float(inputs['x1'])
    tol = float(inputs['tol'])
    N0 = int(inputs['max_iter'])

    result_text, steps = bisection_method(expr, a, b, tol, N0)
    return {
        "output": result_text,
        "steps": steps
    }

