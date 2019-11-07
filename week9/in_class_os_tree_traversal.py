# -*- coding: utf-8 -*-
"""
Joe Holleran
11/06/2019
Python 2
In-Class Tree Traversal
"""
import os
import re

def main():

    for loc, dirs, files in os.walk('.'):
        interrogateFiles(loc, files)

def interrogateFiles(dirname, fileList):
    regexp = re.compile('(\.\w+)$')
    for f in fileList:
        fn = dirname + str(os.sep) + f
        print('File Size: ', end="")
        print(fn)
        if os.path.isfile(fn):
            print(os.path.getsize(fn), 'B')
            match = re.search(regexp, fn)
            if match:
                print('Extension: ', match.group(0))

        
# Code if directory is a zip file
# from zipfile import ZipFile
# with ZipFile('zipdirectoryname', 'r') as zipObj:
#        zipObj.extractall()


# Utility function for exploring features of a list of files
# discovered from our os.walk method
# def interrogateFiles(dirname, fileList):
#       for f in fileList:
#           fn = dirname + str(os.sep) + f
#           print('File Size: ', end="")
#           print(fn)
            
if __name__=='__main__':
    main()
