def greet(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    return f"Hello, {name}!"
