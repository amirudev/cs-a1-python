topping_prompt = "What toppings on Pizza would you like to add, type quit to exit the program \n"

while True:
	topping = input(topping_prompt)

	if topping == 'quit':
		break
	else:
		print(f"Great!, {topping} will be served on your Pizza")