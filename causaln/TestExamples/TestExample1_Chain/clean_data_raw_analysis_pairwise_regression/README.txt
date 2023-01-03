Data for chain junction X->B->Y with no noise added, not Gaussian observational noise, nor external unknown variable noise. 
No Gaussian noise. B varies 1 to 15, with X and Y calculated appropriately. 
Analysis is the regression of every pair of observables, i.e. XB, XY, BY. 

Input Data:
Example1_3_node_chain_NetworkValues.csv -  The data, generated with an edited version of ../TestExampleOne_CreateNetworkAndData_XBY.py

Data Analysis Scripts:
data_analysis_script.ipynb - Jupyter notebook

Output Data:
correlation.* each on each pairwise correlation data saved in three formats, .html, .csv, .txt
slope.* slopes from each on each pairwise regression : .html, .csv, .txt
intercept.* intercept, as per slope.* : .html, .csv, .txt

*_individual_scatter* -  .pdf and .png of pairwise comparisons of the data as scatter plots
*_superposed_scatter* - all data on one scatter plot, with x-axis variable changing between plots. .pdf and .png




 