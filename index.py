def get_input():
    value_1 = int(input("enter first number: "))
    value_2 = int(input("enter second number: "))
    return value_1, value_2

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

def main():
    keep_calculating_count = 3
    while keep_calculating_count >= 1:
        calculate()
        keep_calculating_count = keep_calculating_count - 1
        print(f"remain calculation: {keep_calculating_count}")

if __name__ == "__main__":
    main()        


