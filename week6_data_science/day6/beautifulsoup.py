from bs4 import BeautifulSoup


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie


print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...


# Kinds of objects
## Class tag
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(type(tag))

#### Name
print(tag.name)      # 'b'
tag.name = "blockquote"
tag                  # <blockquote class="boldest">Extremely bold</blockquote>

#### Attrs
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
tag['id']            # 'boldest'
tag.attrs            # {'id': 'boldest'}
tag.attrs.keys()     # dict_keys(['id'])
tag['id'] = 'verybold'
tag['another-attribute'] = 1
tag                  # <b another-attribute="1" id="verybold"></b>
del tag['id']
del tag['another-attribute']
tag                  # <b>bold</b>

#### Multi-valued attributes
css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
css_soup.p['class']  # ['body']

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
css_soup.p['class']  # ['body', 'strikeout']

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')    # not a Multi-valued attributes
id_soup.p['id']      # 'my id'

no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
no_list_soup.p['class']     # 'body strikeout'


## class NavigableString
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
tag.string                  # 'Extremely bold'
type(tag.string)            # <class 'bs4.element.NavigableString'>

unicode_string = str(tag.string)      # To unicode
unicode_string                        # 'Extremely bold'
type(unicode_string)                  # <type 'str'>

tag.string.replace_with("No longer bold")
tag                                   # <b class="boldest">No longer bold</b>

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
print(doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>


## Special strings
#### class comment
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
type(comment)                   # <class 'bs4.element.Comment'>
print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>