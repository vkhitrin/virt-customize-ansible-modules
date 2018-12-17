#!/usr/vin/env python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Vadim Khitrin <me at vkhitrin.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: virt_customize_packages
short_description: Performs package installation on guest disk images
version_added: "2.5.11"
description:
    - Manipulates packages on guest disk image using libguestfs
options:
    image:
        required: True
        description: image path on filesystem.
    name:
        required: False
        description: list of packages to manipulate
    state:
        required: True
        description: action to be performed
        choices:
          - present
          - absent
    list:
        required: False
        description: string to match when querying installed packages, to display all use '*'
    automount:
        required: False
        description: Whether to perform auto mount of mountpoints inside guest disk image (REQUIRED for this module)
        default: True
    network:
        required: False
        description: Whether to enable network for appliance
        default: True

requirements:
    - "guestfs"
    - "python >= 2.7.5"
author: Vadim Khitrin (@vkhitrin)

"""

EXAMPLES = """
---
- name: Installs a single package
  virt_customize_packages:
    image: /tmp/rhel7-5.qcow2
    name: vim
    state: present

- name: Installs several packages
  virt_customize_packages:
    image: /tmp/rhel7-5.qcow2
    name:
      - vim
      - nc
      - telnet
    state: present

- name: Uninstalls a single package
  virt_customize_packages:
    image: /tmp/rhel7-5.qcow2
    name: vim
    state: absent

- name: Uninstalls several package
  virt_customize_packages:
    image: /tmp/rhel7-5.qcow2
    name:
      - vim
      - nc
      - telnet
    state: absent

- name: List all packages containing string 'yum'
  virt_customize_packages:
    image: /tmp/rhel7-5.qcow2
    list: yum

- name: List all packages
  virt_customize_packages:
    image: /tmp/rhel7-5.qcow2
    list: '*'
"""

RETURN = """
- msg:
    type: string
    when: failed
    description: contains the error message (may include python exceptions)
    example: "Unable to locate package testpackage123"

- results:
    type: array
    when: invocation
    description: contains the module execution results
    example: [
        "2:vim-enhanced-7.4.160-4.el7.x86_64 is present"
    ]
"""

from ansible.module_utils.virt_customize import guest
from ansible.module_utils.basic import AnsibleModule

import re

PACKAGE_MANAGERS = {
    "dnf": {"present": "dnf -y install", "absent": "dnf -y remove"},
    "yum": {"present": "yum -y install", "absent": "yum -y remove"},
    "apt": {"present": "apt-get -y install", "absent": "apt-get -y remove"}
}


def packages(guest, module):
    result = ""
    results = {}
    results['msg'] = ""
    results['changed'] = False
    results['failed'] = False
    results['results'] = []
    response = set()
    err = False

    if module.params['automount']:
        if module.params['name']:
            packages_string = ""
            for package in module.params['name']:
                package = package.strip()
                packages_string = "{0} {1}".format(packages_string, package).lstrip()
            for mount in guest.mounts():
                package_manager = guest.inspect_get_package_management(mount)
                if package_manager != "unknown" and package_manager:
                    break

            if package_manager in PACKAGE_MANAGERS.keys():
                try:
                    result = guest.sh("{0} {1}".format(PACKAGE_MANAGERS[package_manager][module.params['state']], packages_string))
                    if package_manager in ['yum', 'dnf'] and not err:
                        for line in result.split('\n'):
                            for package in module.params['name']:
                                package = package.strip()
                                if "Verifying" in line:
                                    results['changed'] = True
                                    response.add(re.findall('([^\s]+)', line)[2] + " is {0}".format(module.params['state']))
                                    dude = re.findall('([^\s]+)', line)
                                if 'already installed' in line:
                                    response.add(line.replace("Package ",''))
                                if re.search(r'No package .* available.', line):
                                    results['failed'] = True
                                    results['msg'] = line
                                    response.add(line)
                                if "No Packages marked for removal" in line:
                                    response.add(line)
                    elif package_manager == 'apt':
                        for line in result.split('\n'):
                            for package in module.params['name']:
                                if package.strip() in line:
                                    if "Unpacking" in line or "Removing" in line:
                                        results['changed'] = True
                                        response.add(re.sub(r'Unpacking|Removing', '', line).replace(' ...\r', '') + " is {0}".format(module.params['state']))
                                    if "already" in line or "not installed" in line:
                                        response.add(line)
                    results['results'] = list(sorted(response))
                except Exception as e:
                    err = True
                    results['failed'] = True
                    results['msg'] = str(e)
                    if response:
                        results['results'] = list(sorted(response))
                    else:
                        results['results'] = results['msg']

            else:
                err = True
                results['msg'] = results['results'] = "Package manager '{0}' is not supported".format(package_manager)

        if module.params['list']:
            app_regex = module.params['list']
            if app_regex != "*":
                app_query = True
            else:
                app_query = False
            packages_list = []
            for mount in guest.mounts():
                apps = guest.inspect_list_applications2(mount)
                if apps:
                    for app in apps:
                        packages_list.append("{0}-{1}-{2}.{3}".format(app['app2_name'], app['app2_version'], app['app2_release'], app['app2_arch']))
                        if app_query:
                            if app_regex not in app['app2_name']:
                                del packages_list[-1]
                    break
            if packages_list:
                results['results'] = packages_list
            else:
                err = True
                results['msg'] = results['results'] = "Packages containing '{0}' not found".format(app_regex)
    else:
        err = True
        results['results'] = "automount is false, can't proceed with this module"
    return results, err


def main():

    mutual_exclusive_args = [['name', 'list'], ['list', 'state']]
    required_togheter_args = [['name', 'state']]
    module = AnsibleModule(
        argument_spec=dict(
            image=dict(required=True, type='str'),
            automount=dict(required=False, type='bool', default=True),
            network=dict(required=False, type='bool', default=True),
            name=dict(required=False, type='list'),
            state=dict(required=True, choices=['present', 'absent']),
            list=dict(required=False, type='str')
        ),
        mutually_exclusive=mutual_exclusive_args,
        required_together=required_togheter_args,
        supports_check_mode=True
    )
    g = guest(module)
    instance = g.bootstrap()
    results, err = packages(instance, module)
    g.close()
    if err:
        module.fail_json(**results)
    module.exit_json(**results)


if __name__ == '__main__':
    main()
