
import pandas as pd
import numpy as np
import sys as sys
sys.path.append("..\\..\..\\")
import multiple_regression_random_initialisation as mregress

input_csv = "ExampleTwo_SimpleFork_U1_Noise_NetworkValues_butU1deleted.csv"
counter = 0 
while counter < 1:
    regression_parameters = mregress.multi_regress_from_csv_2(input_csv, \
        threshold=0.00001, random = 2, max_iter = 10, learning_rate = 0.01)

    if "all_regression_out_parameters" in locals():
        all_regression_out_parameters = np.append(all_regression_out_parameters,\
                                             regression_parameters, axis=0)
    else:
        all_regression_out_parameters = regression_parameters
    counter += 1
print("all_regression_parameters: \n", all_regression_out_parameters)