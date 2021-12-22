cities = {
	"jakarta": {
		"country": "indonesia",
		"population": 10_600_000,
		"areas": 661
	},
	"amsterdam": {
		"country": "dutch",
		"population": 821_000,
		"areas": 219
	},
	"tokyo": {
		"country": "Japan",
		"population": 13_960_000,
		"areas": 2_194
	}
}

for city, information in cities.items():
	print(f"{city} is a city in {information['country']} with population {information['population']} and areas {information['areas']}")
	print(f"{city} Density: {information['population'] / information['areas']} people / squares km")