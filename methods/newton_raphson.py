from sympy import symbols, sympify, diff, lambdify
import math

def newton_raphson_method(fx_expr_str, p0, tol, max_iter):
    """
    Newton-Raphson Method

    Parameters:
    - fx_expr_str: string form of f(x)
    - p0: initial guess
    - tol: tolerance
    - max_iter: maximum number of iterations

    Returns:
    - result: string summary
    - steps: list of tuples (iteration, p, error)
    """

    x = symbols('x')
    try:
        fx_expr = sympify(fx_expr_str)
        dfx_expr = diff(fx_expr, x)
    except Exception as e:
        return f"Invalid function: {e}", []

    f = lambdify(x, fx_expr, modules=['math'])
    df = lambdify(x, dfx_expr, modules=['math'])

    steps = []

    for i in range(1, max_iter + 1):
        try:
            f_val = f(p0)
            df_val = df(p0)
        except Exception as e:
            return f"Evaluation error: {e}", []

        if df_val == 0:
            return "Derivative is zero. Method fails.", steps

        p = p0 - f_val / df_val
        error = abs(p - p0)
        steps.append((i, round(p, 10), round(error, 10)))

        if error < tol:
            return f"Approximate root: p = {p:.10f}", steps

        p0 = p

    return f"Method did not converge after {max_iter} iterations.", steps
def solve(inputs):
    expr = inputs['fx']
    p0 = float(inputs['x0'])
    tol = float(inputs['tol'])
    N0 = int(inputs['max_iter'])

    result_text, steps = newton_raphson(expr, p0, tol, N0)
    return {
        "output": result_text,
        "steps": steps
    }
