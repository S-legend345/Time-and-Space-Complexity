num1 = int(input("Enter a digit: "))
num2 = int(input("Enter another digit: "))

print("num1 & num2: ", num1, num2)
print("num1 | num2: ", num1 | num2)
print("num1 ^ num2: ", num1^num2)
print("num1 << num2: ", num1<<num2)
print("num1 >> num2: ", num1>>num2)
print("~num1: ", ~num1)
print("~num2: ", ~num2)

#Program to verify whether user input is odd or even

def isOddorEven(n):
    if (n^1 == n+1):
        return True
    else:
        return False

num = int(input("Enter some number: "))

if isOddorEven(num):
    print(num, 'is even')
else:
    print(num, 'is odd')