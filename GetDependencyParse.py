""" GetDependencyParse.py - Contains functions to deal with output of Stanford's dependency parser
"""

import re
from parse import parse

def dependency_parse(sentence):
    """ Accepts a sentence and returns its dependency parse as a list-of-lists
    """

    # sentence = raw_input("Enter a sentence: ")

    parser_folder = "parser"    # Change if parser is in some other directory
    parse_output = parse(sentence, parser_folder)
    dep_parse = parse_output[1].split("\n")

    print "---"
    dependency_parse=[]
    for i in dep_parse:
        if len(i.strip()) > 0 and i.strip()[0] != "(":
            line=i.strip()
            dependency_parse.append(filter(lambda x:x.isalpha(),re.findall(r"[\w']+", line)))

    return dependency_parse

if __name__ == "__main__":
    sentence = raw_input("Enter a sentence: ")

    print dependency_parse(sentence)
