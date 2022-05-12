from typing import Any

# https://docs.python.org/3/reference/datamodel.html#special-method-lookup


class Meta(type):
    def __getattribute__(cls, attr: str) -> Any:
        return super().__getattribute__(attr)

    def __setattr__(cls, attr: str, value: Any) -> None:
        super().__setattr__(attr, value)

    def __delattr__(cls, attr: str) -> None:
        super().__delattr__(attr)

    def __dir__(cls) -> list[str]:
        super().__dir__()


class PersistentObject(metaclass=Meta):
    session_state = None

    def __getattribute__(self, attr: str):
        session_state = super().__getattribute__("session_state")
        if attr in list(session_state.keys()):
            # Get (user-defined) value from a key in the session state
            return session_state[attr]
        else:
            # Get class attribute
            return super().__getattribute__(attr)

    def __setattr__(self, attr: str, value: Any) -> None:
        if attr not in super().__dir__():
            # Set (user-defined) value at a key in the session state
            session_state = super().__getattribute__("session_state")
            session_state[attr] = value
        else:
            # Set class attribute
            super().__setattr__(attr, value)

    def __delattr__(self, attr: str) -> None:
        if attr not in super().__dir__():
            # Delete (user-defined) value at a key in the session state
            session_state = super().__getattribute__("session_state")
            del session_state[attr]
        else:
            # Delete class attribute
            super().__delattr__(attr)

    def __dir__(self) -> list[str]:
        session_state = super().__getattribute__("session_state")
        return super().__dir__() + list(session_state.keys())
