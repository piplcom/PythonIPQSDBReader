import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonIPQSDBReader",
    version="2.0.0",
    author="IPQualityScore",
    author_email="support@ipqualityscore.com",
    description="IPQualityScore IP Address Reputation & Proxy Detection DB Reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IPQualityScore/PythonIPQSDBReader",
    packages=setuptools.find_packages(),
    install_requires=["aiofiles==23.1.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
