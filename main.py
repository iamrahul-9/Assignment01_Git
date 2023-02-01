def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
    print(f"The product of {num1} and {num2} is: {multiply(num1, num2)}")

if __name__ == '__main__':
    main()