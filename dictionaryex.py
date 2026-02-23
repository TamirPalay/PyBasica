# 🌟 Exercise 1 : Dictionary Exercises

# 1️⃣ Convert list of tuples into dictionary
pairs = [("name", "Elie"), ("job", "Instructor")]
dict_from_pairs = {key: value for key, value in pairs}
print(dict_from_pairs)

print("-----")

# 2️⃣ Combine two lists into dictionary using zip
states = ["CA", "NJ", "RI"]
full_names = ["California", "New Jersey", "Rhode Island"]
state_dict = {abbr: name for abbr, name in zip(states, full_names)}
print(state_dict)

print("-----")

# 3️⃣ Dictionary of vowels with value 0
vowels_dict = {vowel: 0 for vowel in "aeiou"}
print(vowels_dict)

print("-----")

# 4️⃣ Alphabet position dictionary (1–26 → A–Z)
alphabet_dict = {i: chr(64 + i) for i in range(1, 27)}
print(alphabet_dict)

print("-----")

# 🌟 Super Bonus
# Count vowels in "awesome sauce"

string = "awesome sauce"
vowel_count = {vowel: string.count(vowel) for vowel in "aeiou"}
print(vowel_count)
