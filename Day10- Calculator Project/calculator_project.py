import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

def valid_operator():
    operator = input("+\n-\n*\n/\nPick an Operation: ")
    return operator

def check_new_or_not(ans):
    n = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")
    return n

def calc(num1, ans):
    operator = valid_operator()
    o = ["+","-","*","/"]
    while operator not in o:
        print("Invalid Operation")
        operator = valid_operator()
    num2 = float(input("What's the next number?: "))
    if operator == "+":
        ans = add(num1, num2)
    elif operator == "-":
        ans = subtract(num1, num2)
    elif operator == "*":
        ans = multiply(num1, num2)
    else:
        ans = divide(num1, num2)

    print(f"{num1} {operator} {num2} = {ans}")

    new_or_not = check_new_or_not(ans)
    yes_or_no = ["y","n"]
    while new_or_not not in yes_or_no:
        print("Invalid Selection")
        new_or_not = check_new_or_not(ans)
    if new_or_not == "y":
        calc(ans, 0)
    else:
        return



while(True):
    ans = 0
    num1 = float(input("What's the first number?: "))
    calc(num1, ans)


