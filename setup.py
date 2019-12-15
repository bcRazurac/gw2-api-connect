# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.5.7'
REPOSITORY = 'https://github.com/razurac/gw2-connector'

with open('README.rst', 'r') as f:
    README = f.read()


setup(
    name='GuildWars2-Connector',
    version=__version__,
    description='Library that interfaces with the Guild Wars 2 API that supports v1 and v2',
    long_description=README,
    author='Razurac',
    author_email='azelch@r4zur4c-srv.eu',
    url=REPOSITORY,
    packages=find_packages(exclude=['test', 'res']),
    install_requires=[
        'requests',
    ],
    license='MIT',
    keywords=['guildwars 2', 'api', 'gw2']
)
