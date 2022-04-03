# streamlit-persistence

Allows for persistence of class attributes when building data apps using Streamlit in Python

## Getting started

### Installing

```
python3.9 -m venv venv39 && source venv39/bin/activate
python3.9 -m pip install -U pip setuptools wheel wheel build && python3.9 -m pip install -U pip setuptools wheel wheel build

git clone https://github.com/yaphott/streamlit-persistence.git
cd streamlit-persistence

# Development Mode for Now
python3.9 -m pip install -e .
```

### Using the module

```
import streamlit as st
from streamlit_persistence import PersistentObject


# (1/2) Use 'PersistentObject' as parent class
class Test(PersistentObject):

    # (2/2) Create ref. to session state
    session_state = st.session_state

    colors: list[str] = ["red", "orange", "yellow"]

    def __init__(self) -> None:
        self.color: str = None

    def run(self):
        # Choose index of the previous selection (if not first iteration)
        color_index = self.colors.index(self._color) if self._color else 0

        # Select box with list of colors
        self.color = st.selectbox("Select a color", self.colors, index=color_index)

        st.success(f"You have selected the color {self.color}.")

def main():
    test = Test()
    test.run()

if __name__ == "__main__":
    main()
```
