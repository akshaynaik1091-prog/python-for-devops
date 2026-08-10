from unicodedata import name


num = int(input("Enter a number: "))    

name = input("enter your name")
print(f"hello, {name}")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Akshay = "Krishna"

# while Akshay == "Krishna":
 #   print("Hello Krishna")
    #break

# Real World

choice = input("Enter your choice (Press q to quit) ")

while choice != "q":
    for i in range(1, 11):
        print(f" {num} x {i} = {num * i}")
    choice = input("Enter your choice (Press q to quit) ")