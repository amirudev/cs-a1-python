class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} is an extraordinary restaurant")
		print(f"We served {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.restaurant_name} now on business! find our store with Google Maps")

# mcdonalds = Restaurant("McDonalds", "Fast Food Meals")

# print(mcdonalds.restaurant_name)
# print(mcdonalds.cuisine_type)

# mcdonalds.describe_restaurant()
# mcdonalds.open_restaurant()

# kfc = Restaurant("KFC", "Fried Chicken")
# kopikenangan = Restaurant("Kopi Kenangan", "Coffee Shop")
# wartegbahari = Restaurant("Warteg Bahari", "Traditional Fast Food")

# kfc.describe_restaurant()
# kopikenangan.describe_restaurant()
# wartegbahari.describe_restaurant()