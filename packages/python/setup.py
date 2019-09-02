from distutils.core import setup


with open("VERSION", "r") as f:
    version = f.read()

with open("README.md", "r") as f:
    long_description = f.read()

with open("./requirements/prod.txt", "r") as f:
    install_requires = f.read().split("\n")

setup(
    name="SPL",
    version=version,
    author="Franciscp J. Piedrahita",
    author_email="fpiedrah93@gmail.com",
    packages=["spl", "tests"],
    setup_requires=['wheel'],
    url="HTTP://github.com/SPLA/SPL-Solver",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Product Lines :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    description="Utilities for software product lines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3",
    install_requires=install_requires,
)
