from setuptools import find_packages, setup

setup(
    name='strictint',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typing',
    ],
    author='Thomas Ward',
    author_email='teward@thomas-ward.net',
    description="A library that adds a StrictInt class/datatype, which prohibits converting non-integers to integers.",
    long_description="This is a library which adds a new datatype called 'StrictInt' to the system. It "
                     "is designed to by-default disallow the conversion of numeric values which have non-integer parts "
                     "to the Integer type.",
    license='AGPLv3+',
    url='https://github.com/teward/strictint',
    download_url='https://pypi.python.org/pypi/strictint',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='int types strictint',
    platforms='any',
    test_suite='tests',
    python_requires='>=3.0'
)
