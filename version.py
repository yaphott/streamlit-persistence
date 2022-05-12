import importlib.metadata


try:
    __version__ = importlib.metadata.version("streamlit-persistence")
except importlib.metadata.PackageNotFoundError:
    __version__ = None
