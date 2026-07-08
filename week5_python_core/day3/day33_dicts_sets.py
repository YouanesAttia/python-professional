import collections

text = "python is fast python is simple python is powerful"
words = text.split()
my_dict = {}

for word in words:
    if word in my_dict:
        my_dict[word] = my_dict[word] + 1
    else:
        my_dict[word] = 1
print(my_dict)
print(f"Code Length: ~6 line logic")


ct = collections.Counter(words)
print(ct)
print(f"Code Length: 1 line logic")


phone_book = collections.defaultdict(list)

def add_contact(name, num):
    phone_book[name].append(num)

add_contact("Alice", "555-0101")
add_contact("Alice", "555-9999") 
add_contact("Bob", "555-2020")
add_contact("Charlie", "555-3030")

print(phone_book)