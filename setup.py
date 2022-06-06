#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

VERSION="0.1.9"

setup(
    name="H_m3u8DL",
    version=VERSION,
    description='m3u8视频解析，下载，解密，合并的python程序，支持全平台',
    long_description=long_description,
    author='hecoter',
    author_email='hecoter12138@gmail.com',
    maintainer='hecoter',
    maintainer_email='hecoter12138@gmail.com',
    license='MulanPSL2',
    packages=["H_m3u8DL"],
   
    install_requires=[
        "m3u8","pycryptodome","tqdm","retry","tornado","rich","requests"
    ],
    platforms=["all"],
    url='https://github.com/hecoter/H_m3u8DL',
    include_package_data=True,
    package_data = {
        'H_m3u8DL': ['*.exe', '*/*.js','*/*.so'],
    },
    scripts=[],
    entry_points={
    'console_scripts': ['H_m3u8DL=H_m3u8DL.__init__:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
)