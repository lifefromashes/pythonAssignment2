from APCV.TitanicProject.TitanicPractice.Passenger import Passenger


class TitanicData(Passenger):
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
            passengerList = [x.strip() for x in passengerList]
            print('Passenger List: ', passengerList)
            # lines = [line.strip() for line in f]
        for item in passengerList:
            name = item[11::]
            # print('name', name)
            cabinClass = int(item[0])
            # print('cabin class', cabinClass)
            label = item[9]
            # print('label', label)
            gender = item[7]
            # print('gender', gender)
            passenger = Passenger(cabinClass, gender, label, name)
            # print(passenger)
            # print(type(passenger.getCabinClass()))

            self.examples.append(passenger)
        print('example list after mod:', self.examples)
        print('length of ex list:', len(self.examples))
        self.processed = True

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
        passList = persons
        count = 0
        for person in passList:
            if Passenger.getCabinClass(self) == 1:
                count += 1
                print('cabin class count: ', count)


data = TitanicData("titanicList2.txt")
print(data.isProcessed())
data.buildTitanicExamples()
print('Finished processing', len(data.examples), 'passengers\n')
print(data.isProcessed())

print('COUNT PASSENGER CABIN CLASS: ', data.countPassengers(data.examples, 1))
