from bs4 import BeautifulSoup


html_atag = """<html>
                    <body>
                        <p>Test html a tag example</p>
                        <a href="http://www.packtpub.com">Home</a>
                        <a href="http://www.packtpub.com/books">Books</a>
                    </body>
                </html>"""

soup = BeautifulSoup(html_atag, 'lxml')         # Creating a BeautifulSoup object with parser

# Accessing the first occurrence of the <a> tag
atag = soup.a

# Accessing the name of the tag object via the .name property
tagname = atag.name

# Changing the name of the tag via the .name property
atag.name = 'p'

# Retrieving the text stored inside a tag
first_a_string = atag.string


# print(atag)                 # prints the first <a> tag in the document
# print(tagname)              # prints the name of the tag object
# print(soup)                 # prints with the first <a> tag replaced with the <p> tag
# print(atag['href'])         # prints the href value associated with the <a> tag
# print(atag.attrs)           # accessing attributes with the .attrs property
# print(first_a_string)       # prints the text stored within the <a> tag
