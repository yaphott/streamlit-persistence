# streamlit-persistence

Allows for persistence of class/instance attributes when using Streamlit in Python

## Getting started

### Installing

```bash
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install streamlit-persistence
```

or

```bash
git clone https://github.com/yaphott/streamlit-persistence.git
cd streamlit-persistence
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
```

### Using the module

1. Use `PersistentObject` as the parent class
2. Assign the Streamlit `session_state` to a class attribute named `session_state`
3. Assign class/instance attributes as you would normally
   - Still need to implement a proper way to handle the `__init__` method
   - Until then you can simply check an instantiated class for the instance attribute using `hasattr` before it is referenced

```python
import streamlit as st
from streamlit_persistence import PersistentObject


options = [None, "veggie", "pepperoni"]


class Test(PersistentObject):
    session_state = st.session_state

    def run(self):
        if not hasattr(self, "pizza"):
            self.pizza = None

        # Default to the index of previously selected
        selected = st.selectbox(
            "Select a pizza",
            options,
            index=options.index(self.pizza),
        )

        # Update instance attribute if user changes their selection
        if self.pizza != selected:
            self.pizza = selected
            st.experimental_rerun()

        st.success(f"You have selected the pizza: {self.pizza}")


def main():
    Test().run()


if __name__ == "__main__":
    main()
```
