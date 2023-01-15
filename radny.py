from polityk import Polityk
class Radny(Polityk):
    def __init__(self, name, party, ward):
        super().__init__(name, party)
        self.ward = ward