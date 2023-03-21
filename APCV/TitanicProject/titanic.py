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
        # passenger = Passenger(self.examples)
        with open('TitanicPassengers.txt') as f:
            # for line in f:
            # passenger = Passenger(self.gender, self.name, self.label)
            passengerList = f.readlines()
            name = []
            label = []
            cabinClass = []
            gender = []
            for line in passengerList:
                newList = line.split(",")
                self.examples.append(newList)
                for item in newList:
                    # print('item', item[0:6])
                    name = item[0::]
                    # label = item[0][1]
                    passenger = Passenger(name, label, cabinClass, gender)
                print('label', label)
            print('newlist', self.examples)
            print(passenger)

            # print(self.examples)
            # print(len(self.examples))

            self.processed = True
        print('Example list', self.examples)

        # print(person)

        # ['1,29.0,F,1,Allen, Miss. Elisabeth Walton\n',

        # print(len(self.examples))
        # print('examples list', self.examples)

    def isProcessed(self):
        return self.processed

    def countPassengers(self, persons, cabinClass):
        """
        Given a list of Passenger objects and a cabin class value,
        return the number of persons who booked the cabin class

        Parameters:
        persons - a list of Passenger objects
        cabinClass - a int value equals to either 1 or 2 or 3

        Returns:
        the number of persons who booked the cabin class
        """
        pass



# p = Passenger(1, 'F', 'Survived', 'Miss. Elisabeth Walton Allen')
# print('The passenger is: ', p)
#
data = TitanicData("TitanicPassengers.txt")
print(data.isProcessed())
data.buildTitanicExamples()
print('Finished processing', len(data.examples), 'passengers\n')
print(data.isProcessed())

# print(count_passengers(data.examples, 1))
