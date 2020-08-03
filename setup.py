#!/usr/vin/env python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Vadim Khitrin <me at vkhitrin.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import setuptools

setuptools.setup(
    name='virt-customize-ansible-modules',
    version='0.0.3',
    description='Ansible modules to perform basic libguestfs actions',
    author='Vadim Khitrin',
    author_email='me@vkhitrin.com',
    packages=[
        'ansible/modules/cloud/libguestfs',
        'ansible/module_utils/libguestfs'
    ],
    install_requires=[
        'ansible >= 2.4.0'
    ],
)
