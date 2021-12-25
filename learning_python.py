filename = "learning_python.txt"

with open(filename) as file_object:
	# Reading entire file
	# print(file_object.read())

	# Looping over file object
	# for line in file_object:
		# print(line.rstrip())

	# Storing the line in list
	lines = file_object.readlines()

# for line in lines:
# 	print(line.rstrip())

# Example of .replace() usage
for line in lines:
	text = line.replace("you", "python")
	print(text.rstrip())