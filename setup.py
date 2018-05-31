#!/usr/bin/env python

from setuptools import find_packages, setup

import ml
setup(
        name='ml',
        description='Machine Learning helpers',
        version=ml.__version__,
        author='Will Price',
        author_email='will.price94@gmail.com',
        url='http://github.com/willprice/libml',
        packages=find_packages(),
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.6',
        ],
)
