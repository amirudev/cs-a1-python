rivers = {
	"amazon": "south america",
	"nile": "africa",
	"yangtze": "china"
}

for river, location in rivers.items():
	print(f"{river} run through {location}")

print("River name list")
for river in rivers.keys():
	print(f"{river}")

print("River locations")
for location in rivers.values():
	print(f"{location}")