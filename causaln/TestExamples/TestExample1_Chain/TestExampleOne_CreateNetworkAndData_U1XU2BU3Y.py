# Generating data for the network U1XU2BU3Y
import pandas as pd
import sys, os
sys.path.append('..\\..\\') 
sys.path.append('..\\..\\..\\..\\') # to pick up network_generator.py
import network_generator as ng
filestem = "ExampleOne_Chain_U1XU2BU3Y"


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
U1 = ng.Node("U1")
U2 = ng.Node("U2")
U3 = ng.Node("U3")

## 1.1b. Define the connections that a node makes. 
# add_out_connection automatically also creats an add_in_connection 
# call on the recieving node.
# The below defines a simple network such that X->B->Y and U1->X; U2->B
# U3 -> Y
# such that initially defining the value of X propagates through 
# to define the values of B and y.
U1.add_out_connection(X, 1)
X.add_out_connection(B, 0.5)
U2.add_out_connection(B, 1)
B.add_out_connection(Y, 0.5)
U3.add_out_connection(Y, 1)

# X.PrintNodeData()
# B.PrintNodeData()
# Y.PrintNodeData()
# X.PrintNodeData()

## 1.1c. defining the node list in the order of influence, X->B->Y means that the
# network values will be consistent after one evaluation of the network.
node_list = [X, B, Y, U1, U2, U3]
network = ng.NetworkInstance(node_list)

## 1.2 Evaluate and converge network values.
network.evaluate_network_linear()
network.converge_network_linear()
network_dataframe = network.make_network_parameters_dataframe()
print(network_dataframe)

## 1.3 
# Write network parameters to file, including last converged values. 
network.write_network_parameters("Example1_3_node_chain_NetworkParameters_withU1U2U3_external_noise.txt")  
network_parameters_frame=network.make_network_parameters_dataframe()
network_parameters_frame.to_csv(
                                "Example1_3_node_chain_NetworkParameters_withU1U2U3_external_noise.csv",
                                index=False,
                                na_rep='None')


# 2.  Select multiple pseudo-random values of X, U1, U2, U3.
## 2.1 Scan values.
scan_range_lower = 1  # lowest value in scan range
scan_range_upper = 16 # highest value in scan range.
scanned_data_list = []  # where the data from multiple scans is to be stored.
for count in range(20000): # number of values to be sampled
    seed = count
    U1.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
    seed = (scan_range_upper + 1 ) * (count + 1) # seed needs to be different 
                                    # or U1 and U2 will end up with same value
                    
                                    # A more sophisticated implementation
                                    # would derive seed value based on 
                                    # current time? or some similar. 
    U2.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
    seed = (scan_range_upper + 4 ) * (count + 1) # seed needs to be different
    U3.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
    seed = (scan_range_upper + 6 ) * (count + 1) # seed needs to be different
    X.random_int_value_bias(scan_range_lower, scan_range_upper, seed)
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


print("\n --------------------- \nData for node Y")
Y.print_node_data()
