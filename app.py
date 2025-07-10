# app.py
from flask import Flask, render_template, request
import importlib
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize Flask app
app = Flask(__name__)

# Initialize limiter separately, then attach to app
limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)

# Mapping method names to their corresponding Python files (modules)
method_modules = {
    "bisection": "methods.bisection",
    "false_position": "methods.false_position",
    "secant": "methods.secant_method",
    "newton_raphson": "methods.newton_raphson",
    "fixed_point": "methods.fixed_point",
    "lagrange_interpolation": "methods.lagrange_interpolation"
}

@app.route("/", methods=['GET', 'POST'])
@limiter.limit("10 per minute")  # Rate limit applied to this route
def index():
    result = None
    selected_method = None
    inputs = {}

    if request.method == 'POST':
        selected_method = request.form.get("method")
        inputs = request.form.to_dict()

        try:
            if selected_method in method_modules:
                module = importlib.import_module(method_modules[selected_method])
                result = module.solve(inputs)
            else:
                result = {"error": "Selected method not found."}
        except Exception as e:
            result = {"error": f"Error: {str(e)}"}

    return render_template("index.html", methods=method_modules.keys(), selected_method=selected_method, result=result, inputs=inputs)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
