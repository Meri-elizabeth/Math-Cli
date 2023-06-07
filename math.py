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
elif operation == "combine":
    result = num1 + num2
    operation2 = sys.argv[4]
    num3 = int(sys.argv[5])

    if operation2 == "mul":
        result *= num3
    elif operation2 == "sub":
        result -= num3
    elif operation2 == "add":
        result += num3
    elif operation2 == "divide":
        result /= num3
    else:
        print("Invalid additional operation. Please use 'mul' or 'sub'.")
    print(result)
else:
    print("Invalid operation. Please use 'add', 'mul', or 'sub'.")