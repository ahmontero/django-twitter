#!/usr/bin/python
# -*- coding: utf-8 -*-

import twitter

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-twitter',
    version=twitter.__version__,
    description='An inobstrusive way to login with Twitter into your Django application.',
    long_description=open('README.rst').read() + '\n\n' +
                     open('CHANGES.txt').read(),
    author="Antonio Hinojo",
    author_email="hello@ahmontero.com",
    url="http://github.com/ahmontero/django-twitter",
    packages=["twitter"],
    package_data={'': ['LICENSE.txt']},
    package_dir={'twitter': 'twitter'},
    include_package_data=True,
    install_requires=['oauth2'],
    license=open('LICENSE.txt').read(),
    zip_safe=False,
    keywords='twitter django login',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications',
        'Topic :: Internet'
    ]
)
