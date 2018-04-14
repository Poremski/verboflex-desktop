=================
Verboflex Desktop
=================

|logo| **A verb conjugation tool**

.. |logo| image:: icons/verboflex-64x64.png

|license| |pypi| |travis| |appveyor| |codecov|

.. |license| image:: https://img.shields.io/badge/license-GPL-blue.svg
   :target: https://github.com/Poremski/verboflex-desktop/blob/master/LICENSE.rst
.. |pypi| image:: https://img.shields.io/pypi/v/verboflex-desktop.svg?style=flat
   :target: https://pypi.python.org/pypi/verboflex-desktop/
.. |travis| image:: https://travis-ci.org/Poremski/verboflex-desktop.svg?branch=master
   :target: https://travis-ci.org/Poremski/verboflex-desktop
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/4iynnjnog74ih2of/branch/master?svg=true
   :target: https://ci.appveyor.com/project/Poremski/verboflex-desktop
.. |codecov| image:: https://codecov.io/gh/Poremski/verboflex-desktop/coverage.svg?branch=master
   :target: https://codecov.io/gh/Poremski/verboflex-desktop?branch=master

`website <https://verboflex.com>`_ | `FAQ <doc/faq.rst>`_ | `contributing <CONTRIBUTING.rst>`_ | `releases <https://github.com/Poremski/verboflex-desktop/releases>`_ | `installing <doc/install.rst>`_

About the project
=================
Verboflex Desktop is a cross-platform desktop application written in Python 3
and it’s based on PyQt5. This application offers to the user an interface
for the `Verboflex API`_, which lets users conjugate verbs in tens of
languages.

Supported languages
-------------------

Below, you’ll find the table of content showing the supported languages on
which one can perform verb conjugation in Verboflex Desktop.

+-------------+-----------+-----------------+
| Language    | Code      | Number of verbs |
|             | ISO 639-1 |                 |
+=============+===========+=================+
| Afrikaans   | af        | n/a             |
+-------------+-----------+-----------------+
| Danish      | da        | n/a             |
+-------------+-----------+-----------------+
| Dutch       | nl        | n/a             |
+-------------+-----------+-----------------+
| English     | en        | n/a             |
+-------------+-----------+-----------------+
| Esperanto   | eo        | n/a             |
+-------------+-----------+-----------------+
| Finnish     | fi        | n/a             |
+-------------+-----------+-----------------+
| French      | fr        | n/a             |
+-------------+-----------+-----------------+
| German      | de        | n/a             |
+-------------+-----------+-----------------+
| Greek       | el        | n/a             |
+-------------+-----------+-----------------+
| Ido         | io        | n/a             |
+-------------+-----------+-----------------+
| Interlingua | ia        | n/a             |
+-------------+-----------+-----------------+
| Italian     | it        | n/a             |
+-------------+-----------+-----------------+
| Latin       | la        | n/a             |
+-------------+-----------+-----------------+
| Norwegian   | no        | n/a             |
+-------------+-----------+-----------------+
| Polish      | pl        | n/a             |
+-------------+-----------+-----------------+
| Portuguese  | pt        | n/a             |
+-------------+-----------+-----------------+
| Romanian    | ro        | n/a             |
+-------------+-----------+-----------------+
| Russian     | ru        | n/a             |
+-------------+-----------+-----------------+
| Spanish     | es        | n/a             |
+-------------+-----------+-----------------+
| Swedish     | sv        | n/a             |
+-------------+-----------+-----------------+
| Turkish     | tr        | n/a             |
+-------------+-----------+-----------------+

Supported display languages
---------------------------

Below, you will find the table of content showing the languages which are
supported for the display language for the user interface in Verboflex Desktop.

+-------------+-----------+---------------------------+
| Language    |   Code    | Internationalization path |
|             | ISO 639-1 |                           |
+=============+===========+===========================+
| English     | en        | ./verboflex/locale/en/*   |
+-------------+-----------+---------------------------+
| Spanish     | es        | ./verboflex/locale/es/*   |
+-------------+-----------+---------------------------+
| Swedish     | sv        | ./verboflex/locale/sv/*   |
+-------------+-----------+---------------------------+

Requirements
============

The final requirements will be announced when the project’s release life cycle
enters beta stage. Until then, you can find the current requirements in the
requirements.txt_ file. Please keep in mind that the requirements listed in
the text file can change unexpectedly during the project’s alpha stage.

Changelog
=========

All notable changes to this project are documented in the CHANGELOG.srt_ file.

License
=======

This project uses the OSI-approved Open Source license and it is free
software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, either
version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but **without
any warranty**; without even the implied warranty of **merchantability** or
**fitness for a particular purpose**. See the `LICENSE.srt`_ file for more
details.

.. _Verboflex API: https://github.com/Poremski/verboflex-API
.. _requirements.txt: requirements.txt
.. _CHANGELOG.srt: CHANGELOG.rst
.. _LICENSE.srt: LICENSE.rst
