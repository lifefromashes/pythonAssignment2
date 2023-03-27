# TITANIC ASSIGNMENT / KRISTIN SKIPPER 03_25_2023 / APCV 320  / PROFESSOR LI XU

class Passenger:
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


class TitanicData(object):
    """
    A class to process Titanic data
    Attributes:
    fname - a string value representing the filename
    processed - a bool value True or False
    examples - a list of Passengers
    Methods:
    __init__
    buildTitanticExamples

    """

    def __init__(self, fname):
        self.fname = fname
        self.processed = False
        self.examples = []

    def buildTitanicExamples(self):
        """
        Build all Passenger objects by parsing the file data.
        By this method, self.examples is set as the the list of Passenger objects
        built based on the given file with fname; and self.processed is set as True
        """
        with open(self.fname, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                cabinClass = int(data[0])
                gender = data[2]
                label = 'Survived' if data[3] == '1' else 'Died'
                name = data[4] + ', ' + data[5]
                passenger = Passenger(cabinClass, gender, label, name)
                self.examples.append(passenger)

        self.processed = True

    def isProcessed(self):
        return self.processed


def countPassengers(persons, cabinClass):
    """
    Given a list of Passenger objects and a cabin class value,
    return the number of persons who booked the cabin class
    Parameters:
    persons - a list of Passenger objects
    cabinClass - a int value equals to either 1 or 2 or 3
    Returns:
    the number of persons who booked the cabin class
    """
    count = 0
    for passenger in persons:
        if passenger.getCabinClass() == cabinClass:
            count += 1
    return count


def survivedPassengers(persons, gender):
    """
    Given a list of Passenger objects and a gender value,
    return the number of survived persons with a certain gender

    Parameters:
    persons - a list of Passenger objects
    gender - a string value equals to either 'M' or 'F'

    Returns:
    the number of survived persons with gender
    """
    survived_count = 0
    for person in persons:
        if person.getGender() == gender and person.getLabel() == "Survived":
            survived_count += 1
    return survived_count


p = Passenger(1, 'F', 'Survived', 'Miss. Elisabeth Walton Allen')
print(p)
data = TitanicData("TitanicPassengers.txt")
print(data.isProcessed())
data.buildTitanicExamples()
print('Finished processing', len(data.examples), 'passengers\n')
print(data.isProcessed())
print('COUNT PASSENGER CABIN CLASS: ', countPassengers(data.examples, 1))
print('SURVIVED PASSENGER: ', survivedPassengers(data.examples, 'F'))
