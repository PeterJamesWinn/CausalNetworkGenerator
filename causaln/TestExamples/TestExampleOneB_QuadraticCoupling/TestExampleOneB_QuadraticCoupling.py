

import pandas as pd
import sys, os
sys.path.append('..\\..\\')
from network_generator import *


# Define the connections that a node makes. 
# add_out_connection automatically also creats an add_in_connection 
# call on the recieving node.
#
# The below defines a simple network such that X->B->Y 
# such that initially defining the value of X propagates through 
# to define the values
# of B and y.
X = Node("X", 5)
B = Node("B", 1)
Y = Node("Y")
X.add_out_connection(B, (0.5, quadratic))
B.add_out_connection(Y, (0.5, linear))

# defining the node list in the order of influence, X->B->Y means that the
# network values with be consistent after one evaluation of the network.
node_list = [X, B, Y]
network2 = NetworkInstance(node_list)
print("network instance defined: X B Y , quadratic, linear")
network2.evaluate_network()
network2.converge_network()
network2_dataframe = network2.make_network_parameters_dataframe()
print(network2_dataframe)

# block to iterate through values of X 
node_and_range = (X, range(1,16)) 
# defined as a tuple with the idea that a list of tuples could be passed
# to scan_parameters
data_from_scanningX = network2.scan_parameters(node_and_range)

# write scanned data to file
column_names = network2.list_of_node_names()  
network2_values_dataframe =  \
    pd.DataFrame(data_from_scanningX, columns=column_names)
network2_values_dataframe.to_csv(
                                "Example1B_Quadratic_NetworkValues.csv",
                                index=False,
                                na_rep='None')

# Write network parameters to file, including last converged values. 
network2.write_network_parameters("Example1B_NetworkParameters.txt")  
network2_parameters_frame=network2.make_network_parameters_dataframe()
network2_parameters_frame.to_csv(
                                "Example1B_NetworkParameters.csv",
                                index=False,
                                na_rep='None')

# Add noise to the data. We're going to do that three times here,  
# too few to bother with a loop, to increase the data set size.
standard_deviation_scale = 0.1 # standard deviation of gaussian noise
                               # will be standard_deviation_scale * mean 
                               # of data column.
data_array = add_noise_to_data_sd_data_scaled(data_from_scanningX, standard_deviation_scale)
data_array = np.concatenate([data_array, 
    add_noise_to_data_sd_data_scaled(data_from_scanningX, standard_deviation_scale)], axis = 0 )
data_array = np.concatenate([data_array, 
    add_noise_to_data_sd_data_scaled(data_from_scanningX, standard_deviation_scale)], axis = 0 )

# Alternative possible coding using list
#data_list = add_noise_to_data(data_from_scanningX, add_gaussian_noise, standard_deviation)
#data_list = data_list + add_noise_to_data(data_from_scanningX, add_gaussian_noise, standard_deviation)
#data_list = data_list + add_noise_to_data(data_from_scanningX, add_gaussian_noise, standard_deviation)
#standard_deviation = 2
#data_list = []
#data_list_row = []
#for row in data_from_scanningX:
#    for value in row:        
#        data_list_row.append(add_gaussian_noise(value, standard_deviation))
#    data_list.append(data_list_row)
#    data_list_row = []


# write scanned data to file
#column_names = network2.list_of_node_names()  
network2_values_dataframe = \
    pd.DataFrame(data_array, columns=column_names)
network2_values_dataframe.to_csv(
                                "Example1B_Quadratic_NetworkValues_noisy.csv",
                                index=False,
                                na_rep='None')