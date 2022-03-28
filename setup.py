from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/meeuwsl/modular-steering',
    author='Ludo Meeuws',
    author_email='ludo.meeuws@gmail.com',

    packages=find_packages()
)