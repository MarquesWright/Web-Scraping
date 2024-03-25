from bs4 import BeautifulSoup


with open("ecologicalpyramid.html", "r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "lxml")

    # Searching with find() method

    # finding the producers within the <ul> tag using the find() method
    # producer_entries = soup.find("ul")

    # tag_li = soup.find("li")
    # tag_li = soup.find(name="li")

    # search for occurrence of "fox" within the html document
    # search_for_stringonly = soup.find(text="fox")

    # searching based on attribute values of a tag
    # primary_consumers = soup.find(id="primaryconsumers")

    # searching based on the CSS class
    # css_class = soup.find(attrs={"class": "primaryconsumerlist"})
    # css_class = soup.find(class_="primaryconsumerlist")     # using the 'class_' keyword argument

    # searching using functions defined
    # finding the secondary consumers using functions within the find() method
    # def is_secondary_consumers(tag):
    #     return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

    # secondary_consumer = soup.find(is_secondary_consumers)

    # Searching with find_all() method
    # find_all() method has extra parameter, limit

    # finding all tertiary consumers
    # all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")

    # iterate through this list to display all tertiary consumer names
    # for tertiaryconsumer in all_tertiaryconsumers:
    #     print(tertiaryconsumer.div.string)

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
