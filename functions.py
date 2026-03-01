def difference(a,b):
  return a-b
difference(2,2)

def print_day(num):
  if num<1 or num>7:
    return None
  day ={1: "Sunday", 2: "Monday", 3: "Tuesday", 4:"Wednesday", 5:"Thursday", 6: "Friday", 7:"Saturday"}
  return day[num]

print_day(4)

def last_element(list):
  if not list:
    return None
  return list[-1]

last_element ([])

def number_compare(a, b):
    if a > b:
        return "First is greater."
    if b > a:
        return "Second is greater."
    return "Numbers are equal."

def single_letter_count(word,letter):
  count=0
  for i in word.upper() :
    if letter.upper() == i:
      count+=1
  return count
single_letter_count('amazing','A')

def multiple_letter_count(string):
    return {ch: string.count(ch) for ch in string}

def list_manipulation(lst, command, location, value=None):
    if command == "remove" and location == "end":
        return lst.pop()
    if command == "remove" and location == "beginning":
        return lst.pop(0)
    if command == "add" and location == "beginning":
        lst.insert(0, value)
        return lst
    if command == "add" and location == "end":
        lst.append(value)
        return lst


def is_palindrome(string):
    cleaned = "".join(ch.lower() for ch in string if not ch.isspace())
    return cleaned == cleaned[::-1]


def frequency(lst, search_term):
    return sum(1 for x in lst if x == search_term)


def flip_case(string, letter):
    target = letter.lower()

    return "".join(
        ch.swapcase() if ch.lower() == target else ch
        for ch in string
    )


def multiply_even_numbers(lst):
    evens = [n for n in lst if n % 2 == 0]
    return reduce(operator.mul, evens, 1)


def mode(nums):
    counts = {n: nums.count(n) for n in set(nums)}
    return max(counts, key=counts.get)


def capitalize(string):
    return string[:1].upper() + string[1:]


def compact(lst):
    return [x for x in lst if x]


def partition(lst, callback):
    truthy = [x for x in lst if callback(x)]
    falsy = [x for x in lst if not callback(x)]
    return [truthy, falsy]


def intersection(list1, list2):
    return [x for x in list1 if x in list2]


def once(fn):
    def inner(*args, **kwargs):
        if inner.has_run:
            return None
        inner.has_run = True
        return fn(*args, **kwargs)

    inner.has_run = False
    return inner

