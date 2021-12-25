class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"{self.restaurant_name} is an extraordinary restaurant")
		print(f"We served {self.cuisine_type}")
		print(f"We have serve {self.number_served} meals!")

	def open_restaurant(self):
		print(f"{self.restaurant_name} now on business! find our store with Google Maps")

	def set_number_served(self, served):
		self.number_served = served

	def increment_number_served(self, served):
		self.number_served += served

mcdonalds = Restaurant("McDonalds", "Fast Food")
mcdonalds.set_number_served(10)
mcdonalds.increment_number_served(5)

mcdonalds.describe_restaurant()