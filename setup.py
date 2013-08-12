#!/usr/bin/env python
# http://docs.python.org/distutils/setupscript.html
# http://docs.python.org/2/distutils/examples.html

import sys
from setuptools import setup
import ast

name = 'blurg'
version = ''
with open('{}.py'.format(name), 'rU') as f:
    for node in (n for n in ast.parse(f.read()).body if isinstance(n, ast.Assign)):
        node_name = node.targets[0]
        if isinstance(node_name, ast.Name) and node_name.id.startswith('__version__'):
            version = node.value.s
            break

if not version:
    raise RuntimeError('Unable to find version number')

setup(
    name=name,
    version=version,
    description='images from one directory get blurred and put in another directory',
    author='Jay Marcyes',
    author_email='jay@marcyes.com',
    url='http://github.com/Jaymon/{}'.format(name),
    py_modules=[name],
    license="MIT",
    install_requires=['PIL >= 1.1.7'],
    classifiers=[ # https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: Public Domain',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Topic :: System :: Shells',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points = {
        'console_scripts': ['{} = {}:console'.format(name, name)]
    }
)
