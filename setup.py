from setuptools import setup

VERSION = "2.1.1"


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="json-filter",
    version=VERSION,
    description="Filter responses from json output",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="json filter",
    url="https://github.com/danilocgsilva/json-filter",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["jsonfilter"],
    entry_points={"console_scripts": ["jfilter=jsonfilter.__main__:main"]},
    include_package_data=True
)