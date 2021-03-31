"""Package setup."""

from setuptools import find_packages, setup

setup(
    name='beautifuldict',
    version='0.1.3',
    author='Servicio de Informática y Banco de Datos',
    author_email='sibd@cantabria.es',
    packages=find_packages(),
    url='https://github.com/icane/beautifuldict.git',
    license='Apache License 2.0',
    description='Utils for managing configurations',
    long_description=open('README.rst').read(),
    test_suite='beautifuldict.test',
    keywords=['configuration', 'utils'],
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
          ]
)
