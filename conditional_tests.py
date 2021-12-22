grade = "X"
majority = "CS"
name = "Wahyu Amirulloh"
enroll_year = 2020
prestige = 1

enrolled_students = ["Yaskur", "Ricardo"]

print("is grade == X ? Yes im on X grade")
print(grade == "X")

print("is majority == CI ? No im on CS")
print(majority == "CI")

print("is wahyu amirulloh attended ? yes")
print(name.lower() == "wahyu amirulloh")

print("minimum requirement to get scholarship is 2018 ? no")
print(enroll_year <= 2018)

print("scholarship is open for prestigious students")
print(prestige >= 1 or enroll_year <= 2018)

print("enrolled students can't apply for scholarship")
print(name.lower() in enrolled_students)

print("are you eligible to apply scholarship ? yes")
print(name.lower() not in enrolled_students and ( prestige >= 1 or enroll_year <= 2018 ))