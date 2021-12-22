favorite_places = {
	"wahyu": {
		"japan": ["tokyo", "osaka"],
		"indonesia": ["jakarta", "bandung"]
	},
	"yuwandri": {
		"united states": ["new york", "oklahoma"],
		"united kingdom": ["manchester", "brooklyn"]
	},
	"yaskur": {
		"malaysia": ["kualalumpur", "putrajaya"],
		"thailand": ["bangkok", "pattaya"]
	}
}

for name, places in favorite_places.items():
	print(f"{name.title()} is want to visit")
	for country, cities in places.items():
		print(f"\t - {country.title()}")
		for city in cities:
			print(f"\t\t > {city.title()}")