print("Welcome to Sushan's Basic Calculator!")


def sum_1(a, b):
    sum_result = a + b
    print(f"Result is: {sum_result}")
    ask_user(sum_result)


def sub_1(a, b):
    sub_result = a - b
    print(f"Result is: {sub_result}")
    ask_user(sub_result)


def mul_1(a, b):
    mul_result = a * b
    print(f"Result is: {mul_result}")
    ask_user(mul_result)


def div_1(a, b):
    while True:
        try:
            div_result = a / b
            print(f"Result is: {div_result}")
            ask_user(div_result)
            break
        except ZeroDivisionError:
            print("Please use a denominator other than 0 (zero)")
            first_calculation()


def div_r_1(a, b):
    while True:
        try:
            div_r_result = a // b
            print(f"Result is: {div_r_result}")
            ask_user(div_r_result)
            break
        except ZeroDivisionError:
            print("Please use a denominator other than 0 (zero)")
            first_calculation()


def pow_1(a, b):
    pow_result = a ** b
    print(f"Result is: {pow_result}")
    ask_user(pow_result)


def mod_1(a, b):
    while True:
        try:
            mod_result = a % b
            print(f"Result is: {mod_result}")
            ask_user(mod_result)
            break
        except ZeroDivisionError:
            print("Please use a denominator other than 0 (zero)")
            first_calculation()


def loop_function(in1, in2, operation):
    if operation == '+' or operation in ('add', 'ADD', 'Add'):
        sum_1(in1, in2)
    elif operation in '-' or operation in ('sub', 'SUB', 'Sub'):
        sub_1(in1, in2)
    elif operation == '*' or operation in ('mul', 'MUL', 'Mul'):
        mul_1(in1, in2)
    elif operation == '/' or operation in ('div', 'DIV', 'Div'):
        div_1(in1, in2)
    elif operation == '//' or operation in ('r_div', 'R_DIV', 'R_div'):
        div_r_1(in1, in2)
    elif operation == '**' or operation in ('pow', 'POW', 'Pow'):
        pow_1(in1, in2)
    elif operation == '%' or operation in ('mod', 'MOD', 'Mod'):
        mod_1(in1, in2)
    else:
        print(f"Please Enter a proper operation you want to perform! (+, -, *, /, //, %, **)")
        print("Reinitializing...")
        first_calculation()


def first_calculation():
    while True:
        try:
            in1 = float(input("Enter your 1st Number: "))
            operation = str(input("What kind of operation do you wanna do? "))
            in2 = float(input("Enter your 2nd Number: "))
            loop_function(in1, in2, operation)
            break
        except ValueError:
            print("Please enter numbers, integer, whole or decimals! ")


def ask_user(results):
    more_calc = input("Do you want to do more calculations?(Y/N): ")
    if more_calc == "Y" or more_calc == 'y':
        loop_calculations(results)
    elif more_calc in ("N", "n"):
        print("Thanks for using Sushan's calculator!")
    else:
        print("Please respond with Y/N")
        ask_user(results)


def loop_calculations(results):
    a = results
    while True:
        try:
            operation = str(input("What kind of operation do you wanna do? "))
            in3 = float(input("Enter your number: "))
            loop_function(a, in3, operation)
            break
        except ValueError:
            print("Please enter numbers, integer, whole or decimals! ")


first_calculation()
