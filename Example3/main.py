import re
from bs4 import BeautifulSoup

email_id_example = """<br/>
<div>The below HTML has information that has email ids.</div>
 abc@example.com
<div>xyz@example.com</div>
<span>foo@example.com</span>
"""

soup = BeautifulSoup(email_id_example, "lxml")

# created a regular expression for the email ID
emailid_regexp = re.compile("\w+@\w+\.\w+")

# passed emailid_regexp in the find() method to find first text matching pattern
first_email_id = soup.find(text=emailid_regexp)
print(first_email_id)
