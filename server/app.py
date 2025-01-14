#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)  
    return input_string

@app.route('/count/<int:num>')  
def count(num):  
    # Create a string of numbers from 0 to num-1 with newline characters  
    numbers = '\n'.join(str(i) for i in range(num)) + '\n'  # Exclude num itself  
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')  
def math(num1, operation, num2):  
    if operation == '+':  
        return str(num1 + num2)  # Just return the sum as string  
    elif operation == '-':  
        return str(num1 - num2)  # Just return the difference as string  
    elif operation == '*':  
        return str(num1 * num2)  # Just return the product as string  
    elif operation == 'div':  
        if num2 == 0:  
            return 'Error: Division by zero is not allowed.'  
        return str(num1 / num2)  # Just return the division as string  
    elif operation == '%':  
        return str(num1 % num2)  # Just return the modulus as string  
    else:  
        return 'Error: Invalid operation.'     


if __name__ == '__main__':
    app.run(port=5555, debug=True)
