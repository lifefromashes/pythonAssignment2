'''
Kristin Skipper
Week 10 Exercise #10
OCT 2024
CYBV-474
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file = 'WA_Fn-UseC_-Sales-Win-Loss.csv'
sales_data = pd.read_csv(file)
sales_data.head(n=2)
sales_data.tail(n=2)
sales_data.dtypes

#Using head() method with an argument which helps us to restrict the number of initial records that should be displayed
# print(sales_data.head(n=2))


# set the background colour of the plot to white
# set is depricated, recommended to use set_theme
sns.set_theme(style="whitegrid", color_codes=True)

# setting the plot size for all plots
# set is depricated, recommended to use set_theme
sns.set_theme(rc={'figure.figsize':(11.7,8.27)})

# create a countplot
# sns.countplot('Route To Market',data=sales_data,hue = 'Opportunity Result')
# had to change to this as was getting an error countplot() got multiple values for argument 'data'
sns.countplot(x='Route To Market', hue='Opportunity Result', data=sales_data)
# Remove the top and down margin
sns.despine(offset=10, trim=True)
# display the plot
plt.show()

# setting the plot size for all plots for violin plot
sns.set_theme(rc={'figure.figsize':(16.7,13.27)})

# plotting the violinplot
sns.violinplot(x="Opportunity Result",y="Client Size By Revenue", hue="Opportunity Result", data=sales_data)
plt.show()

#import the necessary module
from sklearn import preprocessing
# create the Labelencoder object
le = preprocessing.LabelEncoder()
#convert the categorical columns into numeric
encoded_value = le.fit_transform(["paris", "paris", "tokyo", "amsterdam"])
print(encoded_value)

print("Supplies Subgroup' : ",sales_data['Supplies Subgroup'].unique())
print("Region : ",sales_data['Region'].unique())
print("Route To Market : ",sales_data['Route To Market'].unique())
print("Opportunity Result : ",sales_data['Opportunity Result'].unique())
print("Competitor Type : ",sales_data['Competitor Type'].unique())
print("'Supplies Group : ",sales_data['Supplies Group'].unique())

# create the Labelencoder object
le = preprocessing.LabelEncoder()
#convert the categorical columns into numeric
sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])
#display the initial records
print(sales_data.head())

# select columns other than 'Opportunity Number','Opportunity Result'
cols = [col for col in sales_data.columns if col not in ['Opportunity Number','Opportunity Result']]
# dropping the 'Opportunity Number'and 'Opportunity Result' columns
data = sales_data[cols]
#assigning the Oppurtunity Result column as target
target = sales_data['Opportunity Result']
print(data.head(n=2))

#import the necessary module
from sklearn.model_selection import train_test_split
#split data set into train and test sets
data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.30, random_state = 10)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#create object of the lassifier
neigh = KNeighborsClassifier(n_neighbors=3)
#Train the algorithm
neigh.fit(data_train, target_train)
# predict the response
pred = neigh.predict(data_test)
# evaluate accuracy
print ("KNeighbors accuracy score : ",accuracy_score(target_test, pred))


