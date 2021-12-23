def build_profile(firstname, lastname, **profile):
	profile['fullname'] = f"{firstname.title()} {lastname.title()}"
	return profile

profile_wahyu = build_profile("wahyu", "amirulloh", hobby="Programming", job="Students", dream="Programmer")

print(profile_wahyu)