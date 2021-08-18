# put your python code here
f_num = float(input())
s_num = float(input())
operand = input()

if operand == "+":
    print(f_num + s_num)

elif operand == "-":
    print(f_num - s_num)

elif operand == "/":
    if s_num == 0:
        print("Division by 0!")
    else:
        print(f_num / s_num)

elif operand == "mod":
    if s_num == 0:
        print("Division by 0!")
    else:
        print(f_num % s_num)

elif operand == "div":
    if s_num == 0:
        print("Division by 0!")
    else:
        print(f_num // s_num)

elif operand == "pow":
    print(f_num ** s_num)

elif operand == "*":
    print(f_num * s_num)