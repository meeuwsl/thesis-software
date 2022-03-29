from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='modular_steering',
    version=__version__,

    url='https://github.com/meeuwsl/thesis-software',
    author='Ludo Meeuws',
    author_email='ludo.meeuws@gmail.com',

    packages=find_packages()
)