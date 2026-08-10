def sum_of_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    total = num1 + num2
    print(total)


env = input("Enter the environment: ")

print("The environment is: " + env)

if env == "prd":
    sum_of_num()