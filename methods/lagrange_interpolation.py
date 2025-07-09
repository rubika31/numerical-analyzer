import math

def lagrange_interpolation(x_points, y_points, x_target):
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x_target - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

def safe_eval(expr, x):
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    allowed.update({'x': x, 'pi': math.pi, 'e': math.e})
    return eval(expr, {"__builtins__": {}}, allowed)

def lagrange_interpolation_wrapper(f_expr, x_values, x_target, degree):
    try:
        # Compute y-values using the function expression
        data = [(x, safe_eval(f_expr, x)) for x in x_values[:degree+1]]
        x_vals, y_vals = zip(*data)
        result = lagrange_interpolation(x_vals, y_vals, x_target)
        return f"Interpolated value of f({x_target}) using degree {degree}: {result:.10f}"
    except Exception as e:
        return f"Error in interpolation: {str(e)}"
def solve(inputs):
    x_values = list(map(float, inputs['x_values'].split(',')))
    y_values = list(map(float, inputs['y_values'].split(',')))
    x_interp = float(inputs['x_interp'])

    output = lagrange_interpolate(x_values, y_values, x_interp)
    return {
        "output": f"Interpolated value at x = {x_interp} is {output}"
    }

