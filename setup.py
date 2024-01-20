from setuptools import find_packages, setup


def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme

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
    version="0.1.2",
    keywords="visualization ml",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements_from_file("requirements.txt"),
    entry_points={"console_scripts": ["qdvis=qdvis.cli:main"]},
)
