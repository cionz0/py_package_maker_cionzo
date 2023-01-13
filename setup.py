""" This module is a module

    :synopsis: A useful module indeed.
    :position: .setup
    :author: cionzo <cionzo@filotrack.com>
    :created on: 13/01/23
    :project: py_package_maker_cionzo
 """

from setuptools import setup, find_packages

setup(
    name='py_package_maker_cionzo',
    version='0.0.1',
    packages=find_packages(),
    scripts=['src/py_package_maker_cionzo/builder.py', 'src/py_package_maker_cionzo/packager.py'],
)