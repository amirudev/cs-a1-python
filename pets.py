pets = {
	"george": {
		"animal": "Monkey",
		"owner": "Yellow Hat"
	},
	"bilu": {
		"animal": "Fish",
		"owner": "Mela"
	},
	"yaskur": {
		"animal": "Human",
		"owner": "Yuwandri"
	}
}

for name, info in pets.items():
	print(f"Pet named {name} is a {info['animal']}, its owned by {info['owner']}")