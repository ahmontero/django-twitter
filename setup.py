#!/usr/bin/python
# -*- coding: utf-8 -*-

import twitter

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

setup(
    name='django-twitter',
    version=twitter.__version__,
    license=open('LICENSE').read(),
    author="Antonio Hinojo Montero",
    author_email="hello@ahmontero.com",
    url="http://github.com/ahmontero/django-twitter",
    description='An inobstrusive way to login with Twitter into your Django application.',
    keywords='twitter django login',
    long_description=open('README').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['oauth2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications',
        'Topic :: Internet'
    ]
)
