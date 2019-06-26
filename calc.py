user_input1 = float(input("Enter a number:"))
op = input("Enter the operator:")
user_input2 = float(input("Enter the second number number:"))


if op == "+" :
    print(user_input1 + user_input2)
elif op == "-":
    print(user_input1 - user_input2)
elif op == "/":
    print(user_input1 / user_input2)
elif op == "*":
    print(user_input1 * user_input2)
elif op == "**":
    print(user_input1 ** user_input2)
else:
    print("Sorry you entered an invalid operator!")
	

