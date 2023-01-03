
Data for fork junction X<-B->Y with unknown/unobservable noise, U1, U2, added to X and Y, respectively. I.e. U1->X<-B->Y<-U2

U1, U2, and B are randomly selected as a value between 1 to 16. 5000 data points were generated

ExampleTwo_SimpleFork_U1U2Noise_NetworkParameters* - record of the values used by the network in .csv and .txt format. 

Inputs Data:
ExampleTwo_SimpleFork_U1U2Noise_NetworkValues.csv -  The data, generated with ../TestExampleTwo_Fork_WithU1U2_ExternalNoise.ipynb
ExampleTwo_SimpleFork_U1U2Noise_NetworkValues_butU1U2deleted.csv - as above but with the columns for U1 and U2 deleted, so that it could be submitted to the regression script without needing to change the script. 

Scripts:
data_analysis_noisy_data.ipynb
multipleRegresion_withoutU1U2.py - regression on X, Y, B, with each in turn as the dependent variable, using my own scripts steepest gradient descent algorithm, starting from random parameters
multipleRegresion_withoutU1U2_scikitLearn.ipynb - as above but using scikit learn
pairwise_regression_withoutU1U2.ipynb - every pair of X, Y, B.  outputs in the notebook.  Didn't run the script for plotting the data. 


Output Data:
correlation.* each on each pairwise correlation data saved in three formats, .html, .csv, .txt
slope.* slopes from each on each pairwise regression : .html, .csv, .txt
intercept.* intercept, as per slope.* : .html, .csv, .txt





 