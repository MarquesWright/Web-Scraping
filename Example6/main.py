import re
from bs4 import BeautifulSoup

email_id_example = """<br/>
<div>The below HTML has information that has email ids.</div>abc@example.com<div>xyz@example.com</div>
<span>foo@example.com</span>
"""

soup = BeautifulSoup(email_id_example, "lxml")

# created a regular expression for the email ID
emailid_regexp = re.compile("\w+@\w+\.\w+")

# passed emailid_regexp in the find_all() method to find all text matching pattern
email_ids = soup.find_all(text=emailid_regexp)

# using limit parameter to determine how many emails are returned if found
email_ids_limited = soup.find_all(text=emailid_regexp, limit=2)

# print results
# print(email_ids)

# print the number of emails determine by 'limit' parameter
print(email_ids_limited)