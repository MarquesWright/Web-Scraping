from bs4 import BeautifulSoup


with open("ecologicalpyramid.html", "r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "lxml")

    # finding the producers within the <ul> tag using the find() method
    # producer_entries = soup.find("ul")

    # tag_li = soup.find("li")
    # tag_li = soup.find(name="li")

    # search for occurrence of "fox" within the html document
    # search_for_stringonly = soup.find(text="fox")

    # searching based on attribute values of a tag
    

    # prints the text stored in the <div> element within the <li> element
    # print(producer_entries.li.div.string)

    # prints the first occurrence of the <li> element
    # print(tag_li)

    # prints the occurrence of a string searched
    # print(search_for_stringonly)
