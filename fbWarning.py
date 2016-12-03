#!python3
"""
# This is just another lazy project
# The goal of this project is to keep a track of warned users in a Facebook Group
# Usage: ./fbWarning.py [filename] -- To log profile links.
        ./fbWarning.py count [filename] -- To count how many times a person is warned from the log file.

        PS: I'll be using this for Linux Bangladesh Group for a while and find out if it's of any use
            or just a piece of garbage.
"""

import re
import pyperclip
import sys
import pprint

pattern = re.compile(r"(http|https):\/\/?(?:web.)?facebook.com\/.+\?+(fref)+=(nf|ufi)")

pr_data = str()


def data_entry(filename, data):
    """
    This function will add the functionality to add the data to a file.
    """
    try:
        with open(filename, 'a') as file:
            file.write(data)
            file.write('\n')
    except IOError:
        print("Please input a correct file name. :) ")


def count(filename):
    counter = {}
    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                counter.setdefault(line, 0)
                counter[line] = counter[line] + 1
    except IOError as error:
        print("Your file is not found.\nError:{}".format(str(error)))
    return counter


if sys.argv[1] == 'count' and len(sys.argv) == 3:
    number = count(sys.argv[2])
    pprint.pprint(number)

elif len(sys.argv) == 2:

    while True:
        raw_data = pyperclip.paste()
        if raw_data == pr_data:
            continue
        if raw_data == '':
            continue
        else:
            match = pattern.search(raw_data)
            if match:
                pr_data = match.group()
                print("Unique ID found, Adding to file.")
                data_entry(sys.argv[1], pr_data)
            else:
                continue
else:
    print("Please follow the manual.")
