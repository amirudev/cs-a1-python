filename = "gutenberg.txt"
with open(filename) as file_object:
	gutenberg = file_object.read()

print(gutenberg.lower().count("the"))