from setuptools import setup

with open("README.md", mode="r", encoding="utf-8") as r:
    long_description = r.read()

setup(
    name="streamlit-persistence",
    version="0.0.3",
    author="yaphott",
    author_email="yaphott@gmail.com",
    description="Allows for persistence of class/instance attributes when using Streamlit in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaphott/streamlit-persistence",
    packages=["streamlit_persistence"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords=["streamlit", "persistence", "attributes", "data-science", "developer-tools"],
    install_requires=["streamlit>=1.8.1"],
    python_requires=">=3.9",
)
