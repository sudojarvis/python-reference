from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('VERSION.txt') as f:
    version = f.read().splitlines()

"""
setup.py file for SWIG example
    name: name of the module
    version: version of the module
    py_modules: list of python modules to be installed
    ext_modules: list of extension modules to be installed
    packages: list of packages to be installed
    package_dir: dictionary of package names and their directories
    package_data: dictionary of package names and their data files
    data_files: list of data files to be installed
    scripts: list of scripts to be installed
    install_requires: list of dependencies to be installed
    author: author name
    author_email: author email
    entry_points:
        pycmd = cli_base.cli:main
            where pycmd is the name of the command line tool
            cli_base is the package name
            and cli is the module name
    
"""
setup(
    name="python command base",
    version=str(version),
    py_modules=['src'],
    package_dir={"": "src"},
    install_requires=required,
    author=', '.join(["mnq78"]),
    author_email=', '.join(["matias.quiroga@nan-labs.com"]),
    entry_points='''
        [console_scripts]
        pycmd=app:start
    ''',
    description="Developer tool CLI base.",
)
