# regex and regular expressions
import re

text = "We are learning regular expressions in Python"

pattern = "ar"

match = re.search(pattern, text)

#print(match.group())

# if match:
#     print(f"Match found : {match.group()}")
# else:
#     print("Match not found")   

# characters
# . - take a place of a single character 
# ^ - match the start of a string
# $ - match the end of a string
# * -match 0, or more repetitions- take the precedence order

# text = "accb a1b aab axb"
# pattern = "a*b"

# matches = re.findall(pattern, text)
# print(matches)

# text = "Hello World "
# pattern = r"^He"

# matches = re.findall(pattern, text)
# print(matches)

# character class
# [abc] - it will for a characterin the order abc 
# [a-z] -it will match any lowercase character
# [0-9]- it will match any digit
# [a-zA-Z0-9] -any alphanumeric charcter
# \d - matches any digit
# \w-matches any word
# \s -matches any whitespace character

text = " My phone number is 123-456-7890"
pattern = r"\d+"

matches = re.findall(pattern, text)
print(matches)
