# Exercise: if-elif-else statements

# Prompt the user to enter a number
numberOne = int(input("Enter a number: "))

# Prompt the user to enter an operator (+ - * /)
signs = input("Enter an operator (+ - * /): ")

# Prompt the user to enter another number
numberTwo = int(input("Enter another number: "))

# Perform the appropriate mathematical operation based on the operator
if signs == "+":
    answer = numberOne + numberTwo
elif signs == "-":
    answer = numberOne - numberTwo
elif signs == "*":
    answer = numberOne * numberTwo
elif signs == "/":
    answer = numberOne / numberTwo
else:
    print("Invalid operator!")

# Print the rounded answer
print(round(answer))

# Prompt the user to enter a temperature in Celsius
temp = int(input("Enter a temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = temp * 9 / 5 + 32

# Print the rounded Fahrenheit temperature
print(round(fahrenheit))
