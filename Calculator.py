import sys
Num1 = float(input('Enter 1st number: '))
Oper = str(input('Enter Operator:  '))
if Oper == '+':
    pass
elif Oper == '-':
    pass
elif Oper == '*':
    pass
elif Oper == '/':
    pass
else:
    print("Invalid Oper")
    sys.exit()

Num2 = float(input('Enter 2nd number: '))
if Oper == '+':
    ans = Num1 + Num2
elif Oper == '-':
    ans = Num1 - Num2
elif Oper == '*':
    ans = Num1 * Num2
elif Oper == '/':
    ans = Num1 / Num2
else:
    print('There was a problem')
    sys.exit()
    
print(ans)