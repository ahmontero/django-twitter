#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from setuptools import setup
from setuptools import find_packages

__author__ = 'Antonio Hinojo Montero <hello@ahmontero.com>'
__version__ = '1.0'

setup(
	# Basic package information.
	name = 'django-twitter',
	version = __version__,
	packages = find_packages(),

	# Packaging options.
	include_package_data = True,

	# Package dependencies.
	install_requires = ['oauth2'],

	# Metadata for PyPI.
	author = 'Antonio Hinojo Montero',
	author_email = 'hello@ahmontero.com',
	license = 'MIT License',
	url = 'http://github.com/ahmontero/django-twitter/tree/master',
	keywords = 'twitter django login',
	description = 'An inobstrusive way to login into Twitter with Django.',
	long_description = open('README.markdown').read(),
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Communications',
		'Topic :: Internet'
	]
)
