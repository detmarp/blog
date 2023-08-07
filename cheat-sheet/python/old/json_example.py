#!/usr/bin/env python
import json

def save():
    None

def load():
    with open('strings.json') as json_data:
        d = json.load(json_data)
        print(d)

def main():
    filename = "json_out.json"
    d = {"one":1,"two":2, "array":[1, "two", 3.0], "bool":True, "unicode":u"\u00A9\u00BD\u00C2"}
    with open(filename, "w") as file:
        # dump() - for writing to file
        json.dump(d, file, sort_keys = True, indent = 4)

    # dumps() for writing to string
    print "as json..."
    print(json.dumps(d))    

    print "as python..."
    with open(filename) as json_data:
        d = json.load(json_data)
        print(d)
    print "...here's the unicode string (copyright, half. A-hat)", d["unicode"]

if __name__ == "__main__":
    main()