import os
from setuptools import setup, find_packages


README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.markdown')
description = 'django-goodfields makes creating good form fields easy.'
long_description = os.path.exists(README_PATH) and open(README_PATH).read() or description

setup(
    name='django-goodfields',
    version='0.0.1',
    description=description,
    long_description=long_description,
    author='Steve Losh',
    author_email='steve@stevelosh.com',
    url='http://bitbucket.org/dwaiter/django-goodfields/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
    ],
)
