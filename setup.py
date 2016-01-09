# -*- coding: utf-8 -*-
from setuptools import setup
setup(
    name='gsdata',
    version='1.1.0',
    description='gsdata unoffical python sdk',
    url='https://github.com/superalsrk/gsdata-python-sdk',
    author='SRK.Lyu',
    author_email='superalsrk@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='gsdata unoffical python sdk',
    license='MIT',

    packages=[
        'gsdata'
    ],

    install_requires=['requests>=2.5.0'],
    test_suite='gsdata_tests'
)
