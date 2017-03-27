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
    """
    with urlopen(url) as log:
        for line in log:
            print(line)


def sortstuff():
    """
    this should sort retrieved error file
    to get top 25 most common errors
    """
    pass


# Main function
def main():
    """
    Something something from a URL
    Usage:
        python3 robert_lemmons_hw6.py <URL>
    """
    url = sys.argv[1]
    logFile(url)


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
