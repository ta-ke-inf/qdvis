from setuptools import find_packages, setup


def requirements_from_file(file_name):
    return open(file_name).read().splitlines()


print("Found packages:", find_packages())

setup(
    name="qdvis",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements_from_file("requirements.txt"),
    entry_points={"console_scripts": ["qdvis=qdvis.cli:main"]},
)
