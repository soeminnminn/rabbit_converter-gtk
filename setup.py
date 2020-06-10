#!/usr/bin/python3
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
      long_description = fh.read()

setuptools.setup(
      name = "rabbitconverter",
      packages = setuptools.find_packages(),
      scripts=['rabbit_converter'],
      version = "1.0",
      description = "Myanmar unicode and Zawgyi-One font converter.",
      long_description = long_description,
      long_description_content_type = "text/markdown",
      author = "Soe Minn Minn",
      author_email = "soeminnminn@gmail.com",
      url = "http://soeminnminn.github.io",
      license = 'GPLv3',
      classifiers = [
         "Programming Language :: Python :: 3",
         "License :: GPLv3",
         "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      install_requires=["gobject", "PyGObject"],
      data_files = [ ("assets/fonts", ["assets/fonts/mmrtext.ttf", "assets/fonts/mmrtextb.ttf", "assets/fonts/zawgyi.ttf"]),
                     ("assets", ["assets/icon.png", "assets/icon.svg", "assets/style.css"]) ] 
      ) 
