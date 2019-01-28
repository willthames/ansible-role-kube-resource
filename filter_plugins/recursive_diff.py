# Copyright (c) 2019 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}


#from ansible.module_utils.common.dict_transformations import recursive_diff

def recursive_diff(dict1, dict2):
    left = dict((k, v) for (k, v) in dict1.items() if k not in dict2)
    right = dict((k, v) for (k, v) in dict2.items() if k not in dict1)
    for k in (set(dict1.keys()) & set(dict2.keys())):
        if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            result = recursive_diff(dict1[k], dict2[k])
            if result:
                left[k] = result[0]
                right[k] = result[1]
        elif dict1[k] != dict2[k]:
            left[k] = dict1[k]
            right[k] = dict2[k]
    if left or right:
        return left, right
    else:
        return None


# ---- Ansible filters ----
class FilterModule(object):

    def filters(self):
        return {
            'recursive_diff': recursive_diff
        }

