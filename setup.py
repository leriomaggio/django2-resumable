# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-resumable',
    version='0.1.0',
    author=u'valerio maggio',
    author_email='valeriomaggio@gmail.com',
    packages=['django_resumable'],
    include_package_data=True,
    package_data={
        'django_resumable': [
            'templates/django_resumable/file_input.html',
            'static/django_resumable/js/resumable.js',
        ]
    },
    url='https://github.com/leriomaggio/django-resumable',
    license='MIT licence',
    description='Django resumable uploads',
    long_description=open('README.md').read(),
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