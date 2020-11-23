import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-package-KemalAltwlkany", # Replace with your own username
    version="0.0.1",
    author="Kemal Altwlkany",
    author_email="kaltwlkany1@etf.unsa.ba",
    description="An hopefully proper python package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KemalAltwlkany/test-project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)