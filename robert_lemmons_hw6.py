#!/usr/bin/env python3
import sys
import re
from urllib.request import urlopen

"""
Create a script that opens an Apache server error log file
 and retrieves the top 25 errors
"""


def logFile(url):
    """
    use URLOPEN to retrieve log file
    create a very convoluted regex
    sort information in a dict
    """
    exp = "[' ](\/[^\s',]+)"
    p = re.compile(exp)
    d = {}
    

    with urlopen(url) as log:
        for line in log:
            l = line.decode("utf-8") #this decodes from binary
            m = p.search(l) #implementing the regex
            if m:
                if m.group(1) in d:
                    d[m.group(1)] += 1 #adding to count
                else:
                    d[m.group(1)] = 1  #creating count
                
        print("***Top 25 Errors***")
        count = 0 
        for key, value in sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True):
            print('Count: %s\tPage: %s' % (value, key))
            count += 1
            if count == 25: #count up to 25 errors
                break


# Main function
def main():
    """
    Usage:
        python3 robert_lemmons_hw6.py <URL>
    """
    url = sys.argv[1]
    logFile(url)


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
