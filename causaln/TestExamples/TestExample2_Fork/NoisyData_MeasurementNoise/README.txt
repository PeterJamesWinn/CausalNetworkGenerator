Data for fork junction X<-B->Y
No unknown/unobserval external nodes adding noise, but Gaussian noise added at nodes to represent observational error. 
B varies from 1 to 15, in one step increments. Noise added to the data set 13 times, to give 13 times 15 observations of X, Y and B.

Inputs Data:
ExampleTwo_SimpleFork_NetworkValues_noisy.csv -  The data, generated with ../TestExampleTwo_Fork.ipynb

Scripts:
data_analysis_noisy_data.ipynb

Output Data:
correlation.* each on each pairwise correlation data saved in three formats, .html, .csv, .txt
slope.* slopes from each on each pairwise regression : .html, .csv, .txt
intercept.* intercept, as per slope.* : .html, .csv, .txt

*_individual_scatter* -  .pdf and .png of pairwise comparisons of the data as scatter plots
*_superposed_scatter* - all data on one scatter plot, with x-axis variable changing between plots. .pdf and .png




 