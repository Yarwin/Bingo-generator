#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='bingo-generator',
    version='0.1.0',
    description='Simple bingo image generator made with pillow',
    url='https://github.com/Yarwin/Bingo-generator',
    author='Yavin',
    author_email='yavinlecretin@gmail.com',
    license='MIT',
    packages=['bingo_generator'],
    scripts=['bin/bingo.py'],
    install_requires=[
        'click',
        'pillow'
    ],
    zip_safe=False)
