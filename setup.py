from setuptools import setup, find_packages

setup(
    name='taverner',  # Change this to your project's name
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    tests_require=[
        'pytest',  # Ensure pytest is installed for testing
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change as needed
    ],
)
