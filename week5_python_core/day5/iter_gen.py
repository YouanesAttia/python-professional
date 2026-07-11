import re
import reprlib
from collections import abc

# Sentence Take #1: A Sequence of Words
RE_WORD = re.compile(r'\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __getitem__(self, key):
        return self.words[key]
    def __len__(self):
        return len(self.words)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
issubclass(Sentence, abc.Iterable)   # False


# Why Sequences Are Iterable: The iter Function
class Foo:
    def __iter__(self):
        pass

issubclass(Foo, abc.Iterable)   # True
f = Foo()
isinstance(f, abc.Iterable)     # True


# Iterables Versus Iterators
s = 'ABC'
for char in s:
    print(char)

s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
#  the best way to check if an object x is an iterator is to call isinstance(x, abc.Iterator).
s3 = Sentence('Pig and Pepper')
it = iter(s3)
next(it)        # Pig
next(it)        # and
next(it)        # Pepper
next(it)        # StopIteration
list(it)        # []
list(iter(s3))  # ['Pig', 'and', 'Pepper']


# Sentence Take #2: A Classic Iterator
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index +=1
        return word
    def __iter__(self):
        return self


# Sentence Take #3: A Generator Function
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        for word in self.words:   
            yield word   
        return  


# How a Generator Function Works
#### Any Python function that has the yield keyword in its body is a generator function
def gen_123():
    yield 1
    yield 2
    yield 3

gen_123       # <function gen_123 at 0x...> 
gen_123()     # <generator object gen_123 at 0x...>  
for i in gen_123(): 
    print(i)

g = gen_123()
next(g)        # 1
next(g)        # 2
next(g)        # 3
next(g)        # StopIteration

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

for c in gen_AB():
    print('-->', c)

### start    
### --> A   
###continue 
### --> B   
### end.


# Sentence Take #4: A Lazy Implementation
class Sentence:
    def __init__(self,text):
        self.text = text
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


