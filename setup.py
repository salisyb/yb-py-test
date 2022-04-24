from setuptools import setup, find_packages


setup(
    name='yb-py-test',
    version='1.0',
    license='MIT',
    author="Salis Abubakar",
    author_email='salisbell404@gmail.com',
    url="https://github.com/salisyb/yb-py-test",
    packages=find_packages('sample'),
    package_dir={'': 'sample'},
    keywords='example project',
    install_requires=[
        'requests',
    ],

)
