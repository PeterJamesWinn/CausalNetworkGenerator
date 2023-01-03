# CausalAndBayesianNetworks

A project to generate causally linked nodes. I.e. nodes where the value of one node affects the value of another node, with the nodes creating a network. 
Different data values for the nodes can then be generated to produce a data set for investigating statistical confounding effects, causal colliders, the effects of conditioning on specific variables to mitigate confounding effects, and to better understand do-calculus for causal inference (see e.g. Dana Mackenzie and Judea Pearl's Book of Why for an introduction to the field). 


The EvaluateNetwork() call has initially been written to give a node the value of the sum of all incoming nodes, but future 
iterations of the code would allow for more complex relationships. 

The code currently defines functions, classes and methods to generate networks.

The examples (see relevent subsection below) are all written with relative paths 
If pip install  has been run in the CausalNetworkGeneratorPackage directory (i.e. the directory above this)
using "pip install ."
then the code can be imported into standard python usage, but the examples/test scripts will need
to be modified as described in the Tests and Examples section, below. Most tests/exmples are set to 
execute within the directory tree using relative paths to load the classes/methods/procedures.
The plan is to modify the examples in the near future. 
To pip uninstall: pip uninstall causaln

Files
-----------
README.md --- this file!

The main code 
---------------
network_generator.py - the main project! Allows the user to quickly define a causal network and calculate data 
                       sets based on the defined causal relationships. See TestExamples directory for examples of usage.
                       In Brief. 1. Define one of more nodes e.g. import network_generator as ng; X = ng.Node("X", 5) creates a node called X with a bias value of 5. 
		       X.add_out_connection(B, 0.5) creates a connection from node X to node B, such that the value of B is,  B = 0.5 X.
		       The network is then defined as an object containing the nodes: network1 = ng.NetworkInstance(node_list)
		       and the values are then propagated through the network until they are self consistent. I.e. every node in the network 
		       is visited in turn and evaluated, and, after completing a visit to every node, this is repeated again until nothing changes. 

Tests and Examples
-----------------------
The test and example files are currently implemented to run within this directory tree structure. 
To run outside the directory tree e.g. 
import network_generator as ng
would need to be replaced with 
import causaln.network_generator as ng 
(assuming pip install  has been run in the CausalNetworkGeneratorPackage directory)

TestExamples/  - example scripts and outputs covering network definition, data generation and data analysis. 
               - these example scripts used for testing the auxilliary data analysis scripts 
UnitTests/ - directory includes UnitTest script that has tests for the basic classes/methods for creating the network.
 

Auxilliary Scripts for data analysis
--------------------------------------
calculate_multiple_regression.py  
     - multi_regress_from_csv() - takes a csv as input, iterates through each column in turn, regressing it against all other comlumns, 
      returning results to stdout. Calls  multi_regress_from_dataframe(), which calls scikit learn
     - multi_regress_from_dataframe() - as multi_regress_from_csv but takes a Pandas dataframe, calls scikit learn. 

calculate_write_pairwise_regression.py - read .csv file and calculate pairwise regression analysis comparing every pair of columns.

multiple_regression_random_initialisation.py - 
      - multi_regress_from_csv_2() like multi_regress_from_csv() from calculate_multiple_regression.py but uses 
      a random initial value of the parameters and steepest gradient descent for optimisation. Needs refactoring, including a better name! 
      Example scripts would all need changing if name changed etc. 

plot_data.py - reads .csv file and plots the data colums against each other, depending on the function called:
        all_against_all__individual_scatter(input_file_name, - output_file_stem="output")  every data column against every other data column, pairwise, and then presented as one figure.
	one_plot(input_file_name, output_file_stem="output") - all data against the first column, on one pair of axes, represented as points an lines. Not much use for large data sets. 
	all_against_all__superposed_scatter(input_file_name, output_file_stem = "output") - all data plotted against the first column, all on the same pair of axes, then all against the second column etc. 

scan_1D_of_network_add_noise.py -   
    scans one variable of the network between the values scan_range_lower and
    scan_range_upper. Adds noise to the converged data set and writes out the
    clean and noisy data to two different files, aswell as files with network
    parameters.

