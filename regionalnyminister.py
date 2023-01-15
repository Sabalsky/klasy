from minister import Minister
class RegionalnyMinister(Minister):
    def __init__(self, name, party, portfolio, region):
        super().__init__(name, party, portfolio)
        self.region = region