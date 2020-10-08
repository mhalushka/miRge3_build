============
Installation
============

miRge3.0-build is developed and tested on Linux environment. 


.. _dependencies:

Dependencies
------------

* miRge3.0-build installation requires ``python 3.8 or newer``
* `Bowtie v1.2.3 <https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.2.3>`_ - please pick one based on your OS. \
    - After downloading Bowtie, extract it (``unzip bowtie-1.2.3-linux-x86_64.zip``), \
    - Change directory to bowtie ``cd bowtie-1.2.3-linux-x86_64`` and type ``pwd`` to get full path of the directory (pwd: present working directory). \
    - Add that path to the environment PATH: ``export PATH=$PATH:"pwd <path> "``.  
        + Example: ``export PATH=$PATH:"/home/user/software/bowtie-1.2.3-linux-x86_64"`` \
* Requires scipy for enabling novel miRNA analysis ``python3.8 -m pip install --user scipy==1.4.1``
* Requires scikit-learn for enabling novel miRNA analysis ``python3.8 -m pip install scikit-learn==0.23.1``
* Requires biopython for parsing all input FASTA files ``python3.8 -m pip install biopython==1.77``


Quick installation
------------------

The easiest way to install miRge3.0-build is to use ``pip3`` on the command line:

If you have root previlages, then install miRge3.0-build as follows::
    
    sudo python3.8 -m pip install miRge3.0-build

if you have only user previlages::

    python3.8 -m pip install --user miRge3.0-build

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
