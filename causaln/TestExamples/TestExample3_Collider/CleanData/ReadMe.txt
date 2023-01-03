
TestExample3_Collider_XBY_clean_and_measurement_noise.py - generates the next three files listed below.
ExampleThree_Collider_NetworkValues.csv - contains the data
ExampleThree_Collider_NetworkParameters.csv - contains the network parameters used to generate the data.
ExampleThree_Collider_NetworkParameters.txt - contains the network parameters used to generate the data.
PairwiseRegression - directory with script to perform pairwise regression and associated output files.
StratifiedAnalysis - directory with scripts to perform stratified analysis of the data. 
multipleRegression_scikitLearn.ipynb  - jupyter notebook: multiple regression with each variable, in turn, as the dependent. Here, really only interested in B = ... 
multiple_regression_random_initialisations.ipynb: jupyter notebook: showing that, for this data, the regression only coverges to one solution, which is what you would expect, since X, Y and intercept are not collinear. 