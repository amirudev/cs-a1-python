my_car = "Wuling"
yaskur_car = "Honda"
my_fuel = 100
astra_membership = True
your_card = ["Brizzi", "Mandiri", "Flazz"]

if my_car.lower() == "wuling":
	print("Wuling is a Korean car company")
else:
	print("Maybe you're buying a Japan car")

print("Recommended Trip: ")
if my_fuel > 300:
	print("Jakarta - Yogyakarta")
elif my_fuel >= 100:
	print("Jakarta - Semarang")
elif my_fuel < 5:
	print("Nearest Gas Station")
elif my_fuel <= 20:
	print("Home")
else:
	print("Inner City Trip")

if my_fuel <= 100 and my_car.lower() == "wuling":
	print("Your fuel will be run out in 500km")

if astra_membership == True or my_car.lower() == "Honda":
	print("Free Car Check Up for period Dec 15th to Dec 25th")

if "Brizzi" in your_card:
	print("Indonesian Local Bank BRI Promo! Discount 30% for every gas station")

if "Jaklingko Brizzi" not in your_card:
	print("Buy Jaklingko edition card! Jaklingko gives you more benefit for Jakartans")