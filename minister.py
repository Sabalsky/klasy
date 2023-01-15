from polityk import Polityk
class Minister(Polityk):
    def __init__(self, name, party, portfolio):
        super().__init__(name, party)
        self.portfolio = portfolio