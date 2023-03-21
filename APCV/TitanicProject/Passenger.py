class Passenger(object):
    """
    A class to represent a Passenger object for Titanic data

    Attributes:
    cabinClass - an int value (1 or 2 or 3)
    gender - a string value equals to either 'M' or 'F'
    label - a string value either "Survived" or "Died"
    name - a string for the passenger name

    Methods:
    __init__
    Getter methods to access the data attributes
    __str__

    """

    def __init__(self, cabinClass, gender, label, name):
        self.cabinClass = cabinClass
        self.gender = gender
        self.label = label
        self.name = name

    def getCabinClass(self):
        return self.cabinClass

    def getGender(self):
        return self.gender

    def getName(self):
        return self.name

    def getLabel(self):
        return self.label

    def __str__(self):
        return '{self.name}, {self.label}, gender({self.gender}), booked cabin class {self.cabinClass}'.format(
            self=self)


# p = Passenger(1, 'F', 'Survived', 'Miss. Elisabeth Walton Allen')
# print(p)


