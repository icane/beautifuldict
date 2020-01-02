# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='beautifuldict',
    version='0.1.0',
    author='Instituto Cántabro de Estadística',
    author_email='icane@cantabria.es',
    packages=find_packages(),
    url='https://gitlab.com/icane/beautifuldict.git',
    license='Apache License 2.0',
    description='Utils for managing configurations',
    long_description=open('README.rst').read(),
    test_suite='beautifuldict.test',
    keywords=['icane', 'configuration', 'utils'],
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries'
          ],
)
