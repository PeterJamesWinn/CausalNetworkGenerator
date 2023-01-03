import pandas as pd
import sys, os
sys.path.append('..\\..\\') # to pick up network_generator.py
from network_generator import *

def scan_1D_of_network_add_noise(node_list, variable_to_scan, scan_range_lower,
        scan_range_upper, filestem):
    '''
    scans one variable of the network between the values scan_range_lower and
    scan_range_upper. Adds noise to the converged data set and writes out the
    clean and noisy data to two different files, aswell as files with network
    parameters.
    '''
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

    # write scanned data to file
    network2_values_dataframe = \
        pd.DataFrame(data_array, columns=column_names)
    network2_values_dataframe.to_csv(
                                    filestem+"_NetworkValues_noisy.csv",
                                    index=False,
                                    na_rep='None')