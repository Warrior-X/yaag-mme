#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    history = changelog_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Cutewarriorlover",
    author_email='cutewarriorlover@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    description="Yet Another Adventure Game - Murder Mystery Edition is a text based adventure game where you play with other NPC adventurers. But whether they live or die, is up to you.",
    entry_points={
        'console_scripts': [
            'yaag_mme=yaag_mme.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='yaag_mme',
    name='yaag_mme',
    packages=find_packages(include=['yaag_mme', 'yaag_mme.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Cutewarriorlover/yaag-mme',
    version='0.0.1',
    zip_safe=False,
)
