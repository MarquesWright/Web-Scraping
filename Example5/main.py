from bs4 import BeautifulSoup

identical_class = """<p class="identical">Example of p tag with class identical</p>
                    <div class="identical">Example of div tag with class identical</div>"""

identicalsoup = BeautifulSoup(identical_class, "lxml")

# searching for a <div> tag with the class attribute value of "identical"
identical_div = identicalsoup.find("div", class_="identical")

print(identical_div)