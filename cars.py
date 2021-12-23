def make_car(manufacture, model, **car):
	car['manufacture'] = manufacture
	car['model'] = model
	return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)