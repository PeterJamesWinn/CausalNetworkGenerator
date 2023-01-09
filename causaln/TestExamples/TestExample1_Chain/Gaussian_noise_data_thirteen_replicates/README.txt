Data for chain junction X->B->Y with Gaussian noise added to each observation. Noise is added after the network has 
been evaluated, so it is simulated error in measurement. B varies 1 to 15, with X and Y calculated appropriately. 
This was repeated 13 times to give 13 x 15 data points in total. 
Only calculating pairwise regression &  correlation; i.e. X with B; X with Y: B with Y.


Input Data:
Example1_3_node_chain_NetworkValues_noisy.csv -  The data, generated with an edited version of ../TestExampleOne_CreateNetworkAndData_XBY.py 13 iterations of the integer range 1 to 15, with Gaussian noise added, to make 195 unique points. 

Scripts:
data_analysis.ipynb 

Output Data:
correlation.* each on each pairwise correlation data saved in three formats, .html, .csv, .txt
slope.* slopes from each on each pairwise regression : .html, .csv, .txt
intercept.* intercept, as per slope.* : .html, .csv, .txt

*_individual_scatter* -  .pdf and .png of pairwise comparisons of the data as scatter plots
*_superposed_scatter* - all data on one scatter plot, with x-axis variable changing between plots. .pdf and .png




 