from distutils.core import setup


with open('VERSION', 'r') as f:
    version = f.read()

with open('README.md','r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().split('\n')

setup(
    name='SPL',
    version=version,
    author='Franciscp J. Piedrahita',
    author_email='fpiedrah93@gmail.com',

    packages=['spl', 'tests'],
    url='https://github.com/SPLA/SPL-Solver',

    license='MIT',
    description='Simple library to write decision trees',
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=install_requires,
)
