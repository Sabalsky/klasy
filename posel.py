from polityk import Polityk
class Poseł(Polityk):
    def __init__(self, name, party, constituency):
        super().__init__(name, party)
        self.constituency = constituency