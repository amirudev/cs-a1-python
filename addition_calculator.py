calculator_program = True

while calculator_program:
	try:
		number_1 = int(input("Type first number: "))
		number_2 = int(input("Type second number: "))
	except ValueError:
		print("Sorry, you are not typing number correctly. Lets try again")
		continue
	else:
		print(f"{number_1} + {number_2} = {number_1 + number_2}")
		calculator_program = False