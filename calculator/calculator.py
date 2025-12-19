import operator

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter operation you want to perform on the numbers: ")

operation_defination = {
    '*':operator.mul,
    '/':operator.truediv,
    '-': operator.sub,
    '+': operator.add,
    '**': operator.pow,
}

result = operation_defination[operation](num1,num2)
print(result)