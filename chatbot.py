import random

greetings=["hello","hey","wassup"]
responses=["hi", "bonjour","hallo"]

questions=["how are you?", "how you doin"]
answer=["good","okay","fine"]

while True:
	ask=input(">>>")
	if ask in greetings:
		randomResponse=random.choice(responses)
		print(randomResponse)
	elif ask in questions:
		randomResponse=random.choice(answers)
		print(randomResponse)
	else:
		print("what?")
