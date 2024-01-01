from setuptools import find_packages, setup


def requirements_from_file(file_name):
    return open(file_name).read().splitlines()


print("Found packages:", find_packages())

setup(
    name="qdvis",
    description="qdvis: Quick data visualizer.",
    author="Takeguchi",
    author_email="hirotake.stu@gmail.com",
    maintainer="Takeguchi",
    maintainer_email="hirotake.stu@gmail.com",
    url="https://github.com/ta-ke-inf/qdvis/tree/main",
    download_url="https://github.com/ta-ke-inf/qdvis/tree/main",
    license="MIT",
    version="0.1.0",
    keywords="visualization ml",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements_from_file("requirements.txt"),
    entry_points={"console_scripts": ["qdvis=qdvis.cli:main"]},
)
