from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Function to safely perform calculation
def calculate(expression):
    try:
        # Allowed functions and constants
        allowed = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log10,
            "log10": math.log10,
            "log2": lambda x: math.log(x, 2),
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "pow": math.pow
        }
        result = eval(expression, {"__builtins__": None}, allowed)
        return result
    except Exception:
        return "Error"

@app.route('/', methods=['GET', 'POST'])
def index():
    expression = ''
    result = ''
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        result = calculate(expression)
    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

