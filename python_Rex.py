import re

#Python Regular Expressions Mastery
#Task 1:Code Correction

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
print(emails)

text2 = "Contact emails are: linda@example.com and coriander_123@example.com."
emails2 = re.findall(r"[\w]+@[\w]+\.[A-Z|a-z]{2,}", text2)
print(emails2)

#Python Regular Expressions Deep Dive
#Task 1:Email Extraction Enhancement

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[^exclude]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

#3. Advanced Text Processing with Python Regex
#Task 1:Advanced Data Extraction

texture = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

# Extract the Occupation from the text

t_pattern = r"Occupation: (\w*)"
textures = re.findall(t_pattern, texture)
for word in textures:
    print(word)

#4 Python Regex Challenge: Enhancing E-Commerce Operations
#Task 1:Product Description Keyword Tagging

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"]


moddescript = re.split(r",", ",".join(descriptions))
print(moddescript)

key = "smartphone", "t-shirt", "kitchen knife set"
key1 = "229.98", "9.99", "59.74"

for i in range(len(moddescript)):
    moddescript[i] = re.sub(r"[\w.]^[key[i]]*", " ", moddescript[i])
    print(f"{moddescript[i]} , priced at ${key1[i]}.")












