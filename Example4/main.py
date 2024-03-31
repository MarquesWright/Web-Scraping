from bs4 import BeautifulSoup

customattr = """<p data-custom="custom">custom attribute example</p>"""

customsoup = BeautifulSoup(customattr, "lxml")

# the following will throw an error because keywords cannot have
# a '-' character in variable names

# customSoup.find(data-custom="custom")

# to avoid errors, pass in keyword arguments as a dictionary
# in the attrs argument
using_attrs = customsoup.find(attrs={'data-custom':'custom'})

print(using_attrs)