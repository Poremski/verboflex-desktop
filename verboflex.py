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
Simple launcher for Verboflex Desktop.
"""

import sys
import verboflex.verboflex

if __name__ == '__main__':
    sys.exit(verboflex.verboflex.main())
