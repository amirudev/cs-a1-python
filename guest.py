filename = "guest.txt"
guest = input("Type your name: ")

with open(filename, "w") as file_object:
	file_object.write(guest)