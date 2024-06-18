import re

# Sample text containing email addresses
text = "Contact us at support@example.com or sales@example.com"

# Regular expression pattern
pattern = r"(\w+@\w+\.\w+)"

# Use re.findall to find all matches of the pattern in the text
matches = re.findall(pattern, text)

# Print all matches
for match in matches:
    print("Match found:", match)
