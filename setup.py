# !/usr/bin/env python
# coding: utf-8

import sys

from setuptools import setup

from legendary import __version__ as legendary_version

if sys.version_info < (3, 9):
    sys.exit('python 3.9 or higher is required for legendary')

with open("README.md", "r") as fh:
    long_description_l = fh.readlines()
    del long_description_l[2:10]  # remove discord/twitter link and logo
    long_description = ''.join(long_description_l)

setup(
    name='legendary-gl',
    version=legendary_version,
    license='GPL-3',
    author='Ahanaf',
    author_email='ahanafrashid2020@outlook.com',
    packages=[
        'legendary',
        'legendary.api',
        'legendary.downloader',
        'legendary.downloader.mp',
        'legendary.lfs',
        'legendary.models',
        'legendary.utils',
    ],
    entry_points=dict(
        console_scripts=['legendary = legendary.cli:main']
    ),
    install_requires=[
        'requests<3.0',
        'setuptools',
        'wheel',
        'filelock'
    ],
    extras_require=dict(
        webview=['pywebview>=3.4'],
        webview_gtk=['pywebview>=3.4', 'PyGObject']
    ),
    url='https://github.com/AhanafRASHID/legendary_parameter_fix.git',
    description='Free and open-source replacement for the Epic Games Launcher application unstable but usable version',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.9',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment',
        'Development Status :: 4 - Beta',
    ]
)
