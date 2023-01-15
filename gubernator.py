from polityk import Polityk
class Gubernator(Polityk):
    def __init__(self, name, party, state):
        super().__init__(name, party)
        self.state = state