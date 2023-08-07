#!/usr/bin/env python
import sys
import os
import re

"""
some strings to match against:
<TextureAtlas imagePath="yes1.png"
  <TextureAtlas   imagePath  =  "yes2.png"
<TextureAtlas imagePath=  "yes3.png"
< TextureAtlas imagePath="no1.png"
<TextureAtlas image="no2.png"
<TextureAtlas other stuff imagePath "no3.png"
<TextureAtlas other stuff imagePath "no4.png"
<TextureAtlas imagePath="yes4.png"
"""

def main(filepath):
    file = open(filepath, 'r')
    text = file.read()
    file.close()
    # find the "file" with the character on each side
    matches = re.findall("(.file.)", text)
    print matches

    # try to extract png names, from context like this: <TextureAtlas imagePath="farm_01_anim.png"
    matches = re.findall("<TextureAtlas\s*imagePath\s*=\s*\"(.*.png)\"", text)
    print matches
        
if __name__ == "__main__":
    main(os.path.abspath(sys.argv[0]))