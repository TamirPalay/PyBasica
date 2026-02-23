# Exercise : List #1

# 1. Print all values in the list
nums = [1, 2, 3, 4]
[print(n) for n in nums]

print("-----")

# 2. Print all values multiplied by 20
[print(n * 20) for n in nums]

print("-----")

# 3. First letter of each name
names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)

print("-----")

# 4. Even numbers only
nums2 = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums2 if n % 2 == 0]
print(evens)

print("-----")

# 5. Intersection of two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = [n for n in list1 if n in list2]
print(intersection)

print("-----")

# 6. Reverse words and lowercase
words = ["Elie", "Tim", "Matt"]
reversed_words = [word[::-1].lower() for word in words]
print(reversed_words)

print("-----")

# 7. Letters present in both strings
first = "first"
third = "third"
common_letters = [letter for letter in first if letter in third]
print(common_letters)

print("-----")

# 8. Numbers divisible by 12 from 1 to 100
divisible_by_12 = [n for n in range(1, 101) if n % 12 == 0]
print(divisible_by_12)

print("-----")

# 9. Remove vowels from "amazing"
word = "amazing"
no_vowels = [char for char in word if char not in "aeiou"]
print(no_vowels)

print("-----")

# 10. Generate [[0,1,2],[0,1,2],[0,1,2]]
list_3x3 = [[i for i in range(3)] for _ in range(3)]
print(list_3x3)

print("-----")

# 11. Generate 10x10 list from 0–9
list_10x10 = [[i for i in range(10)] for _ in range(10)]
print(list_10x10)
