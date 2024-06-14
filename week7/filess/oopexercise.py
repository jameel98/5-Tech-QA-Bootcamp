class City:
    def __init__(self, name, passcode):
        self._name = name
        self._passcode = passcode

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    # Getter for passcode
    @property
    def passcode(self):
        return self._passcode

    # Setter for passcode
    @passcode.setter
    def passcode(self, passcode):
        if isinstance(passcode, (int, str)) and str(passcode).strip():
            self._passcode = passcode
        else:
            raise ValueError("Passcode must be a non-empty string or integer")
