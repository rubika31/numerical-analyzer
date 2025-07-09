import math

def false_position_method(expr, p0, p1, TOL, N0):
    """
    False Position Method

    Parameters:
    - expr: string expression for f(x)
    - p0, p1: initial guesses
    - TOL: tolerance
    - N0: max number of iterations

    Returns:
    - result: string result or failure message
    - steps: list of tuples (iteration, p, f(p), error)
    """

    def f(x):
        return eval(expr, {"x": x, **math.__dict__})

    try:
        q0 = f(p0)
        q1 = f(p1)
    except Exception as e:
        return f"Function evaluation error: {e}", []

    if q0 * q1 > 0:
        return "Function has the same signs at p0 and p1. Method not applicable.", []

    steps = []
    i = 2

    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        try:
            fp = f(p)
        except Exception as e:
            return f"Function evaluation error at p={p}: {e}", []

        error = abs(p - p1)
        steps.append((i, round(p, 10), round(fp, 10), round(error, 10)))

        if error < TOL:
            return f"Approximate root: p = {p:.10f} after {i} iterations.", steps

        i += 1
        if fp * q1 < 0:
            p0, q0 = p1, q1
        p1, q1 = p, fp

    return f"Method failed to converge after {N0} iterations.", steps
def solve(inputs):
    expr = inputs['fx']
    a = float(inputs['x0'])
    b = float(inputs['x1'])
    tol = float(inputs['tol'])
    N0 = int(inputs['max_iter'])

    result_text, steps = false_position_method(expr, a, b, tol, N0)
    return {
        "output": result_text,
        "steps": steps
    }
