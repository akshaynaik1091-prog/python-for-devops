for i in range(5):

    env = input("Enter the environment")
    print("The environment is: " + env)

    #a = int(input("Enter a number a 1: "))
    #b = int(input("Enter a number b 2: "))

    #print(" Data type of a is", type(a), "and data type of b is", type(b))
    #print("The sum of a and b is: ", a + b)
    #print("The difference of a and b is: ", a - b)
    #print("The product of a and b is: ", a * b)
    #print("The quotient of a and b is: ", a / b)

    if env == "prd":
        print("Don't deploy on friday")
    elif env == "stg":
        print("Take Backup & Test Well")
    else:
        print("Deploy on any day")