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
        with open('TitanicPassengers.txt') as f:
            self.examples = f.readlines()
            self.processed = True

        # print(len(self.examples))

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


# def load_string_from_file(filename):
#     """ Read words from filename, return a string composed of the file content. """
#     file = open(filename, "r")
#     lines = file.read()
#     return lines

# file_content = load_string_from_file('TitanicPassengers.txt')
# print('File Contents:\n', file_content)


data = TitanicData("TitanicPassengers.txt")
print(data.isProcessed())
data.buildTitanicExamples()
print('Finished processing', len(data.examples), 'passengers\n')
print(data.isProcessed())