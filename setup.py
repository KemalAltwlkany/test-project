import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-package-KemalAltwlkany", # Replace with your own username
    version="0.1.3",
    author="Kemal Altwlkany",
    author_email="kaltwlkany1@etf.unsa.ba",
    description="A hopefully proper python package.",
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
    install_requires=[
    	'numpy<=1.19.3',
    	'pandas>=1.1.4',
    	'plotly>=4.12.0'
    ]
)