from setuptools import setup, find_packages

setup(
    name="hpctools",
    version="0.1.0",
    author="Diogo Silva (diogocsilva)",
    description="HPC automation toolkit for generating Makefiles and SLURM job scripts.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "hpctools = hpctools.cli:cli",
        ],
    },
    install_requires=[
        "click>=8.0",
        "rich>=13.0",
        "questionary>=2.0",
    ],
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)