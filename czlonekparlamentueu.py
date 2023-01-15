from polityk import Polityk
class CzłonekParlamentuEuropejskiego(Polityk):
    def __init__(self, name, party, country):
        super().__init__(name, party)
        self.country = country