from setuptools import setup, find_packages

from modular_steering import __version__




extra_dev = [
    'pytest>=4.6.11',
    'pytest-cov>=2',
]

setup(
    name='modular_steering',
    version=__version__,

    url='https://github.com/meeuwsl/thesis-software',
    author='Ludo Meeuws',
    author_email='ludo.meeuws@gmail.com',
    install_requires=[
    'numpy',
    ],

    extras_require = {
        'dev': extra_dev,
    },


    packages=find_packages()
)