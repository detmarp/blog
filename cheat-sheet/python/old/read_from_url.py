#!/usr/bin/env python
import urllib2
import re

def remove_tag(tag, text):
    template = r"<tag[^>]*>([^<]*)</tag>"
    pattern = re.sub("tag", tag, template)
    return re.sub(pattern, r"\1", text)
    
def html_to_text(html):
    # todo, this regex stuff isn't really working
    text = html
    text = remove_tag("a", text)
    text = remove_tag("b", text)
    text = remove_tag("i", text)
    text = remove_tag("sup", text)
    return text

url = "https://en.wikipedia.org/wiki/Gunship_2000"
response = urllib2.urlopen(url)
text = response.read()
regex = re.compile(r"<p>(.*)</p>")

# search() finds the first match
result = regex.search(text)
if result:
    first_paragraph = result.group(1)
    print(first_paragraph)
    print
    print(html_to_text(first_paragraph))

