python3.9 setup.py sdist bdist_wheel
python3.9 -m twine check dist/*
python3.9 -m twine upload --repository streamlit-persistence dist/*
