def send_messages(send_messages, sent_messages):
	while send_messages:
		message = send_messages.pop()
		sent_messages.append(message)

messages = ["Hello", "Good Morning", "Nice to meet you"]
messages_sent = []

print("Before:")
print(messages)
print(messages_sent)

print("After:")

send_messages(messages, messages_sent)

print(messages)
print(messages_sent)