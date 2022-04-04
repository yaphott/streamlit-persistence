# streamlit-persistence

Allows for persistence of class attributes when building data apps using Streamlit in Python

## Getting started

### Installing

```
python3.9 -m venv venv39 && source venv39/bin/activate
python3.9 -m pip install -U pip setuptools wheel build && python3.9 -m pip install -U pip setuptools wheel build

git clone https://github.com/yaphott/streamlit-persistence.git
cd streamlit-persistence

# Install
python3.9 -m pip install .
```

### Using the module

```
import streamlit as st
from streamlit_persistence import PersistentObject


# (1/2) Use 'PersistentObject' as parent class
class Test(PersistentObject):

    # (2/2) Set a class attribute with a reference to Streamlit's session state
    session_state = st.session_state

    def __init__(self) -> None:
        self.colors: list[str] = None

        self.color: str = None

    def run(self):
        # Setting an instance attribute
        # The value of self.colors should be None unless modified by a previous iteration
        if self.colors is None:
            self.colors = ["red", "blue", "green"]

        # Select box with the list of colors
        self.color = st.selectbox(
            "Select a color",
            self.colors,
            # Same idea here. We use the index of the user's selection
            # from the previous iteration by checking if the value is None.
            index=self.colors.index(self.color) if self.color is None else 0,
        )

        st.success(f"You have selected the color {self.color}.")


def main():
    test = Test()
    test.run()

if __name__ == "__main__":
    main()
```
