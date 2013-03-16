#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Copyright (c) 2010 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import setuptools
import sys

name = 'python-hubicclient'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name=name,
    version='0.1',
    description='Client for the HubiC cloud storage service',
    long_description=read('README.md'),
    url='https://github.com/Gu1-/python-hubicclient',
    license='Apache License (2.0)',
    author='Gu1',
    author_email='gu1@aeroxteam.fr',
    keywords="hubic swift cloud storage",
    install_requires=['python-swiftclient'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: OpenStack',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
    ],
    scripts=[
        'bin/hubic',
    ],
)
