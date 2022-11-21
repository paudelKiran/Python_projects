import re
# This program generally takes a text and separate the emails present there
email_template = r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+"
text = input("Please enter the text :-->\t")
emails = re.findall(email_template, text)
print(emails)
