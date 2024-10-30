print("Welcome to the calculator")

num1 = float(input("Insert the first number: "))
num2 = float(input("Insert the second number: "))
operation = input("Insert the operation (+, -, *, /): ")
result = 0

if (operation == "*"):
   result = num1 * num2
elif (operation == "+"):
   result = num1 + num2
elif (operation == "-"):
   result = num1 - num2
elif (operation == "/"):
   if (num2 == 0):
      result = "Undefined"
      print("Invalid operation")
   else:
      result = num1 / num2
else:
   (print("Invalid operation"))
 

print(f'The result is {round(result, 2)}')