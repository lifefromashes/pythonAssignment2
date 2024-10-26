'''
CYBV-474
September 2024

Kristin Skipper

'''

# Standard Library Imports

# 3rd Party Library Imports
print("Please wait, importing libraries")
import pandas as pd  # import Pandas 3rd party library
import matplotlib.pyplot as plt
import numpy as np

# Main Script Starts Here
if __name__ == '__main__':
    '''
    Creating a Panda Dataframe from a CSV File
    '''

    print("Assignment 3")
    # Set no display limits and a large width
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)

    # Create a Panda Dataframe from a CSV File
    df = pd.read_csv(r'IP-CONNECT.CSV')

    # Filter out rows that have IPV6 addresses
    print('Length of df before filtering out IPV6: ', (len(df)))
    df_filtered = df[df['ipV6'] == 0]
    print('Length of df after filtering out IPV6: ', (len(df_filtered)))

    print('\n Filtered DF')
    print(df_filtered.head(10))

    column_list = [
        'CONNECTION', 'TOTAL', 'ipV4', 'TCP', 'UDP', 'ARP', 'ICMP', 'IGMP', 'CAST', 'INTERNAL', 'DOMESTIC',
        'FOREIGN', 'HOSTILE'
    ]

    # Create Paired DFs starting after Connection since it doesn't need to be paired with itself
    for column in column_list[1:]:
        paired_df = df_filtered[['CONNECTION', column]]
        print(f"Paired DataFrame with CONNECTION and {column}:")
        # print(paired_df.head(25))  # printing just the first 25 for console space.
        print(paired_df)  # printing just the first 25 for console space.
        print("\n")

    # Map the non-numeric data to numermic values
    # First create dict of unique items for each column required
    unique_vals_dict = {}
    for col in column_list:
        unique_vals = df[col].unique()
        unique_vals_dict[col] = {val: idx + 1 for idx, val in enumerate(unique_vals)}

    np_arrays = {}
    for col in column_list:
        # Replace the column values with their numeric mappings from the dictionary
        np_arrays[col] = df[col].map(unique_vals_dict[col]).to_numpy()

    # Generate a horizontal bar chart for each column
    for column in column_list[1:]:
        plt.figure(figsize=(10, 6))
        plt.barh(np_arrays['CONNECTION'], np_arrays[column], color='hotpink')

        plt.title(f'Horizontal Bar Chart for CONNECTION and {column}')
        plt.xlabel(column)
        plt.ylabel('Connection')
        # Ensure labels are visible
        plt.tight_layout()
    plt.show()

