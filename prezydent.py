from polityk import Polityk
class Prezydent(Polityk):
    def __init__(self, name, party, term_length):
        super().__init__(name, party)
        self.term_length = term_length
