from lib.utils import get_input

def calculate():
    try:
        value_1, value_2 = get_input()
    except Exception:
        value_1, value_2 = get_input()    
    operators = ["-","+","/","*","%"]   
    op = input("choose calculation operand (+, -, %, /, *) ") 
    while op not in operators:
        op = input("give valid calculation operand (+, -, %, /, *) ")
    value_sum = 0
    if op == "-":
        value_sum = value_1 - value_2
    elif op == "+":
        value_sum = value_1 + value_2
    elif op == "/":
        value_sum = value_1 / value_2
    elif op == "%":
        value_sum = value_1 % value_2
    elif op == "*":
        value_sum = value_1 * value_2    

    print(f"{value_1} {op} {value_2} = {value_sum}") 