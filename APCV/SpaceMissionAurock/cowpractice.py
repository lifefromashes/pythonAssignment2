"""
Space Mission to Aurok, Kristin Skipper
APCV 320 Professor Li
4/10/23
"""
import time


class Cow(object):
    """
    Cow is defined as a means to organize cow data including name and weight as
    well as accessing name and weight from a cow object
    Attributes:
    name, a str value, name of the Cow object
    weight, an int value, weight of the Cow object
    i, an int value, IQ of the Cow object
    Methods:
    __init__
    __str__
    Getter methods for name, weight, and i
    getDensity: returns the IQ density of Cow
    """
    def __init__(self, name, weight, iq):
        """
        Parameters:
        n, a str value to set name
        w, an int value to set weight
        i, an int value to set IQ

        """
        self.name = name
        self.weight = weight
        self.iq = iq
        # self.density = density

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getIQ(self):
        return self.iq

    def getDensity(self):
        # DON'T CHANGE
        return self.iq / self.weight

    def __str__(self):
        return ' (' + self.name + ', ' + str(self.weight) + ', ' + str(self.iq) + ')'


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated triples composed of cow name, weight, and iq, and return a
    list containing Cow objects each of which has has a name, a weight, and an iq

    Parameters:
    filename: a str value representing the name of the data file to load data

    Returns:
    a list of Cow objects
    """
    # TODO: Your code here
    # data = []
    # with open(filename, 'r') as file:
    #     for line in file:
    #         cowList = line.strip().split(',')
    #         cowName = cowList[0]
    #         cowWeight = int(cowList[1])
    #         cowIQ = int(cowList[2])
    #         cowDensity = cowIQ / cowWeight
    #         cow = Cow(cowName, cowWeight, cowIQ, cowDensity)
    #         # print('COW', cow)
    #         data.append(cow)
    # return data
    data = []
    with open(filename, 'r') as file:
        for line in file:
            cowName, cowWeight, cowIq = line.strip().split(',')
            cow = Cow(cowName, int(cowWeight), int(cowIq))
            data.append(cow)
    return data


def insertionSort(cows):
    """
    Parameter:
    cows: a list of Cow objects

    Returns a list of Cow objects sorted based on Cow's intelligence density in reverse order.
    That is, the first Cow on the return list has the highest intelligence density, and the
    last one has the lowest intelligence density.
    """
    i, j = 0, 0
    for c in cows:
        if i == 0:
            i += 1
            continue
        # Move elements of cows[0..i-1], that are
        # greater than c, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and c.getDensity() > cows[j].getDensity():
            cows[j + 1] = cows[j]
            j -= 1
        cows[j + 1] = c
        i += 1
    return cows


def greedy(cows, maxCost, method=1):
    """
    Parameters:
    cows: a list of Cow objects
    maxCost: int >0, the maximum weight can be carried by spaceship
    method: int (1 or 2), default value is 1.
        When method == 1, call sorted in Python to sort the cows;
        and when method == 2, call insertionSort defined earlier to sort.
    Returns a tuple (result, totalValue)
    result: a list of Cow objects chosen to transport
    totalValue: int, the sum of the IQ values of the transported Cows
    """
    # Step 1: sort the Cow objects based on their intelligence density
    if method == 1:
        sortedCowList = sorted(cows, key=lambda cow: cow.getDensity(), reverse=True)
    if method == 2:
        sortedCowList = insertionSort(cows)
    # Step 2: pick the Cow objects with constraint of the maximum weight maxCost
    # Hint: You may need to use a loop structure
    result = []
    totalValue, totalCost = 0.0, 0.0
    for cow in sortedCowList:
        if totalCost + cow.getWeight() <= maxCost:
            result.append(cow)
            totalValue += cow.getIQ()
            totalCost += cow.getWeight()

    return result, totalValue


# data = load_cows("cows1.txt")
data = load_cows("testFile.txt")
for i in range(len(data)):
    print('COW DATA: ', data[i])

# Let us try this Cow class
mary = Cow('mary', 3, 120)
print('Cow: ', mary)

result, totalValue = greedy(data, maxCost=1000, method=1)
print("Selected cows:", result)
print("Total IQ value:", totalValue)
print("SORT", insertionSort(data))


#########################################################################

def testGreedy(filename, constraint, method=1, toPrint=False):
    items = load_cows(filename)

    start = time.process_time_ns()
    print("At the beginning of processing {}".format(filename))
    print("Start time (in nanoseconds): {} \n".format(start))

    taken, val = greedy(items, constraint, method)

    end = time.process_time_ns()
    print("At the end of processing {}".format(filename))
    print("End time (in nanoseconds): {} ".format(end))
    print("\nElapsed time to process {} in {} nanoseconds.".format(filename, end - start))

    print('\nTotal value of items taken = {}'.format(val))
    for item in taken:
        if toPrint:
            print('   ', item)


testGreedy("cows1.txt", 100)
print('###########################################')
testGreedy("cows1.txt", 100, 2)
print('###########################################')
testGreedy("cows2.txt", 100)
print('###########################################')
testGreedy("cows2.txt", 100, 2)
