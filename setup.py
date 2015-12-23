#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open('itypes.py').read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version()


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


setup(
    name='itypes',
    version=version,
    url='http://github.com/tomchristie/itypes',
    license='BSD',
    description='Simple immutable types for python.',
    author='Tom Christie',
    author_email='tom@tomchristie.com',
    packages=get_packages('coreapi'),
    package_data=get_package_data('coreapi'),
    install_requires=['requests', 'click', 'jinja2>=2.7'],
    entry_points="""
        [console_scripts]
        coreapi=coreapi.commandline:client
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)