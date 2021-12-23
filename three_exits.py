topping_prompt = "What toppings on Pizza would you like to add, type quit to exit the program \n"
active = True

while active:
	topping = input(topping_prompt)

	if topping == 'quit':
		active = False
	else:
		print(f"Great!, {topping} will be served on your Pizza")