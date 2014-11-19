#!/bin/sh

cd ..
if [ -d aspell-python ] ; then
    cd aspell-python
    git pull
else
    git clone git@github.com:WojciechMula/aspell-python.git
    cd aspell-python
fi
python3 setup.py install --user
