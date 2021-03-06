"""
This is the journal module.
"""

import datetime, os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_fullpathname(name)
    if os.path.exists(filename):  # if .jrl exists,  read each line and append it new dictionary
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data  # if doesnt exists return empty list


def save(name, data):
    filename = get_fullpathname(name)
    print(".....saving to {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def get_fullpathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, data):
    data.append(text)
