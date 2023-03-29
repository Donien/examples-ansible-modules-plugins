#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common.text.converters import to_text

import datetime
import time

def to_unixtime(time_string, format="%Y-%m-%d %H:%M:%S"):
    raise ValueError("Dingo bingo bongo ding")
    time_object = datetime.datetime.strptime(time_string, format)
    time_object = time.mktime(time_object.timetuple())
    return to_text(time_object)

def second_power(number):
    number = number * number
    return to_text(number)

def mocking_meme(st):
    if type(st) != str:
        raise TypeError(f"Value '{st}' not of type string...")
    st_arr = []
    mock_count = 0
    for letter in st:
        if mock_count%2 == 0:
            st_arr.append(letter.lower())
        else:
            st_arr.append(letter.upper())
        if not letter.isalpha():
            mock_count = 0
        else:
            mock_count += 1
            
    st = "".join(st_arr)
    return to_text(st)

class FilterModule(object):
    def filters(self):
        return {
            'to_unixtime': to_unixtime,
            'mocking': mocking_meme,
            'second_power': second_power
        }
