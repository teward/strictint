## IMAP Lib Extension Module

### Basic Information

<table>
<tr><td align=center valign=center><a href="http://www.gnu.org/licenses/agpl-3.0" target="_blank"><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" title="AGPL 3.0" /></a></td></tr>
<tr><td align=center valign=center><a href="https://pypi.python.org/pypi/strictint" target="_blank"><img src="http://img.shields.io/pypi/v/strictint.svg" title="PyPI Version" /></a></td></tr>
</table>


### Continuous Integration Status

| CI Provider | Status                                                                                                                                                              |
|:-----------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Travis CI   | [![Travis-CI](https://travis-ci.org/teward/strictint.svg?branch=master)](https://travis-ci.org/teward/strictint)                                                  |
| CircleCI    | [![CircleCI](https://circleci.com/gh/teward/strictint.svg?style=shield)](https://circleci.com/gh/teward/strictint)                                                |


## Description

This module provides an object class/type called `StrictInt`.  This StrictInt object class is a subclass of the `int` 
object type, but behaves with different functionality than the straight `int` class.

The `StrictInt` object type is an object which will refuse to coerce non-integer values.  This means that values which 
have a fractional or non-integer or imaginary component to them will not be converted to an `int` and instead will 
raise a `ValueError` on cases where a value cannot be converted into an `int` without losing the non-`int` parts of the 
value. 


## Compatibility

This module was written to be compatible in Python 3.5 and up.  However, it should be compatible with any version of 
Python 3 (3.0 through 3.x).


## Installation / Usage

### Use PyPI

This library is available from the PyPI repository.

### Install from Source Code (Python 3)

#### Dependencies

First, install the dependencies from PyPI.

For system-wide installation:

    pip3 install --upgrade -r requirements.txt

For user-space installation:

    pip3 install --user --upgrade -r requirements.txt

### Installing / Importing in Code

Simply copy the `imaplibext` package folder into your working directory for your Python script or program.

## Usage

Once installed in either method, you can import into your Python code as a drop-in replacement for `imaplib`'s 
`IMAP4` or `IMAP4_SSL` commands.

    # Use this to import as a module and call things with `imaplibext.OBJECTNAME`
    import imaplibext
    
    # or, use this, to call IMAP4 and IMAP4_SSL directly in your code, but get the UID functions instead.
    from imaplibext import IMAP4, IMAP4_SSL
    
## Usage

Usage is identical to `imaplib`'s `IMAP4` and `IMAP4_SSL` classes and corresponding function calls. There is no real
difference in how to reference functions or the classes in the IMAP4 or IMAP4_SSL functions here compared to the parent
`imaplib` functions.


## FAQ

### Where can I report issues or make Feature Requests?

Issues and feature requests can be reported on the [Github Repository](https://github.com/teward/strictint)
