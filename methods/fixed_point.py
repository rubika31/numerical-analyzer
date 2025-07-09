import math

def fixed_point_method(g_expr, p0, TOL, N0):
    """
    Fixed-Point Iteration Method

    Parameters:
    - g_expr: A string representing the function g(x)
    - p0: Initial guess
    - TOL: Tolerance
    - N0: Maximum number of iterations

    Returns:
    - result: success or failure message
    - steps: list of tuples (iteration, p, error)
    """

    def g(x):
        return eval(g_expr, {"x": x, **math.__dict__})

    i = 1
    error = float('inf')
    steps = []

    while i <= N0:
        p = g(p0)
        error = abs(p - p0)
        steps.append((i, round(p, 10), round(error, 10)))

        if error < TOL:
            return f"Converged to fixed point: {p} (within tolerance {TOL})", steps

        p0 = p
        i += 1

    return f"Method failed to converge after {N0} iterations.", steps

def solve(inputs):
    g_expr = inputs['fx']
    p0 = float(inputs['x0'])
    tol = float(inputs['tol'])
    N0 = int(inputs['max_iter'])

    result_text, steps = fixed_point(g_expr, p0, tol, N0)
    return {
        "output": result_text,
        "steps": steps
    }
