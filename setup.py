#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='ppp_spell_checker',
    version='0.2.3',
    description='A spell checker for the PPP. Use the Aspell API.',
    url='https://github.com/ProjetPP',
    author='Projet Pensées Profondes',
    author_email='ppp2014@listes.ens-lyon.fr',
    license='MIT',
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'ppp_datamodel>=0.5',
        'ppp_libmodule>=0.6',
        'aspell-python-py3',
    ],
    packages=[
        'ppp_spell_checker',
    ],
)
