from radny import Radny
class RadnyMiasta(Radny):
    def __init__(self, name, party, ward, city):
        super().__init__(name, party, ward)
        self.city = city