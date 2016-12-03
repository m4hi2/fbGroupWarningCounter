#!python3
"""
# This is just another lazy project
# The goal of this project is to keep a track of warned users in a Facebook Group
# Usage: Copy profile link> 'Yes' | 'No' > Sync!
"""

import re
import pyperclip

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
            data_entry("file.txt", pr_data)
        else:
            continue
