# Contributing

First of all, thanks for taking the time to give this project a hand! Here is the how-to:

## Remember:
- useful commit messages
- lower case file and function/class names
- always use the standard filename (sort.js, sort.ts, sort.cpp, not JSsort.js or MySpecialSort.cpp) (found in the `scripts` dict in `runner.py`)

## Adding a language
- First, go to `lang-config.json` and add your language's information there.
- Next, write any scripts you are interested in writing.
- Any that you don't want to write, or that don't really fit your language, go to `runner.py` and add your language's name to each `exclude` call in the `scripts` dictionary.
- Profit! Your language is now being benchmarked.

## Adding a script to an existing language
- First, write the script, using the convention outlined above.
- Then, remove your language's name from the the relevent `exclude` call(s)

