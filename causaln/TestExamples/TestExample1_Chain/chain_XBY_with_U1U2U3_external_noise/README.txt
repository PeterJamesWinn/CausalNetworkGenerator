Data for chain junction X->B->Y with U1, U2, U3, providing random noise feeding into X, B and Y, respectively
No Gaussian noise. B, U1, U2, U3 vary 1 to 15, with X and Y calculated appropriately. 



Input Data:
.csv -  The data, generated with an edited version of ../TestExampleOne_CreateNetworkAndData_U1XU2BU3Y.py

Scripts:
multipleRegression_scikitLearn.ipynb  - does what it says!
data_analysis_noise_free_set.ipynb 

Output Data:
correlation.* each on each pairwise correlation data saved in three formats, .html, .csv, .txt
slope.* slopes from each on each pairwise regression : .html, .csv, .txt
intercept.* intercept, as per slope.* : .html, .csv, .txt

*_individual_scatter* -  .pdf and .png of pairwise comparisons of the data as scatter plots
*_superposed_scatter* - all data on one scatter plot, with x-axis variable changing between plots. .pdf and .png




 