
import pandas as pd
import sys, os
sys.path.append('..\\..\\') # to pick up network_generator.py
from network_generator import *
filestem = "ExampleTwo_SimpleFork"


## 1.  Define network and converge.
## 1.1 Define nodes and network.
## 1.2 Evaluate and converge network values.
## 1.3 Write network values.
## 2.  Scan multiple values of X and then add noise.
## 2.1 Scan values.
## 2.2 Write noise free values to file.
## 2.3 Add noise multiple times.
## 2.4 Write noisy values to file.

## 1.1a.  Define the nodes, their names and any initial values. Default value is 0
X = Node("X", 1)
B = Node("B", 5)
Y = Node("Y")

## 1.1b. Define the connections that a node makes. 
# add_out_connection automatically also creats an add_in_connection 
# call on the recieving node.
# The below defines a simple network such that X->B->Y 
# such that initially defining the value of X propagates through 
# to define the values of B and y.
B.add_out_connection(X, 0.5)
B.add_out_connection(Y, 0.3)
variable_to_scan = B
scan_range_lower = 1
scan_range_upper = 16

# X.PrintNodeData()
# B.PrintNodeData()
# Y.PrintNodeData()
# X.PrintNodeData()

## 1.1c. defining the node list in the order of influence, X->B->Y means that the
# network values will be consistent after one evaluation of the network.
node_list = [X, B, Y]
network = NetworkInstance(node_list)
network.evaluate_network_linear()
network.converge_network_linear()
network_dataframe = network.make_network_parameters_dataframe()
print(network_dataframe)

## 2.1 block to iterate through values of X 
node_and_range = (variable_to_scan, range(scan_range_lower, scan_range_upper)) 
# node_and_range defined as a tuple with the idea that a list of tuples 
#could be passed to scan_parameters, to scan multiple parameters at once.
data_from_scanningX = network.scan_parameters_linear(node_and_range)

## 2.2 write scanned data to file
column_names = network.list_of_node_names()  
network1_values_dataframe = pd.DataFrame(data_from_scanningX, columns=column_names)
network1_values_dataframe.to_csv(
                                filestem+"_NetworkValues.csv",
                                index=False,
                                na_rep='None')

# Write network parameters to file, including last converged values. 
network.write_network_parameters(filestem+"_NetworkParameters.txt")  
network_parameters_frame=network.make_network_parameters_dataframe()
network_parameters_frame.to_csv(
                                filestem+"_NetworkParameters.csv",
                                index=False,
                                na_rep='None')

## 2.3 add noise.
##

# Add noise to the data. We're going to do that thirteen times here,  
# too few to bother with a loop, to increase the data set size.
standard_deviation_scale = 0.1 # standard deviation of gaussian noise
                               # will be standard_deviation_scale * mean 
                               # of data column.

data_array = add_noise_to_data_sd_data_scaled(data_from_scanningX, 
                                              standard_deviation_scale)
for i in range(12): # add twelve more noisy copies of the data
    data_array = np.concatenate([data_array, add_noise_to_data_sd_data_scaled(
                                data_from_scanningX, standard_deviation_scale)],
                                axis = 0 )



# write scanned data to file
network2_values_dataframe = \
    pd.DataFrame(data_array, columns=column_names)
network2_values_dataframe.to_csv(
                                filestem+"_NetworkValues_noisy.csv",
                                index=False,
                                na_rep='None')
