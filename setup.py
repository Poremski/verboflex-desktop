#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Verboflex Desktop
#
# A cross-platform desktop application developed in Python which supports verb
# conjugation in tens of languages.
#
# Copyright (C) 2018 Javier Poremski
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Setuptools installer script for Verboflex Desktop.
"""

import re
import ast
import os
import os.path
from scripts import setupcommon as common
import setuptools

try:
    BASEDIR = os.path.dirname(os.path.realpath(__file__))
except NameError:
    BASEDIR = None


def read_file(name):
    """
    Get the string contained in the file named name.
    """
    with common.open_file(name, 'r', encoding='utf-8') as f:
        return f.read()


def _get_constant(name):
    """
    Read a __magic__ constant from verboflex/__init__.py.
    We don’t import verboflex here because it can go wrong for multiple
    reasons. Instead we use re/ast to get the value directly from the source
    file.
    :param name: The name of the argument to get.
    :return: The vlaue fo the argument.
    """
    field_re = re.compile(r'__{}__\s+=\s+(.*)'.format(re.escape(name)))
    path = os.path.join(BASEDIR, 'verboflex', '__init__.py')
    line = field_re.search(read_file(path)).group(1)
    value = ast.literal_eval(line)
    return value


try:
    common.write_git_file()
    setuptools.setup(
        packages=setuptools.find_packages(exclude=['scripts', 'scripts.*']),
        include_package_data=True,
        entry_points={'gui_scripts':
                      ['verboflex = verboflex.verboflex:main']},
        zip_safe=True,
        install_requires=['pypeg2'],
        python_requires='>=3.5',
        name='verboflex-desktop',
        version='.'.join(str(e) for e in _get_constant('version_info')),
        description=_get_constant('description'),
        long_description=read_file('README.rst'),
        url='https://verboflex.com/',
        author=_get_constant('author'),
        author_email=_get_constant('email'),
        license=_get_constant('license'),
        classifiers=[
            'Development Status :: 1 - Alpha',
            'Environment :: X11 Applications :: Qt',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 or later'
                ' (GPLv3+)',
            'Natural Language :: English',
            'Natural Language :: Spanish',
            'Natural Language :: Swedish',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Operating System :: POSIX :: BSD',
            'Operating System :: MacOS',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Intended Audience :: Education'
            'Topic :: Education',
        ],
        keywords='verb conjugation tool language pyqt qt',
    )
finally:
    if BASEDIR is not None:
        path = os.path.join(BASEDIR, 'verboflex-desktop', 'git-commit-id')
        if os.path.exists(path):
            os.remove(path)

