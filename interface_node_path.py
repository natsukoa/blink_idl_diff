#!/usr/bin/env python

"""
The goal of this script is to integrate IDL file path under the directory to text file.
"""
import os
import sys


def get_idl_files(path):
    """Return file path
    
    Args:
      path: directory path
    Return:
      str, absolute IDL file path
    """
    file_type = '.idl'
    non_idl_set = (
        'InspectorInstrumentation.idl',
    )
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            if file_name.endswith(file_type) and file_name not in non_idl_set:
                yield os.path.join(dir_path, file_name)


def main(args):
    path = args[0]
    filename = args[1]
    f = open(filename, 'w')
    for filepath in get_idl_files(path):
        f.write(filepath + '\n')
    f.close()


if __name__ == '__main__':
    main(sys.argv[1:])
