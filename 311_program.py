# -*- coding: utf-8 -*-
"""
Joe Holleran
10/02/2019
311 Program
Python 2
"""
import json


with open('wprdc_json.txt', 'r') as fields:
    wprdc_json = json.load(fields)
    
for word in wprdc_json:
    print(word, end="")

    

