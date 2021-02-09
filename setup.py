from setuptools import setup, find_packages, Command
import shutil
from glob import glob1
from os import path
from json import load


def convert(value):
    """Converts some specific json objects to python object"""
    if isinstance(value, dict):
        return {convert(k): convert(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [convert(element) for element in value]
    else:
        return value


class Clean(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    # noinspection PyMethodMayBeStatic
    def run(self):
        shutil.rmtree('build', ignore_errors=True)
        current = path.realpath('.')
        for _folder in glob1(current, '*.egg-info'):
            shutil.rmtree(path.join(current, _folder), ignore_errors=True)


def readme():
    with open('README.md') as f:
        return f.read()


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


with open('setup.json', 'r') as config_file:
    config = load(config_file, object_hook=convert)


setup(
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requirements(),
    author='Swimlane',
    author_email='info@swimlane.com',
    python_requires='>=3.6',
    package_data={},
    entry_points={},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    cmdclass={'clean': Clean},
    **config
)
