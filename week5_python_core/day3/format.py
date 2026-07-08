import  re

name = input("Name: ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(1) + " " + matches.group(2)

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(1) + " " + matches.group(2)


# re.sub(pattern, repl, string, count=0, flags=0)
url = input("URT: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Username: {username}")