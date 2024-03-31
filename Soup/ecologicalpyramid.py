from bs4 import BeautifulSoup


with open("ecologicalpyramid.html", "r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "lxml")

    # SEARCHING USING find() METHOD

    # finding the producers within the <ul> tag using the find() method
    # producer_entries = soup.find("ul")

    # tag_li = soup.find("li")
    # tag_li = soup.find(name="li")

    # search for occurrence of "fox" within the html document
    # search_for_stringonly = soup.find(text="fox")

    # searching based on attribute values of a tag
    # primary_consumers = soup.find(id="primaryconsumers")

    # Searching based on the CSS class
    # css_class = soup.find(attrs={"class": "primaryconsumerlist"})
    # css_class = soup.find(class_="primaryconsumerlist")     # using the 'class_' keyword argument

    # Searching using functions defined
    # finding the secondary consumers using functions within the find() method
    # def is_secondary_consumers(tag):
    #     return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

    # secondary_consumer = soup.find(is_secondary_consumers)

    # SEARCHING WITH find_all() METHOD
    # find_all() method has extra parameter, limit, which limits the number of results you get

    # finding all tertiary consumers
    # all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")

    # iterate through this list to display all tertiary consumer names
    # for tertiaryconsumer in all_tertiaryconsumers:
    #     print(tertiaryconsumer.div.string)

    # Understanding parameters used with find_all()

    # searching for all text within the document
    # all_texts = soup.find_all(text=True)

    # searching for a list of strings
    all_texts_in_list = soup.find_all(text=["plants", "algae"])

    # PRINT METHODS FOR DISPLAYING EXAMPLES

    # prints the text stored in the <div> element within the <li> element
    # print(producer_entries.li.div.string)

    # prints the first occurrence of the <li> element
    # print(tag_li)

    # prints the occurrence of a string searched
    # print(search_for_stringonly)

    # prints the value of a tag based on attribute
    # print(primary_consumers.li.div.string)

    # prints the css class being searched
    # print(css_class)

    # prints the first secondary consumer
    # print(secondary_consumer.li.div.string)

    # prints the type of the variable
    # print(type(all_tertiaryconsumers))

    # prints out all the tags associated with soup object
    # print(soup.find_all(True))

    # prints every text content within the soup object including the new-line characters
    # print(all_texts)

    # prints strings that are defined in a list
    print(all_texts_in_list)
