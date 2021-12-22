subdistricts = ["Cileungsi", "Gunungputri"]
# >> ['Cileungsi', 'Gunungputri', 'Jonggol']

subdistricts.append("Klapanunggal")
# >> ['Cileungsi', 'Gunungputri', 'Klapanunggal']

subdistricts.insert(1, "Jonggol")
# >> ['Cileungsi', 'Jonggol', 'Gunungputri', 'Klapanunggal']

del subdistricts[2]
# >> ['Cileungsi', 'Jonggol', 'Klapanunggal']

subdistricts.pop()
# >> ['Cileungsi', 'Jonggol']

subdistricts.pop(1)
# >> ['Cileungsi']

subdistricts.remove("Cileungsi")
# >> []

subdistricts = ["Cileungsi", "Jonggol", "Gunungputri", "Klapanunggal"]
# >> ['Cileungsi', 'Jonggol', 'Gunungputri', 'Klapanunggal']

subdistricts.sort()
# >> ['Cileungsi', 'Gunungputri', 'Jonggol', 'Klapanunggal']

subdistricts.sort(reverse=True)
# >> ['Klapanunggal', 'Jonggol', 'Gunungputri', 'Cileungsi']

subdistricts.reverse()
# >> ['Cileungsi', 'Gunungputri', 'Jonggol', 'Klapanunggal']

print(subdistricts)
print(f"length of list: {len(subdistricts)}")