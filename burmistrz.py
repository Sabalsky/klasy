from polityk import Polityk
class Burmistrz(Polityk):
    def __init__(self, name, party, city):
        super().__init__(name, party)
        self.city = city