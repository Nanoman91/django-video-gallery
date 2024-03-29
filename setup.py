# coding: utf-8

import os

from setuptools import setup

# Avoid polluting the .tar.gz with ._* files under Mac OS X
os.putenv('COPYFILE_DISABLE', 'true')

# Prevent distutils from complaining that a standard file wasn't found
README = os.path.join(os.path.dirname(__file__), 'README')
if not os.path.exists(README):
    os.symlink(README + '.rst', README)

description = 'A Simple Photo gallery with granular access control, Based on MyKs-Gallery'

with open(README) as f:
    long_description = '\n\n'.join(f.read().split('\n\n')[2:6])

setup(
    name='django-gallery',
    version='0.1',
    author='Jeremy Gaul',
    author_email='django-gallery@jeremygaul.com',
    url='https://github.com/jeremygaul/django-gallery',
    description=description,
    long_description=long_description,
    download_url='http://pypi.python.org/pypi/django-gallery',
    packages=[
        'gallery',
        'gallery.management',
        'gallery.management.commands',
    ],
    package_data={
        'gallery': [
            'locale/*/LC_MESSAGES/*',
            'static/css/gallery.css',
            'templates/admin/gallery/*.html',
            'templates/gallery/*.html',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    platforms='all',
    license='BSD'
)
