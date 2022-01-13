__author__ = 'Sujit Mandal'
#Date : 07-09-2020
from setuptools import setup 

def readme():
    with open('README.md') as files:
        README = files.read()

    return(README)

setup(
    name = 'python-gmail',
    version = '0.0.8',
    description = 'Automatically Send Gmail with SMTP Server.',
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/sujitmandal/py-gmail',
    author = 'Sujit Mandal',
    author_email = 'mandals974@gmail.com',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages = ['gmail'],
    include_package_data = True,
)