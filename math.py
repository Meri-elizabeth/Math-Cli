import sys
operation = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])
if operation == "add":
    print(num1 + num2)
elif operation == "mul":
    print(num1 * num2)
elif operation == "sub":
    print(num1 - num2)
else:
    print("Invalid operation. Please use 'add', 'mul', or 'sub'.")