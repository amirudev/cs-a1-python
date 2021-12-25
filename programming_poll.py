reasons = {}
poll_program = True
filename = "programming_poll.txt"

while poll_program:
	name = input("Type your name ( type 'q' to quit program ): ")
	if name == 'q' or name == '':
		poll_program = False
	else:
		reason = input("Reason why you like programming: ")

		with open(filename, "a") as file_object:
			file_object.write(f"{name} - {reason}\n")
		