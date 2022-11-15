import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    # Add your list of production dependencies here
    'docopt==0.6.2',
]

DEV_REQUIREMENTS = [
    'black == 22.*',
    'build == 0.7.*',
    'flake8 == 4.*',
    'isort == 5.*',
    'mypy == 0.942',
    'pytest == 7.*',
    'pytest-cov == 4.*',
    'twine == 4.*',
]

setuptools.setup(
    name='reverse_polish_notation',
    version='0.1.0',
    description='Reverse Polish Notation calculator implementation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/marbuzova/reverse-polish-notation',
    author='marbuzova',
    packages=setuptools.find_packages(
        exclude=[
            'test',
        ]
    ),
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'reverse-polish=reverse_polish_notation.app:main',
        ]
    },
    python_requires='>=3.7, <4',
)