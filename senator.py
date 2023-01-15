from polityk import Polityk
class Senator(Polityk):
    def __init__(self, name, party, state):
        super().__init__(name, party)
        self.state = state