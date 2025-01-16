# local test:
cd $ucxdsa/..
pip install ./dsa_package

# linting
cd dsa_package
ruff check

# testing
* Go to the test directory:
* cd tests
* python -m unittest

# pdoc website
https://pdoc3.github.io/pdoc/

# generate documentation
* cd src
* pdoc --html --force dsa/
* (no need) zip -vr dsadocs.zip html/ -x "*.DS_Store"

# build package
update readme
Update the versions at: pyproject.toml
update dates in src/dsa/__init__.py
Go to the distribution directory:
* dsa_package
* update version in pyproject.toml
* python -m build

# upload dsa package (Note: cannot overwrite existing version! need to update version)
### upload to test server
delete everything in dist
python -m twine upload --repository testpypi dist/*

# upload to official server 
python -m twine upload --skip-existing dist/*
If errors, make sure to update pkginfo:
pip install --upgrade pkginfo

# To verify on pypi
https://pypi.org/project/ucxdsa/2024.5.9/
https://pypi.org/project/ucxdsa/<version_number>/

# update DSA page
