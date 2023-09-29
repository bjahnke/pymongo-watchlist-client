from setuptools import setup

setup(
    name='pymongo-watchlist-client',
    version='0.0.0.4',
    packages=['src/watchlist'],
    url='',
    license='',
    author='bjahnke',
    author_email='bjahnke71@gmail.com',
    description='client library for connecting to watchlist dbs',
    install_requires=[
        'requests',
    ]
)
