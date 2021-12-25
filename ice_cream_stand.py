from restaurant import Restaurant

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, *flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def print_flavors(self):
		print("We have variant of flavors")
		for flavor in self.flavors:
			print(flavor)

wall_ice = IceCreamStand("Walls Ice Cream", "Dessert", "Strawberry Ice Cream", "Chocolate Ice Cream", "Vanilla Ice Cream")

wall_ice.describe_restaurant()
wall_ice.print_flavors()