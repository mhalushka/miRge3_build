============
Installation
============

miRge3.0-build is developed and tested on Linux environment. 


.. _dependencies:

Dependencies
------------

miRge3.0-build installation requires `Python 3.8 or newer`


Quick installation
------------------

The easiest way to install miRge3.0-build is to use ``pip3`` on the command line:

If you have root previlages, then install miRge3.0-build as follows::
    
    sudo python3.8 -m pip install miRge3.0-build

else::

    python3.8 -m pip install --user --upgrade miRge3.0-build

This will download the software from `PyPI (the Python packaging
index) <https://pypi.python.org/pypi/miRge3.0-build/>`_, and
install the miRge3.0-build binary into ``$HOME/.local/bin``. If an old version of
miRge3.0-build exists on your system, the ``--upgrade`` parameter is required in order
to install a newer version. You can then run the program like this::

    ~/.local/bin/miRge3.0-build --help

If you want to avoid typing the full path, add the directory
``$HOME/.local/bin`` to your ``$PATH`` environment variable.


Installation with conda
-----------------------

Yet to be implemented

Uninstalling
------------

To uninstall type::

    pip uninstall miRge3.0-build
