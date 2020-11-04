import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-generate_mac",
    version="1.3.0",
    author="GI_Jack",
    author_email="GI_Jack@hackermail.com",
    description="Library for generating Ethernet MAC addresses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GIJack/python-generate_mac",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
