#!/bin/sh

## https://www.tecmint.com/package-pygobject-applications-as-deb-package/
## https://packaging.python.org/tutorials/packaging-projects/
## https://dzone.com/articles/executable-package-pip-install

python3 ./setup.py sdist bdist_wheel

## install
# python3 -m pip install dist/rabbitconverter-1.0-py3-none-any.whl