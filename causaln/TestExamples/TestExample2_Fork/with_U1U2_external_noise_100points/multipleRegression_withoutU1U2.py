
import sys 
sys.path.append('..\\..\\..\\') # to pick up regression module.
import multiple_regression_random_initialisation as mregress
import pandas as pd
import numpy as np



input_csv = "ExampleTwo_SimpleFork_U1U2Noise_NetworkValues_butU1U2deleted.csv"
counter = 0 
while counter < 2:
    regression_parameters = mregress.multi_regress_from_csv_2(input_csv, \
        threshold=0.00001, random = 1, max_iter = 5000, learning_rate = 0.01)
    if "all_regression_out_parameters" in locals():
        all_regression_out_parameters = np.append(all_regression_out_parameters,\
                                          regression_parameters, axis=0)
    else:
        all_regression_out_parameters = regression_parameters
    counter += 1
print("all_regression_parameters: \n", all_regression_out_parameters)