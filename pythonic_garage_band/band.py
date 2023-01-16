# Create a band class
class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members or []

    # retuns the string correlated with solo playing below
    def play_solos(self):
        return [member.play_solo() for member in self.members]

    # Tells you the name of the band 
    def __str___(self):
        return f"Our band name is {self.name}"

    # returns what class it is an instance of and the name of the instance
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    
# base class
class Musician:
    def __init__(self, name, instrument, solo, solos):
        self.name = name
        self.instrument = instrument
        self.solo = solo
    # gets instrument from musician class
    def get_instrument(self):
        return self.instrument

    # string of what the musicans name and instrument are
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    # produces string representing an instance of musican and what the musicians name is
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    # returns the solo for the musician 
    def play_solo(self):
        return self.solo



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
