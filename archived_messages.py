def archive_messages(archive_messages, archived_messages):
	while archive_messages:
		message = archive_messages.pop()
		archived_messages.append(message)

messages = ["Hello", "Good Morning", "Nice to meet you"]
messages_archived = []

print("Before:")
print(messages)
print(messages_archived)

print("After:")

archive_messages(messages[:], messages_archived)

print(messages)
print(messages_archived)