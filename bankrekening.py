# https://dodona.be/nl/courses/4195/series/46776/activities/2096226599


class BankRekening:
    def __init__(self, naamRekeninghouder, rekeningNummer, initieelBedrag=0):
        self.naamRekeninghouder = naamRekeninghouder
        self.rekeningNummer = rekeningNummer
        self.saldo = initieelBedrag

    def storten(self, bedrag):
        self.saldo += bedrag

    def afhalen(self, bedrag):
        self.saldo -= bedrag

    def __str__(self):
        return f"{self.naamRekeninghouder}, {self.rekeningNummer}, bedrag: {self.saldo}"

    def __repr__(self):
        return f"BankRekening('{self.naamRekeninghouder}', '{self.rekeningNummer}', {self.saldo})"
