import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="onagame2015",
    version="0.1",
    author="Pedro Guridi",
    author_email="pedro.guridi@gmail.com",
    description=("A turn based strategy game for Python bots."),
    license="MIT",
    keywords="game engine coding challenge",
    url="https://github.com/Onapsis/onagame2015",
    packages=['onagame2015'],
    provides=['onagame2015'],
    install_requires=[
        "turnboxed",
    ],
    long_description=read('README'),
    classifiers=[
        'Intended Audience :: Developers',
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)