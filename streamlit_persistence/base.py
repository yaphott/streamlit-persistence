from typing import Any


class Meta(type):
    def __getattribute__(cls, name: str) -> Any:
        return super().__getattribute__(name)

    def __setattr__(cls, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __dir__(cls) -> list[str]:
        super().__dir__()


class PersistentObject(metaclass=Meta):
    session_state = None

    def __getattribute__(self, name: str):
        session_state = super().__getattribute__("session_state")
        if name in list(session_state.keys()):
            # User-Defined Attribute from Session State
            return session_state[name]
        else:
            # Class Attribute
            return super().__getattribute__(name)

    def __setattr__(self, name: str, value: Any) -> None:
        session_state = super().__getattribute__("session_state")
        if name not in super().__dir__():
            # Assign User-Defined Attribute to Session State
            session_state[name] = value
        else:
            # Assign Class Attribute
            super().__setattr__(name, value)

    def __dir__(self) -> list[str]:
        session_state = super().__getattribute__("session_state")
        return super().__dir__() + list(session_state.keys())
