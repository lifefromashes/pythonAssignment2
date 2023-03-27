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
        with open(self.fname, 'r') as f:
            lines = f.readlines()

        for line in lines:
            values = line.strip().split(',')
            cabinClass = int(values[0])
            age = float(values[1])
            gender = values[2]
            label = int(values[3])
            name = values[4] + ', ' + values[5]

            passenger = Passenger(cabinClass, gender, label, name)
            self.examples.append(passenger)

        self.processed = True

    # def buildTitanicExamples(self):
    #     """
    #     Build all Passenger objects by parsing the file data.
    #     By this method, self.examples is set as the the list of Passenger objects
    #     built based on the given file with fname; and self.processed is set as True
    #     """
        # with open(self.fname) as f:
        #     passengerList = f.readlines()
        #     passengerList = [x.strip() for x in passengerList]
        #     print('Passenger List: ', passengerList)
        #     # lines = [line.strip() for line in f]
        # for item in passengerList:
        #     name = item[11::]
        #     print('name', name)
        #     cabinClass = int(item[0])
        #     print('cabin class', cabinClass)
        #     label = item[9]
        #     print('label', label)
        #     gender = item[7]
        #     print('gender', gender)
        #     passenger = Passenger(cabinClass, gender, label, name)
        #     print(passenger)
        #     print(type(passenger.getCabinClass()))
        #
        #     self.examples.append(passenger)
        # print('example list after mod:', self.examples)
        # print('length of ex list:', len(self.examples))
        # self.processed = True

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

        count = 0
        for person in persons:
            if person.getCabinClass() == cabinClass:
                count += 1
        return count


# data = TitanicData("TitanicPassengers.txt")
# data = TitanicData("titanicList2.txt")
# print(data.isProcessed())
# data.buildTitanicExamples()
# print('Finished processing', len(data.examples), 'passengers\n')
# print(data.isProcessed())

# Create a TitanicData instance and build the examples
titanic_data = TitanicData('titanicList2.txt')
titanic_data.buildTitanicExamples()

# Get the list of passengers and cabin class value
passengers = titanic_data.examples
cabin_class = 1

# Call the countPassengers() method to count the number of passengers who booked the specified cabin class
count = countPassengers(passengers, cabin_class)

# Print the result
print(f"{count} passengers booked cabin class {cabin_class}")

print('COUNT PASSENGER CABIN CLASS: ', data.countPassengers(data.examples, 1))

# print('Count Passengers: ', data.countPassengers(data.examples, 1))
# print('PRint statement data.examples', data.examples)
# print(len(data.examples))
# print('example list', data.examples)
# print('Survived Passengers: ', data.survivedPassengers(data.examples, 'F'))
