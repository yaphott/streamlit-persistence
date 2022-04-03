import setuptools

setuptools.setup(
    name="streamlit-persistence",
    description="Allows for persistence of class attributes when building data apps using Streamlit in Python",
    author="yaphott",
    packages=[
        "streamlit_persistence",
    ],
    classifiers=[
        "Development Status :: 0.1",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "streamlit>=1.8.1",
    ],
    include_package_data=True,
    python_requires=">=3.9",
    version="0.0.1",
)
