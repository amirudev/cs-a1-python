sandwich_orders = ["Tuna Sandwich", "Pastrami", "Honey Sandwich", "Pastrami", "Ham Sandwich", "Pastrami"]
finished_sandwich = []

while sandwich_orders:
	while 'Pastrami' in sandwich_orders:
		sandwich_orders.remove('Pastrami')

	sandwich = sandwich_orders.pop()
	print(f"{sandwich} is being processed")
	finished_sandwich.append(sandwich)

print("All sandwiches orders are completed")
for sandwich in finished_sandwich:
	print(f"\t {sandwich}")