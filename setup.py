from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in interview_test_app/__init__.py
from interview_test_app import __version__ as version

setup(
	name="interview_test_app",
	version=version,
	description="this App is for interview test at samb",
	author="adityayudhap21@gmail.com",
	author_email="adityayudhap21@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
