import cars
from user_profile import build_profile
from sandwiches import make_sandwich as ms
import city_names as cn
from album import *

# Import 1
car = cars.make_car("Honda", "Brilink", color="Black", origin="Japan")
print(car)

# Import 2
profile = build_profile("Wahyu", "Amirulloh", job="Students", credit="Good", score="78")
print(profile)

# Import 3
ms("Tomato", "Pepperoni", "Tomato Sauce")

# Import 4
city = cn.city_country("Bogor", "Indonesia")
print(city)

# Import 5
album = make_album("Kenshi Yonezu", "Yankee", 8)
print(album)

