#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common.text.converters import to_text

def hello_world(greeting):
    greeting = greeting + ' world!'
    return to_text(greeting)

def second_power(number):
    number = number * number
    return to_text(number)

class FilterModule(object):
    def filters(self):
        return {
            'hello_world': hello_world,
            'second_power': second_power
        }


