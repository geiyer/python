class School:
    def __init__(self, name, county, zip, state):
        self._name =  name
        self._county = county
        self._zip = zip
        self._state = state

    def __str__(self) -> str:
        return self._name + " in " + self._county + " county"    