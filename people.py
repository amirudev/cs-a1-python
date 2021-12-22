users = {
	"wahyu": {
		"first_name": "Wahyu",
		"last_name": "Amirulloh",
		"subdistrict": "Cileungsi"
	},
	"yaskur": {
		"first_name": "Yaskur",
		"last_name": "Fauzan",
		"subdistrict": "Citeureup"
	},
	"yuwandri": {
		"first_name": "Yuwandri",
		"last_name": "Alfarizi",
		"subdistrict": "Gunungputri"
	}
}

for user, user_info in users.items():
	print(f"Username: {user}")
	print(f"\tFull Name: {user_info['first_name']} {user_info['last_name']}")
	print(f"\tSubdistricts: {user_info['subdistrict']}")