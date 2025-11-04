from setuptools import find_packages, setup

with open("./README.md", "r") as file:
    long_description = file.read()

setup(
    name="ima-314",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "./algorithms"},
    packages=find_packages(where="./algorithms"),
    url="https://github.com/Gireesh-Kumar-Gowd/Optmizers-in-Machine-Learning",
    author="Gireesh",
    author_email="gireeshkumargowd@gmail.com",
)
