from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    # package name in pypi
    name='rfc5424syslog',
    # extract version from module.
    version=__version__,
    description="A Logging Formatter for Python's logging module to properly handle Syslog RFC5424 messages",
    long_description="",
    classifiers=[],
    keywords='',
    author='Morgan Fainberg',
    author_email='',
    url='https://github.com/morganfainberg/python-rfc5424-logging-formatter',
    license='GPLv2',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
    ],
)
