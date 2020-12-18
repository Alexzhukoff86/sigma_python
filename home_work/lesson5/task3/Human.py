class Human:

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name.capitalize()
        self._last_name = last_name.capitalize()
        self._fullname = " ".join([self._first_name, self._last_name])