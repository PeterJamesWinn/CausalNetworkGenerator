
import pandas as pd
import sys
import numpy as np
sys.path.append('..\\..\\') # to pick up network_generator.py
import network_generator as ng

## 1.  Define network and converge.
## 1.1 Define nodes and network.
## 1.2 Evaluate and converge network values.
## 1.3 Write network values.
## 2.  Scan multiple values of X and then add noise.
## 2.1 Scan values.
## 2.2 Write noise free values to file.
## 2.3 Add noise multiple times.
## 2.4 Write noisy values to file.

## 1.1a. Define the nodes, their names and any bias values. Default value 
# is 0.  For nodes without incoming connections their bias
#  will become their value.
X = ng.Node("X", 5)
B = ng.Node("B", 1)
Y = ng.Node("Y")

## 1.1b. Define the connections that a node makes. 
# add_out_connection automatically also creats an add_in_connection 
# call on the recieving node.
# The below defines a simple network such that X->B->Y 
# such that initially defining the value of X propagates through 
# to define the values of B and y.
X.add_out_connection(B, 0.5)
B.add_out_connection(Y, 0.5)

# X.PrintNodeData()
# B.PrintNodeData()
# Y.PrintNodeData()
# X.PrintNodeData()

## 1.1c. defining the node list in the order of influence, X->B->Y means that the
# network values will be consistent after one evaluation of the network.
node_list = [X, B, Y]
network1 = ng.NetworkInstance(node_list)

## 1.2 Evaluate and converge network values.
network1.evaluate_network_linear()
network1.converge_network_linear()
network1_dataframe = network1.make_network_parameters_dataframe()
print(network1_dataframe)

## 1.3 
# Write network parameters to file, including last converged values. 
network1.write_network_parameters("Example1_3_node_chain_NetworkParameters.txt")  
network1_parameters_frame=network1.make_network_parameters_dataframe()
network1_parameters_frame.to_csv(
                                "Example1_3_node_chain_NetworkParameters.csv",
                                index=False,
                                na_rep='None')


## 2.1 block to iterate through values of X 
node_and_range = (X, range(1,16)) 
# node_and_range defined as a tuple with the idea that a list of tuples 
#could be passed to scan_parameters, to scan multiple parameters at once.
data_from_scanningX = network1.scan_parameters_linear(node_and_range)

## 2.2 write scanned data to file
column_names = network1.list_of_node_names()  
network1_values_dataframe = pd.DataFrame(data_from_scanningX, columns=column_names)
network1_values_dataframe.to_csv(
                                "Example1_3_node_chain_NetworkValues.csv",
                                index=False,
                                na_rep='None')



print("\n --------------------- \nData for node B")
B.print_node_data()

## 2.3 add noise.
##

# Add noise to the data. We're going to do that six times here,  
# too few to bother with a loop, to increase the data set size.
standard_deviation_scale = 0.1 # scaling standard deviation of gaussian noise
                               # will be standard_deviation_scale * mean 
                               # of data column.

data_array = ng.add_noise_to_data_sd_data_scaled(data_from_scanningX, 
                                              standard_deviation_scale)
for i in range(6): # add five more noisy copies of the data
    data_array = np.concatenate([data_array, ng.add_noise_to_data_sd_data_scaled(
                                data_from_scanningX, standard_deviation_scale)],
                                axis = 0 )
    data_array = np.concatenate([data_array, ng.add_noise_to_data_sd_data_scaled(
                                data_from_scanningX, standard_deviation_scale)], 
                                axis = 0 )

# write scanned data to file
network2_values_dataframe = \
    pd.DataFrame(data_array, columns=column_names)
network2_values_dataframe.to_csv(
                                "Example1_3_node_chain_NetworkValues_noisy.csv",
                                index=False,
                                na_rep='None')
