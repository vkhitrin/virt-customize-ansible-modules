#!/usr/vin/env python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Vadim Khitrin <me at vkhitrin.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from setuptools import setup

py_files = [
    "ansible/module_utils/virt_customize",
]
files = [
    "ansible/modules/virt_customize",
]

long_description = open('README.md', 'r').read()

setup(
    name='virt-customize-ansible-modules',
    version='0.1.0',
    description='Ansible Modules for performing libguestfs actions',
    long_description=long_description,
    author='Vadim Khitrin',
    author_email='me@vkhitrin.com',
    url='https://github.com/vkhitrin/virt-customize-ansible-modules',
    license='GPLv3',
    py_modules=py_files,
    packages=files,
    install_requires = [
        'ansible>=2.4.0',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
