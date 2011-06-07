#!/usr/bin/env python
from setuptools import setup,find_packages

METADATA = dict(
    name='django-cooki18n',
    version='0.1.0',
    author='Raymond Penners',
    author_email='raymond.penners@intenct.nl',
    description='related to Django tickets #12794, #15902',
    long_description=open('README.rst').read(),
    url='http://github.com/pennersr/django-cooki18n',
    keywords='django i18n cookie language',
    install_requires=['django'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**METADATA)
    
