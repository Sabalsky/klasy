from burmistrz import Burmistrz
class BurmistrzDzielnicy(Burmistrz):
    def __init__(self, name, party, city, district):
        super().__init__(name, party, city)
        self.district = district