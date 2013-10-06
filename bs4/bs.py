html_doc= """<html><head><title>The Dormouse's story</title></head> <body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
from pprint import pprint
soup = BeautifulSoup(html_doc)
print(soup.prettify())
print('-'*50)
print(soup.head)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(type(soup.p)) # Tag
print(soup.p.attrs) # attrs
print(soup.p['class'])
print(type(soup.p.string))# NavigableString
print(unicode(soup.p.string)) # NavigableString--->Unicode string
pprint(soup.find_all('p'))
print('-'*20)
print(soup.a)
print(type(soup.a)) # Tag
print(soup.a.attrs) # attrs
print(soup.a['class'])
pprint(soup.find_all('a'))
print(soup.find(id='link3'))

print('-'*20)
# extract all URLs
for link in soup.find_all('a'):
	#print(link.get('href'))
	print(link['href'])

print('-'*20)
# get all text
print(soup.get_text())

"""
tag:
	A Tag object corresponds to an XML or HTML tag in the original document:

name: 
	Every tag has a name, accessible as .name:

attributes:
	A tag may have any number of attributes.You can access a tags attributes by treating the tag like a dictionary:
"""

# multi-valued attributes
# class is multi-valued
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print(css_soup.p['class'])
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
print(css_soup.p['class'])
# ["body"]

# id is NOT multi-valued
id_soup = BeautifulSoup('<p id="my id"></p>')
print(id_soup.p['id'])
# 'my id'

#If you parse a document as XML, there are no multi-valued attributes:
#xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
#xml_soup.p['class']
# u'body strikeout'

#NavigableString
tag = soup.p
print(tag.string)
# u'Extremely bold'
print(type(tag.string))
# <class 'bs4.element.NavigableString'>

unicode_string = unicode(tag.string)
print(unicode_string)
# u'Extremely bold'
print(type(unicode_string))
# <type 'unicode'>

# You cant edit a string in place, but you can replace one string with another, using replace_with():
tag.string.replace_with("No longer bold")
print(tag)
# <blockquote>No longer bold</blockquote>


# The Comment object is just a special type of NavigableString:
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
markup_soup = BeautifulSoup(markup)
comment = markup_soup.b.string
print(type(comment))
# <class 'bs4.element.Comment'>
print(comment)
print(markup_soup.b.prettify())

# Navigating the tree
# Navigating using tag names
# If you need to get all the <a> tags, or anything more complicated than the first tag with a certain name, you'll need to use one of the methods described in Searching the tree, such as find_all():

# contents             children                    descendants
# list(direct child)  list iterator(direct child) list iterator(all child)
print('*'*30)
head_tag = soup.head
print(head_tag)
print(head_tag.name)
print(head_tag.string)
print(head_tag.attrs) # dict
print(len(head_tag.contents)) # 1
print(len(list(head_tag.children))) # 1
print(len(list(head_tag.descendants))) # 2
title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

# BeautifulSoup 
print('*'*30)
print(soup.name) # document
print(soup.original_encoding) 
print(soup.string) # None
print(soup.attrs) # {}
print(len(soup.contents)) # 1
print(len(list(soup.children))) # 1
print(len(list(soup.descendants))) # 26
html_tag = soup.contents[0]
print(html_tag.name)

print('-'*20)
print("way 1 to iterate")
l = len(html_tag)
for i in range(l): 
	tagi = html_tag.contents[i]
	print(tagi.name)
print("way 2 to iterate")
for child_tag in html_tag.children:
	if child_tag.name:
		print(child_tag.name)

print("way 3 to iterate")
# The .descendants attribute lets you iterate over all of a tags children, recursively: its direct children, the children of its direct children, and so on:
for child_tag in html_tag.descendants:
	if child_tag.name:
		print(child_tag.name)

print('-'*30)
print('strings')
# strings and stripped_strings: list iterator
for string in soup.strings:
	print(repr(string))
print('stripped_strings')
# Here, strings consisting entirely of whitespace are ignored, and whitespace at the beginning and end of strings is removed.
for string in soup.stripped_strings:
	print(repr(string))

# parent
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>
title_tag.string.parent
# <title>The Dormouse's story</title>

html_tag = soup.html
type(html_tag.parent)
# <class 'bs4.BeautifulSoup'>
soup.parent
# None

# parents: list iterator
print('*'*20)
link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
# p
# body
# html
# [document]
# None

# .next_sibling and .previous_sibling
# .next_siblings and .previous_siblings

# Searching the tree
# find() and find_all()
# Kinds of filters: 
# string
soup.find_all('b')
# [<b>The Dormouse's story</b>]

# A regular expression
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

for tag in soup.find_all(re.compile("t")):
    print(tag.name)
# html
# title

# A list
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,

print('*'*20)
# True
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p

# A function
def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were...</p>,
#  <p class="story">...</p>]
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# find_all()
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]


# Searching by CSS class using "class_"
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(class_=re.compile("itl"))
# [<p class="title"><b>The Dormouse's story</b></p>]

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

soup.find_all(class_=has_six_characters)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.find_all("p", class_="strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="strikeout body")
# []

soup.find_all("a", attrs={"class": "sister"})
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# text
# With text you can search for strings instead of tags.
soup.find_all(text="Elsie")
# [u'Elsie']

soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return (s == s.parent.string)

soup.find_all(text=is_the_only_string_within_a_tag)
# [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']

soup.find_all("a", text="Elsie")
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]

# limit
soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# recursive
soup.html.find_all("title")
# [<title>The Dormouse's story</title>]

soup.html.find_all("title", recursive=False)
# []

# Beautiful Soup offers a lot of tree-searching methods (covered below), and they mostly take the same arguments as find_all(): name, attrs, text, limit, and the keyword arguments. But the recursive argument is different: find_all() and find() are the only methods that support it. Passing recursive=False into a method like find_parents() wouldnt be very useful.

# Calling a tag is like calling find_all()
soup.find_all("a")
soup("a")

soup.title.find_all(text=True)
soup.title(text=True)


# These two lines of code are nearly equivalent:
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>

soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>


# CSS selectors
soup.select("title")
# [<title>The Dormouse's story</title>]
