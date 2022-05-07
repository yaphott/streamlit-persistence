from setuptools import setup

with open("README.md", mode="r", encoding="utf-8") as r:
    long_description = r.read()

setup(
    name="streamlit-persistence",
    version="0.0.2",
    author="yaphott",
    author_email="yaphott@gmail.com",
    description="Allows for persistence of class/instance attributes when using Streamlit in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaphott/streamlit-persistence",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/streamlit-persistence/issues",
    # },
    packages=["streamlit_persistence"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["streamlit>=1.8.1"],
    python_requires=">=3.9",
)
