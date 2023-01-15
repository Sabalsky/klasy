from polityk import Polityk
class SekretarzStanu(Polityk):
    def __init__(self, name, party, department):
        super().__init__(name, party)
        self.department = department