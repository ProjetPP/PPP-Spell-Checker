#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='ppp_spell_checker',
    version='0.1',
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
    ],
    packages=[
        'ppp_spell_checker',
    ],
)

import sys
if 'install' in sys.argv:
    # From http://stackoverflow.com/questions/20415522/running-a-bash-script-from-python
    import subprocess
    cmd = "./dependencies.sh"
    if '--user' in sys.argv:
        cmd = '{0} {1}'.format(cmd,'--user')
    # no block, it start a sub process.
    p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # and you can block util the cmd execute finish
    p.wait()

