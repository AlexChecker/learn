print("Введите оператор: ")
oper = input()
result =0
if oper == '^':
    print("Введите первое число: ")
    first = int(input())
    print("Введите второе число: ")
    second = int(input())
    result=pow(first,second)
    print(f"{first}{oper}{second}={result}")
elif oper =='+'or oper =='-'or oper =='*'or oper =='/': 
    result=0
    while True:
        intake = int(input())
        if intake ==0: break
        match oper:
            case '+':
                result += intake
            case '-':
                result -= intake
            case '*':
                result *= intake
            case '/':
                result /= intake
    print(f"Результат: {result}")
else:
    print("Нет действия!")


