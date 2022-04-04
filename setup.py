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
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "node-and-timestamp",
    },
    install_requires=[
        "streamlit>=1.8.1",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
    python_requires=">=3.9",
)
