dreams = {}
poll_active = True

while poll_active:
	name = input("Please enter your name: ")
	place = input("Please enter name of place would you like to visit: ")

	dreams[name] = place

	print(f"Alright, {name}. I hope you can visit {place} soon!")

	poll = input("Dream vacation polling, press enter to continue or quit to exit program ")
	if poll == 'quit':
		poll_active = False

print("--- Polling Results ---")
if dreams:
	for name, place in dreams.items():
		print(f"\t{name} is would like to visit {place}")
else:
	print("Polling does not has any response")