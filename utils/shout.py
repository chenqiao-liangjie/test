def shout(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return text.upper()
