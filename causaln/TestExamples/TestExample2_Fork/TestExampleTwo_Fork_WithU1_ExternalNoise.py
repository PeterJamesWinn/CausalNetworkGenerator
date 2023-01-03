# U1 -> X <-B -> Y

import pandas as pd
import sys, os
import numpy as np
sys.path.append('..\\..\\..\\') # to pick up network_generator.py
sys.path.append('..\\..\\')
import network_generator as ng
filestem = "ExampleTwo_SimpleFork_U1_Noise"

## 1.  Define network and converge.
## 1.1 Define nodes and network.
## 1.2 Evaluate and converge network values.
## 1.3 Write network values.
## 2.  Scan multiple values of B and U1
## 2.1 Scan values.


## 1.1a.  Define the nodes, their names and any initial values. Default value is 0
X = ng.Node("X", 1)
B = ng.Node("B", 5)
Y = ng.Node("Y")
U1 = ng.Node("U1")

## 1.1b. Define the connections that a node makes. 
# add_out_connection automatically also creats an add_in_connection 
# call on the recieving node.
# The below defines a simple network such that X<-B->Y, with U1 
# adding noise to X.
B.add_out_connection(X, 0.5)
B.add_out_connection(Y, 0.3)
U1.add_out_connection(X, 1)  # X := 0.5 B + U1

variable_to_scan = B
scan_range_lower = 1
scan_range_upper = 16

## 1.1c. defining the node list in the order of influence, X->B->Y means that the
# network values will be consistent after one evaluation of the network.
#
node_list = [X, B, Y, U1]
network = ng.NetworkInstance(node_list)

# 2.  Select multiple pseudo-random values of B, U1.
## 2.1 Scan values.
scan_range_lower = 1  # lowest value in scan range
scan_range_upper = 16 # highest value in scan range.
scanned_data_list = []  # where the data from multiple scans is to be stored.
for count in range(100): # number of values to be sampled
    seed = count
    U1.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
    seed = (scan_range_upper + 1 ) * (count + 1) # seed needs to be different 
                                    # or U1 and U2 will end up with same value
                    
                                    # A more sophisticated implementation
                                    # would derive seed value based on 
                                    # current time? or some similar. 
    seed = (scan_range_upper + 4 ) * (count + 1) # seed needs to be different
    B.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
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

# Write network parameters to file, including last converged values. 
network.write_network_parameters(filestem+"_NetworkParameters.txt")  
network_parameters_frame=network.make_network_parameters_dataframe()
network_parameters_frame.to_csv(
                                filestem+"_NetworkParameters.csv",
                                index=False,
                                na_rep='None')

column_names = network.list_of_node_names()  
network_values_dataframe = pd.DataFrame(scanned_data_list, columns=column_names)
network_values_dataframe.to_csv(
                                filestem+"_NetworkValues.csv",
                                index=False,
                                na_rep='None')  