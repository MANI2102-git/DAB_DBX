
from setuptools import setup, find_packages

setup(
    name="employeedata",
    version="0.1.0",
    description="Employee data export package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "main=employeedata.main:main",
        ],
    },
)
