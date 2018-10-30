#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    'test': [
        "pytest==3.3.2",
        "pytest-xdist",
        "tox>=2.9.1,<3",
    ],
    'lint': [
        "flake8==3.4.1",
        "isort>=4.2.15,<5",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +
    extras_require['test'] +
    extras_require['lint'] +
    extras_require['doc']
)

setup(
    name='devcon-iv-ethpm',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.1.0-alpha.0',
    description="""devcon-iv-ethpm: Starter repo for the devcon iv ethpm workshop.""",
    long_description_markdown_filename='README.md',
    author='Nick Gheorghita',
    author_email='nickg@ethereum.org',
    url='https://github.com/ethereum/devcon-iv-ethpm',
    include_package_data=True,
    install_requires=[
        "eth-utils>=1,<2",
        "ethpm>=0.1.4a1,<1",
        "pytest-ethereum>=0.1.3a1,<1",
    ],
    setup_requires=['setuptools-markdown'],
    python_requires='>=3.6, <4',
    extras_require=extras_require,
    py_modules=['devcon-iv-ethpm'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
