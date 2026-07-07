name = input("What's your name?")

with open('names.txt', 'a') as file:
    file.write(f"{name}\n")

# file.close() We may not call it if we use with

with open('names.txt', "r") as file:
    lines = file.readlines()
for line in lines:
    print("Hello, ", line.rstrip())