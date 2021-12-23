sandwich_orders = ["Tuna Sandwich", "Honey Sandwich", "Ham Sandwich"]
finished_sandwich = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"{sandwich} is being processed")
	finished_sandwich.append(sandwich)

print("All sandwiches orders are completed")
for sandwich in finished_sandwich:
	print(f"\t {sandwich}")