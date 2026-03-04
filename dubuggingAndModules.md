What is a Module?
A module is a file containing Python code (functions, classes, variables) that can be reused across different programs. It helps organize code into logical, reusable units.

Three Ways to Import a Module
python# 1. Import the whole module
import random

# 2. Import a specific item from a module
from random import randint

# 3. Import with an alias
import random as rnd

Purpose of Importing
Importing lets you reuse existing code without rewriting it — accessing built-in Python tools, third-party libraries, or your own modules to extend your program's functionality.

Three Examples Using the random Module
pythonimport random

# 1. Pick a random number between 1 and 10
random.randint(1, 10)

# 2. Shuffle a list (e.g. a deck of cards)
random.shuffle(deck)

# 3. Pick a random item from a list
random.choice(["rock", "paper", "scissors"])

What is an ImportError?
An ImportError is raised when Python cannot find or load a module you're trying to import.
pythonimport numpy  # ImportError if numpy isn't installed
Common causes:

Module not installed (pip install <module>)
Typo in the module name
Module not in Python's path


When is OrderedDict Useful?
Use OrderedDict when the insertion order of keys matters and you need to rely on it explicitly — e.g. building an LRU cache, processing config files in sequence, or maintaining a log of events.
pythonfrom collections import OrderedDict

steps = OrderedDict()
steps["step1"] = "Load data"
steps["step2"] = "Clean data"
steps["step3"] = "Train model"

Note: Regular dict preserves order in Python 3.7+, but OrderedDict makes the intent explicit and supports .move_to_end().


When is defaultdict Useful?
Use defaultdict when you want to avoid KeyError by automatically providing a default value for missing keys — great for grouping, counting, or building nested structures.
pythonfrom collections import defaultdict

# Grouping words by first letter
groups = defaultdict(list)
for word in ["apple", "ant", "banana"]:
    groups[word[0]].append(word)
# {'a': ['apple', 'ant'], 'b': ['banana']}

Purpose of if __name__ == '__main__':
pythonif __name__ == '__main__':
    pass
This block runs only when the file is executed directly, not when it's imported as a module.
Scenario__name__ valueRun directly (python app.py)'__main__' → block runsImported by another file'app' → block skipped
Why use it? It lets you write code that tests or runs your module standalone, without accidentally executing it when another file imports it.
