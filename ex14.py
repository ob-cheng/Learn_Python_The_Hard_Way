from sys import argv

script, user_name, few = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a {few} questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
So you said {likes} about me. 
You live in {lives}. 
And you have a {computer}. Nice!""")