from setuptools import setup, find_packages # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='label_studio_cli',
    version='0.1',
    author='Spinnernicholas',
    author_email='spinnernicholas@gmail.com',
    description='A CLI for Label Studio',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Spinnernicholas/label-studio-cli',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ls-cli = label_studio_cli.main:main'
        ],
    },
    extras_require={
        'dev': [
            'label-studio==1.12.0'
        ]
    },
)