""" Minerva Python Library
"""
import os
from setuptools import setup, find_packages
import versioneer

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

REQUIRES = [
    'marshmallow==3.0.0b11',
    'marshmallow-sqlalchemy',
    'mccabe',
    # http://initd.org/psycopg/docs/install.html#binary-install-from-pypi
    'psycopg2-binary',
    'py',
    'SQLAlchemy',
    'stringcase'
]

TEST_REQUIRES = [
    'pytest',
    'docker',
    'requests',
    'factory_boy'
]

VERSION = versioneer.get_version()
DESCRIPTION = 'minerva DB'
AUTHOR = 'D.P.W. Russell'
EMAIL = 'douglas_russell@hms.harvard.edu'
LICENSE = 'MIT'
HOMEPAGE = 'https://github.com/sorgerlab/minerva-db'

setup(
    name='minerva-db',
    version=VERSION,
    cmdclass=versioneer.get_cmdclass(),
    package_dir={'': 'src'},
    description=DESCRIPTION,
    long_description=README,
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=REQUIRES,
    setup_requires=['pytest-runner'],
    tests_require=TEST_REQUIRES,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    url=HOMEPAGE,
    download_url=f'{HOMEPAGE}/archive/v{VERSION}.tar.gz',
    keywords=['minerva', 'database', 'library', 'microscopy'],
    zip_safe=False
)
