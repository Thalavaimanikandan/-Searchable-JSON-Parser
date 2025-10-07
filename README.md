Suggested Folder Structure
Searchable‑JSON‑Parser/
├── README.md
├── LICENSE
├── json_parser.py
├── sample.json
├── tests/
│   └── test_parser.py
└── examples/
    └── example_usage.py

File Contents
README.md
# Searchable JSON Parser

A parser for JSON built using regex + recursion, with capabilities to search/query within the parsed structure.

## Features

- Parse JSON strings (objects, arrays, strings, numbers, booleans, null)  
- Represent parsed JSON data in Python classes  
- Query / search by key, path, value conditions  
- Minimal dependencies (uses Python standard library)  
- Example usage, tests included  

## Installation & Usage

1. Clone or download:

   ```bash
   git clone https://github.com/Thalavaimanikandan/Searchable-JSON-Parser.git
   cd Searchable-JSON-Parser


(Optional) Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate


Use in your script:

from json_parser import JSONParser

s = '{"name":"Alice","age":30,"address":{"city":"Wonderland"},"tags":["friend","explorer"]}'
parser = JSONParser(s)
obj = parser.parse()

# Search for all occurrences of “city”
results = obj.search_by_key("city")
print(results)  # e.g. ["Wonderland"]

Folder Layout

json_parser.py — core parser & data model

sample.json — sample JSON for testing

examples/example_usage.py — example script showing how to use the parser

tests/test_parser.py — basic unit tests

LICENSE — open source license

Running Tests
pytest tests/


or

python -m unittest discover tests

Contributing

Feel free to add new query / filter methods

Add better error handling, edge case support

Optimize performance (e.g. large JSON, streaming)

Add more tests

License
MIT License

Copyright (c) 2025 Thalavaimanikandan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[... full MIT license text ...]


---

### LICENSE

Place the full MIT license (or whichever license you prefer). Example:



MIT License

Copyright (c) 2025 Thalavaimanikandan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
