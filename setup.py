# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django2-resumable',
    version='0.1.1',
    author=u'Valerio Maggio',
    author_email='valeriomaggio@gmail.com',
    packages=['django2_resumable'],
    include_package_data=True,
    package_data={
        'django2_resumable': [
            'templates/django2_resumable/file_input.html',
            'static/django2_resumable/js/resumable.js',
        ]
    },
    url='https://github.com/leriomaggio/django2-resumable',
    license='MIT licence',
    description='Django 2.x resumable uploads',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'Django >= 2.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False,
)
