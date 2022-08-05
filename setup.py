from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="avas",  # Required
    version="0.1.1a1",  # Required
    description="A python module for the AVAS minecraft server api",  # Optionalional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/Scratchdragon/AVAS.py",  # Optional
    author="Scratchdragon",  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "License :: Creative Commons :: CC0 1.0 Universal",
        
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    keywords="api, minecraft, avas, development",  # Optional
    py_modules=["avas"],
    python_requires=">=3.0, <4",
    install_requires=["json","requests"],  # Optional
    #extras_require={  # Optional
    #    "dev": ["check-manifest"],
    #    "test": ["coverage"],
    #},
    project_urls={  # Optional
        "Bug Reports": "https://github.com/Scratchdragon/AVAS.py/issues",
        "Source": "https://github.com/Scratchdragon/AVAS.py/",
    },
)
