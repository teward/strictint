IMAP Lib Extension Module
-------------------------

Basic Information
~~~~~~~~~~~~~~~~~

|License|

Continuous Integration Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+---------------+
| CI Provider   | Status        |
+===============+===============+
| Travis CI     | |Travis-CI|   |
+---------------+---------------+
| CircleCI      | |CircleCI|    |
+---------------+---------------+

Description
-----------

This module provides an object class/type called ``StrictInt``. This
StrictInt object class is a subclass of the ``int`` object type, but
behaves with different functionality than the straight ``int`` class.

The ``StrictInt`` object type is an object which will refuse to coerce
non-integer values. This means that values which have a fractional or
non-integer or imaginary component to them will not be converted to an
``int`` and instead will raise a ``ValueError`` on cases where a value
cannot be converted into an ``int`` without losing the non-\ ``int``
parts of the value.

Compatibility
-------------

This module was written to be compatible in Python 3.5 and up. However,
it should be compatible with any version of Python 3 (3.0 through 3.x).

Installation / Usage
--------------------

Use PyPI
~~~~~~~~

This library is available from the PyPI repository.

Python 2:
^^^^^^^^^

Install from Source Code
~~~~~~~~~~~~~~~~~~~~~~~~

Dependencies
^^^^^^^^^^^^

First, install the dependencies from PyPI.

Python 2
''''''''

For system-wide installation:

::

    pip install --upgrade -r requirements.txt

For user-space installation:

::

    pip install --user --upgrade -r requirements.txt

Python 3
''''''''

For system-wide installation:

::

    pip3 install --upgrade -r requirements.txt

For user-space installation:

::

    pip3 install --user --upgrade -r requirements.txt

Installing / Importing in Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simply copy the ``imaplibext`` package folder into your working
directory for your Python script or program.

Usage
-----

Once installed in either method, you can import into your Python code as
a drop-in replacement for ``imaplib``'s ``IMAP4`` or ``IMAP4_SSL``
commands.

::

    # Use this to import as a module and call things with `imaplibext.OBJECTNAME`
    import imaplibext

    # or, use this, to call IMAP4 and IMAP4_SSL directly in your code, but get the UID functions instead.
    from imaplibext import IMAP4, IMAP4_SSL

Usage
-----

Usage is identical to ``imaplib``'s ``IMAP4`` and ``IMAP4_SSL`` classes
and corresponding function calls. There is no real difference in how to
reference functions or the classes in the IMAP4 or IMAP4\_SSL functions
here compared to the parent ``imaplib`` functions.

FAQ
---

Where can I report issues or make Feature Requests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Issues and feature requests can be reported on the `Github
Repository <https://github.com/teward/imaplibext>`__

.. |License| image:: https://travis-ci.org/teward/strictint.svg?branch=master
   :target: http://www.gnu.org/licenses/agpl-3.0
.. |PyPI| image:: http://img.shields.io/pypi/v/strictint.svg
   :target: https://pypi.python.org/pypi/strictint
.. |Travis-CI| image:: https://travis-ci.org/teward/strictint.svg?branch=master
   :target: https://travis-ci.org/teward/strictint
.. |CircleCI| image:: https://circleci.com/gh/teward/strictint.svg?style=shield
   :target: https://circleci.com/gh/teward/strictint
