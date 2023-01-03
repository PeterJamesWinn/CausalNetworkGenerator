# for stratified analysis of data
import pandas as pd

# read data into pandas frame.
input_file = "ExampleThree_Collider_NetworkValues.csv"
collider_data_frame = pd.read_csv(input_file)
print(collider_data_frame)
#print(collider_data_frame.head())

values = collider_data_frame.loc[collider_data_frame["B"] < 8.6]
print(values)
sorted = collider_data_frame.sort_values(by='B')

print(sorted)
values.plot(x='X', y='Y', kind='scatter')