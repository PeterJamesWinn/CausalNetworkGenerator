
import pandas as pd
import sys, os
sys.path.append('..\\..\\..') # to pick up network_generator.py
from network_generator import *
from scan_1D_of_network_add_noise import *
filestem = "ExampleThree_Collider"

## 1.  Define network and converge.
## 1.1 Define nodes and network.
## 1.2 Evaluate and converge network values.
## 1.3 Write network values.
## 2.  Scan multiple values of X and Y then add noise.
## 2.1 Scan values.
## 2.2 Write noise free values to file.
## 2.3 Add noise multiple times.
## 2.4 Write noisy values to file.

## 1.1a.  Define the nodes, their names and any bias values. Default 
# value is 0.  For nodes without incoming connections their bias will 
# become their value. 
X = Node("X")
B = Node("B", 5) # B = 0.5 X + 0.3 Y  +5
Y = Node("Y")

## 1.1b. Define the connections that a node makes. 
# add_out_connection automatically also creats an add_in_connection 
# call on the recieving node.
# The below defines a simple network such that X->B->Y 
# such that initially defining the value of X propagates through 
# to define the values of B and y.
X.add_out_connection(B, 0.5)
Y.add_out_connection(B, 0.3)  #B = 0.5 X + 0.3 Y  +5

## 1.1c. Define node list and network instance
# defining the node list in the order of influence, X->B<-Y means 
# that the
# network values will be consistent after one evaluation of the network.
node_list = [X,  Y, B]
network = NetworkInstance(node_list)

## 1.2 Evaluate and converge network values.
network.evaluate_network_linear()
network.converge_network_linear()
network_dataframe = network.make_network_parameters_dataframe()
print(network_dataframe)

## 1.3  Write network parameters to file, including last converged values. 
network.write_network_parameters(filestem+"_NetworkParameters.txt")  
network_parameters_frame=network.make_network_parameters_dataframe()
network_parameters_frame.to_csv(
                                filestem+"_NetworkParameters.csv",
                                index=False,
                                na_rep='None')

## 2.  Scan multiple values of X and Y then add noise.
## 2.1 Scan values.
scan_range_lower = 1  # lowest value in scan range
scan_range_upper = 16 # highest value in scan range.
scanned_data_list = []  # where the data from multiple scans is to be stored.
for count in range(32): # number of values to be sampled
    seed = count
    X.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
    seed = (scan_range_upper + 1 ) * count # seed needs to be different 
                                    # or X 
                                    # and Y will end up with same value
                                    # A more sophisticated implementation
                                    # would derive seed value based on 
                                    # current time? or some similar. 
    Y.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
    network.evaluate_network_linear()
    network.converge_network_linear()
    data_list_row = []
    for node in network.network_node_list:
        print(node)
        data_list_row.append(node.node_value)
        print("data_list_row: ", data_list_row)
    scanned_data_list.append(data_list_row)
    data_list_row = []
    print("scanned_data_list: ", scanned_data_list)


## 2.2 Write noise free values of scanned data to file.
column_names = network.list_of_node_names()  
network_values_dataframe = pd.DataFrame(scanned_data_list, columns=column_names)
network_values_dataframe.to_csv(
                                filestem+"_NetworkValues.csv",
                                index=False,
                                na_rep='None')


## 2.3 Add noise multiple times.
# Add noise to the data. We're going to do that fifteen times here,  
# too few to bother with a loop, to increase the data set size.
standard_deviation_scaling = 0.1 # standard deviation of gaussian noise
                            # will be standard_deviation_scale * mean 
                            # of data column.

data_array = add_noise_to_data_sd_data_scaled(scanned_data_list, 
                                              standard_deviation_scaling)
for i in range(14): # add 14 more noisy copies of the data
    data_array = np.concatenate([data_array, add_noise_to_data_sd_data_scaled(
                              scanned_data_list, standard_deviation_scaling)],
                                axis = 0 )



## 2.4 Write noisy values to file.
# write scanned data to file
network2_values_dataframe = \
    pd.DataFrame(data_array, columns=column_names)
network2_values_dataframe.to_csv(
                                filestem+"_NetworkValues_noisy.csv",
                                index=False,
                                na_rep='None')       
