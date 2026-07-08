import re

email = input("Email: ").strip()

# re.search(pattern, string, flag=0)
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net)$ ", email, re.IGNORECASE):  # \w is the same as [a-zA-Z0-9_]
    print('Valid')
else:
    print('Invalid')
