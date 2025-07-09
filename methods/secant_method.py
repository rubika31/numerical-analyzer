import math

def secant_method(expr, p0, p1, tol, max_iter):
    """
    Secant Method

    Parameters:
    - expr: string expression for f(x)
    - p0: first initial guess
    - p1: second initial guess
    - tol: tolerance
    - max_iter: maximum number of iterations

    Returns:
    - result: success or failure message
    - steps: list of tuples (iteration, p, f(p), error)
    """

    def f(x):
        return eval(expr, {"x": x, **math.__dict__})

    steps = []

    try:
        q0 = f(p0)
        q1 = f(p1)
    except Exception as e:
        return f"Function evaluation error: {e}", []

    i = 2
    while i <= max_iter:
        if q1 - q0 == 0:
            return f"Division by zero at iteration {i}.", steps

        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        error = abs(p - p1)
        steps.append((i, round(p, 10), round(f(p), 10), round(error, 10)))

        if error < tol:
            return f"Root approximation: p = {p:.10f} after {i} iterations.", steps

        i += 1
        p0, q0 = p1, q1
        p1, q1 = p, f(p)

    return f"Method failed after {max_iter} iterations.", steps
def solve(inputs):
    expr = inputs['fx']
    p0 = float(inputs['x0'])
    p1 = float(inputs['x1'])
    tol = float(inputs['tol'])
    N0 = int(inputs['max_iter'])

    result_text, steps = secant_method(expr, p0, p1, tol, N0)
    return {
        "output": result_text,
        "steps": steps
    }
