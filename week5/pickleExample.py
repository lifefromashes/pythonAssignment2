'''
Introduction to the Pickle Library
Professor Hosmer
June 2021
'''

import pickle

print("\nSimple Pickle example\n")

# Open the destination File (write binary)
pickleFileWrite = open('./examplePickle.db', 'wb') 

#Create any python object
pythonList = ["abc", "def", 123, 4096, "End"]

#serialize the list and DUMP to file
print("Serializing a list:", pythonList)
pickle.dump(pythonList, pickleFileWrite)                      
pickleFileWrite.close() 

# Open the pickle file (read binary)
pickleFileRead = open('./examplePickle.db', 'rb')

# LOAD the serialized data into a list + print
print("\nLoading the pickled list\n")
retrievedList = pickle.load(pickleFileRead)

# Display the recovered List

print("Recovered List:    ", retrievedList)

pickleFileRead.close()
