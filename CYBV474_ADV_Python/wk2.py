'''
CYBV-474
September 2024

Kristin Skipper

'''

# Standard Library Imports

# 3rd Party Library Imports
print("Please wait, importing libraries")
import pandas as pd  # import Pandas 3rd party library

# Main Script Starts Here
if __name__ == '__main__':
    '''
    Creating a Panda Dataframe from a CSV File
    '''

    print("Assignment 2 - STARTER SCRIPT")
    # Set no display limits and a large width
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)

    # Create a Panda Dataframe from a CSV File
    df = pd.read_csv(r'ipObservations.csv')

    # Filter out values of IPV6
    print('Length of df before filtering out IPV6: ', (len(df)))
    df.drop(df[df['FRAME-TYPE'] == 'IPV6'].index, inplace=True)
    print('Length of df after filtering out IPV6: ', (df.shape[0]))

    print('\n Filtered DF')
    print(df.head(10))

    # Map the non-numeric data to numermic values
    # First create dict of unique items for each column required
    src_vals = df['SRC-PORT'].unique()
    unique_src_port_dict = {val: idx + 1 for idx, val in enumerate(src_vals)}
    dst_vals = df['DST-PORT'].unique()
    uniqueDstPortDict = {val: idx + 1 for idx, val in enumerate(dst_vals)}
    frame_vals = df['FRAME-TYPE'].unique()
    uniqueFrameDict = {val: idx + 1 for idx, val in enumerate(frame_vals)}
    protocol_vals = df['PROTOCOL'].unique()
    uniqueProtocolDict = {val: idx + 1 for idx, val in enumerate(protocol_vals)}
    srcCountry_vals = df['SRC-COUNTRY'].unique()
    uniqueSrcCountryDict = {val: idx + 1 for idx, val in enumerate(srcCountry_vals)}
    dstCountry_vals = df['DST-COUNTRY'].unique()
    uniqueDstCountryDict = {val: idx + 1 for idx, val in enumerate(dstCountry_vals)}

    df['SRC-PORT'] = df['SRC-PORT'].map(unique_src_port_dict)
    df['DST-PORT'] = df['DST-PORT'].map(uniqueDstPortDict)
    df['FRAME-TYPE'] = df['FRAME-TYPE'].map(uniqueFrameDict)
    df['PROTOCOL'] = df['PROTOCOL'].map(uniqueProtocolDict)
    df['SRC-COUNTRY'] = df['SRC-COUNTRY'].map(uniqueSrcCountryDict)
    df['DST-COUNTRY'] = df['DST-COUNTRY'].map(uniqueDstCountryDict)

    # sort by highest observed connection
    df.sort_values(by=['Observed'], inplace=True, ascending=False)
    print('\n Sorted DF')
    print(df.head(10))

    # Save Df as a .csv file
    df.to_csv('C:/CYBV474_Adv_Python/PandaDataFrame_KristinSkipper-WK-2.csv', index=False)

