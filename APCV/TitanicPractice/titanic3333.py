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
        with open(self.fname) as f:
            passengerList = f.readlines()

            for line in passengerList:
                newList = line.split(",")
                name = newList[4:7]
                gender = newList[2]
                cabinClass = int(newList[0])
                label = newList[3]

                passenger = Passenger(cabinClass, gender, label, name)

                self.examples.append(passenger)
                # self.examples.append(passengerList)
                # self.examples.append(newList)
            print('PASSENGER', passenger)
            print('outside for loop', len(self.examples))
            self.processed = True
            # print('PASSENGER_LIST', passengerList)
        # print(passenger)
        print('asdfasdf', passengerList)
        # print('asdfasdf', len(passengerList))
        return passengerList

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
        # persons = self.buildTitanicExamples()
        # passenger = self.buildTitanicExamples()
        # print('PAAAASSSENGER', passenger)

        # for p in passenger:
        #     count = 0
        #     if cabinClass == 1:
        #         count += 1
        # return count
        # count = 0
        # for person in persons:
        #     if cabinClass == 1:
        #         count += 1
        # return count
        # for index, value in enumerate(persons):
        #     print(index, value)
        count = 0
        # cabinClassList = []
        # for item in persons:
        #     if cabinClass == 1:
        #         count += 1
        #         cabinClassList.append(count)

        # print('Cabin class list count',len( cabinClassList))
        for person in persons:
            p = persons[0][cabinClass] == 1
            cabinClass1True = cabinClass == 1
            if cabinClass1True:
                count += 1
        print("COUNNNNT", count)



    def survivedPassengers(self, persons, gender):
        """
        Given a list of Passenger objects and a gender value,
        return the number of survived persons with a certain gender

        Parameters:
        persons - a list of Passenger objects
        gender - a string value equals to either 'M' or 'F'

        Returns:
        the number of survived persons with gender
        """
        pass


# p = Passenger(1, 'F', 'Survived', 'Miss. Elisabeth Walton Allen')
# print('The passenger is: ', p)
#
# data = TitanicData("TitanicPassengers.txt")
data = TitanicData("titanicList2.txt")
print(data.isProcessed())
data.buildTitanicExamples()
print('Finished processing', len(data.examples), 'passengers\n')
print(data.isProcessed())

print('Count Passengers: ', data.countPassengers(data.examples, 1))
# print('PRint statement data.examples', data.examples)
print(len(data.examples))
# print('example list', data.examples)
print('Survived Passengers: ', data.survivedPassengers(data.examples, 'F'))
