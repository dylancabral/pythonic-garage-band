class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members or []

    def play_solos(self):
        return [member.play_solo() for member in self.members]
# base class
class Musician(Band):
    def __init__(self, name, instrument, solo, solos):
        self.name = name
        self.instrument = instrument
        self.solo = solo
        self.solos = solos

    def get_instrument(self):
        return self.instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def play_solo(self):
        return self.solo

    def play_solos(self):
        return self.solos


# derived classes
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar", "face melting guitar solo", "face melting guitar solo")


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass", "bom bom buh bom", "bom bom buh bom")


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums", "rattle boom crash", "rattle boom crash")