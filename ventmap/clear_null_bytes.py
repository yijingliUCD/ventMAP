"""
clear_null_bytes
~~~~~~~~~~~~~~~~

Self explanatory; clears null bytes from files
"""
import argparse
import os
from io import BufferedReader, open, StringIO


def clear_descriptor_null_bytes(descriptor):
    try:
        descriptor_text = unicode(descriptor.read().replace('\x00', ''))
    except NameError:  # python 3
        descriptor_text = str(descriptor.read()).replace('\x00', '')
    reader = StringIO(descriptor_text)
    reader.seek(0)
    return reader


def clear_null_bytes(input_file):
    with open(input_file, "rU") as old:
        return clear_descriptor_null_bytes(old)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="rel path to input file")
    args = parser.parse_args()
    stringio = clear_null_bytes(args.input_file)
    with open(new_file, "w") as new:
        new.write(stringio.read())


if __name__ == "__main__":
    main()
