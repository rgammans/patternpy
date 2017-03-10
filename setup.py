from setuptools import setup, find_packages
"""
A meta-library of reusable generators of python patterns.

PatternPy is a resusable library which save rewritting common patterns.

This libary is intended to be used to aid the DRY princicple by providing
functions which return generated structured for the common pythonic patterns.
"""

setup(
    name="PatternPy",
    version="0.1.0",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
