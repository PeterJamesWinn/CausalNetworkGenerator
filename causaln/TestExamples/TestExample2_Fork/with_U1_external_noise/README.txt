
Data for fork junction X<-B->Y with unknown/unobservable noise, U1,  added to X . I.e. U1->X<-B->Y

U1, U2, and B are randomly selected as a value between 1 to 16. 100 data points were generated

ExampleTwo_SimpleFork_U1_Noise_NetworkParameters* - record of the values used by the network in .csv and .txt format. 

Inputs Data:
ExampleTwo_SimpleFork_U1_Noise_NetworkValues.csv -  The data, generated with ../TestExampleTwo_Fork_WithU1U2_ExternalNoise.ipynb
ExampleTwo_SimpleFork_U1_Noise_NetworkValues_butU1deleted.csv - as above but with the columns for U1 and U2 deleted, so that it could be submitted to the regression script without needing to change the script. 

Scripts:
data_analysis_noisy_data.ipynb
multipleRegresion_withoutU1.py - regression on X, Y, B, with each in turn as the dependent variable, using my own scripts steepest gradient descent algorithm, starting from random parameters
multipleRegresion_withoutU1_scikitLearn.ipynb - as above but using scikit learn
pairwise_regression.ipynb - every pair of X, Y, B.  outputs in the notebook. 
multiple_regression_without_U1_scikitLearn.ipynb


Output Data:
correlation.* each on each pairwise correlation data saved in three formats, .html, .csv, .txt
slope.* slopes from each on each pairwise regression : .html, .csv, .txt
intercept.* intercept, as per slope.* : .html, .csv, .txt

*_individual_scatter* - .pdf and .png of pairwise comparisons of the data as scatter plots
*_superposed_scatter* - all data on one scatter plot, with x-axis variable changing between plots. .pdf and .png




 