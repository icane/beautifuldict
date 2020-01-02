*************
BeautifulDict
*************

:Info: Python package to manage configuration dictionaries.
:Author: Servicio de Informática y Banco de Datos <sibd@cantabria.es>


Features
========

* Simple wrapper around python dictionaries
* Access to nested keys with dot notation: ``config.deeply.nested.key`` or as dictionary keys: ``config['deeply']['nested']['key']``
* Allows add dictionaries, remove keys or modify values by overriding dictionary methods  


Installation
============

.. code:: bash

   pip install beautifuldict


* **Package**: https://pypi.org/project/beautifuldict/
* **Source**: https://github.com/icane/beautifuldict


Quick Example
=============

A Baseconfig object stores the configuration parameters as a parameter tree. It gives access to parameters in two ways: as dictionary keys or as attributes of the object.

.. code-block:: python

   >>> from beautifuldict.baseconfig import Baseconfig

   >>> CONFIG_DICT = {
   >>>      'example1': 'hello world',
   >>>      'example2': {
   >>>          'key1': 1,
   >>>          'key2': 2}
   >>>      }
   >>> config = Baseconfig(CONFIG_DICT)
   >>> config.example1     # returns 'hello world'
   >>> config['example1']  # returns 'hello world'
   >>> config.example2.key1  # returns 1
   >>> config['example2']['key1']  # returns 1

