# Ansible module examples

## Download repository
```
git clone 
cd examples-ansible-modules
```

## Filter Plugins

**What is a filter**
```
---
- name: Example Playbook for custom filter plugins
  hosts: localhost
  tasks:
    - name: Example of hello_world() filter plugin
      debug:
        msg: "{{ 'Hello' | hello_world() }}"
```

The `| hello_world()` part is a filter. 

The module:
- should be compatible with Python 2.6 and Python 3.5
- will be executed on the controller.
- should return always strings with to_text() function to avoid errors if a Jinja2 templates are rendered
- will exit the plugin with an error message with the `AnsibleFilterError()` function 

This exception should always be implemented:
```
try:
    cause_an_exception(with_undefined_variable)
except jinja2.exceptions.UndefinedError as e:
    raise AnsibleUndefinedVariable("Something happened, this was the original exception: %s" % to_native(e))
except Exception as e:
    raise AnsibleFilterError("Something happened, this was the original exception: %s" % to_native(e))
```

Example filter:
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common.text.converters import to_native

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
```

Links:
- Developing filter plugins: https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#filter-plugins
- Developing plugins: https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html

## Modules

What is a module?
```
---
- name: Example Playbook for custom filter plugins
  hosts: localhost

  tasks:
    - name: Fail test_template module
      test_template:
        name: 'fail me'
      ignore_errors: true
```

A module is accessed by tasks in Playbooks.

A module
- should be compatible with Python 2.6 and Python 3.5
- can be executed by a task in a Playbook
- will be executed on the remote node, not the controller node
- has different states that can be returned. The states are `changed`, `ok`, `fatal`.
- will return a `changed` state set `result['changed'] = True` and it has to be exited with the `module.exit_json()` function
- will return `ok` and has to be exited with `module.exit_json()` function
- will fail the module exit `module.fail_json()`

Check __library/test_template.py__ to see how the code looks like.

## Links
- Ansible Module reference: https://docs.ansible.com/ansible/latest/reference_appendices/module_utils.html
- Check list for community ready modules: https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_checklist.html
- Developing modules: https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html
- Developing plugins: https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html
- Developing modules best practices / Conventions, tips, and pitfalls: https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_best_practices.html