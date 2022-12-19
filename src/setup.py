from setuptools import setup

NAME = "walpackagetest"
VERSION = "1.2.2"

INSTALL_REQUIRES = [
    "selenium >=4.0.0, <4.1.4",
    "pytest >=6.2.5, < 7.0.0",
    "pytest-bdd >=5.0.0, < 6.0.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="this is just a description",
    long_description="this is just a long description",
    author="Waleed",
    author_email="mwzulfiqar@live.com",
    license="MIT",
    packages=["walpackagetest", "walpackagetest"],
    install_requires=INSTALL_REQUIRES,
    entry_points={"pytest11": ["walpackagetest = walpackagetest.core"]},
    classifiers=["Framework :: Pytest"],
)
