from setuptools import setup, find_packages
import unittest

setup(
    name='pyUnitTypes',
    version='0.0.1',
    description='python package to work with different physical units as types and pythons type annotations',
    packages=find_packages(),
    test_suite='setup.my_test_suite'
)



