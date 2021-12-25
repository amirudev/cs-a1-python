guest_program = True
filename = "guest_book.txt"
guests = []

while guest_program:
	guest = input("Type your name ( type 'q' to quit program ): ")
	if guest == 'q':
		guest_program = False
	else:
		guests.append(guest)

with open(filename, "w") as file_object:
	for guest in guests:
		file_object.write(f"{guest}\n")