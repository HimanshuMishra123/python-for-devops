import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")


#The code provided will not find a match and will output "No match".
#The re.match function in Python attempts to match a pattern only at the beginning of the string. 
#Since the pattern r"quick" is not at the beginning of the string the match will fail. Better to use search or findall