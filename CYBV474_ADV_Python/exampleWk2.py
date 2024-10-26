'''
CYBV-474
August 2023
Professor Hand

Panda Simple Dataframe Example

'''

# Standard Library Imports

# 3rd Party Library Imports
print("\nIMPORTING A SIMPLE CSV DATASET")
print("Please wait, importing libraries")
import pandas as pd  # import Pandas 3rd party library

# Main Script Starts Here
if __name__ == '__main__':
    '''
    Example 1 : CREATING A SIMPLE PANDA DATAFRAME
    '''

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)

    print('\n')

    # Create a Panda Dataframe from a JSON File
    df = pd.read_csv(r'CYBER-SALARY.CSV')
    print("\n", df.info())

    print("\n Reported Entry Level Cyber Security Salaries")
    print("\n", df)

    print("\n Sorted Entry Level Cyber Security Salaries")
    df.sort_values(by=['SALARY'], inplace=True)
    print("\n", df)

    print("\n Sorted Entry Level Cyber Security Salaries Highest First")
    df.sort_values(by=['SALARY'], inplace=True, ascending=False)
    print("\n", df)

    print("\nAvgerage Entry Level Cyber Security Salary")

    avgSalary = df["SALARY"].mean()
    avgSalary = round(avgSalary, 2)
    print('AVG $ {:,}'.format(avgSalary))

    print("\nRemove possible outliers and re-calculate average")
    df.drop(df[df.SALARY > 150000].index, inplace=True)
    print("\n", df)
    avgSalary = df["SALARY"].mean()
    avgSalary = round(avgSalary, 2)
    print('AVG $ {:,}'.format(avgSalary))

    # Display the resulting table
    print("\nReset the Index field and Display the final Results")
    df.reset_index(drop=True, inplace=True)
    print("\n", df)








