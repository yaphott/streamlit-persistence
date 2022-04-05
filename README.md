# streamlit-persistence

Allows for persistence of class attributes when building data apps using Streamlit in Python

I've worked out a few ways I could handle the `__init__` method but have **not had time to implement** them. A temporary workaround*is to use `hasattr` to check if a previous iteration initialized the value.

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

    def run(self):
        if not hasattr(self, "colors"):
            self.colors = [None, "red", "blue", "green"]

        if not hasattr(self, "color"):
            self.color = None

        index = self.colors.index(self.color)
        self.color = st.selectbox("Select a color", self.colors, index=index)

        if self.color:
            return None

        st.success(f"You have selected the color {self.color}.")


def main():
    Test().run()


if __name__ == "__main__":
    main()

```
