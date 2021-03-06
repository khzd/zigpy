"""Setup module for zigpy"""

import pathlib

from setuptools import find_packages, setup
import zigpy

setup(
    name="zigpy",
    version=zigpy.__version__,
    description="Library implementing a ZigBee stack",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/zigpy/zigpy",
    author="Russell Cloran",
    author_email="rcloran@gmail.com",
    license="GPL-3.0",
    packages=find_packages(exclude=["*.tests"]),
    install_requires=["aiohttp", "crccheck", "pycryptodome", "voluptuous"],
    extras_require={"testing": ["asynctest", "pytest", "pytest-aiohttp"]},
)
