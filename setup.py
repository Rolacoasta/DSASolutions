from setuptools import setup, find_packages

setup(
    name='StructySolutions',
    version='0.1.0',
    author='Max Madden',
    author_email='maxamadden@yahoo.com',
    packages=find_packages(),
    description='For anyone who wants to get a different perspective of solutions in the Structy course!',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().splitlines(),
)
