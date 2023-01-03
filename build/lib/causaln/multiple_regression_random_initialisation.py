'''
code to read a .csv and for each column in turn perform a multiple 
regression with respect to all the other columns. Uses random 
initialisation and steepest gradient descent.
The code works but needs refactoring 
'''

import pandas as pd
import numpy as np

def multi_regress_from_csv_2(filename, threshold=0.001, random = 1, \
    max_iter = 0, learning_rate = 0.01):
    '''
    Regresses one column against all other columns in a csv file, 
    iterating to include every column in turn as the dependent variable.
    max_iter = 0 implies no restriction on number of iterations, otherwise
    the value is the maximum number of gradient descent steps.
    random = 1 - use random starting values of the parameters
    random = 0 - use the average gradient as starting parameter values, 
    intercept 0.
    Threshold, value of mean squared error below which to stop optimising
    '''
    data_frame = pd.read_csv(filename)
    
    for (column_name, column_data) in data_frame.iteritems():
        dependent_data = column_data
        dependent_name = column_name
        # independent data is every column except the one selected by this 
        # iteration of the for loop.
        independent_data = data_frame.loc[:, data_frame.columns != column_name] 
        independent_names = list(data_frame.loc[:, data_frame.columns != \
            column_name])
        #print("dependent name: ", dependent_name, "independent names: ", \
        #    independent_names)
        print(f"Calling Regression with threshold = {threshold}, random = \
            {random}, max_iter = {max_iter}")
        regression_out_parameters = regress(independent_data, dependent_data, \
            threshold, random, max_iter, learning_rate)
        r_squared = calculate_r_squared(regression_out_parameters, independent_data, dependent_data)
        #print("r_squared", r_squared)
        # Get create a numpy array with names identifying the parameters.
        # Insert new column name to indentify the intercept
        independent_names.insert(0, "intercept") 
        independent_names = np.array(independent_names)
        independent_names = np.expand_dims((independent_names), axis=1)
        independent_names = np.transpose(independent_names)
        # columns names to the parameter array - except transpose so to rows.
        regression_out_parameters = np.transpose(regression_out_parameters)
        regression_out_parameters = np.append(independent_names,regression_out_parameters, axis=0)
        regression_out_parameters = np.append(regression_out_parameters, [["r_squared "], [r_squared]], axis=1)
        # save to final store so don't overwrite on next iteration
        if  "all_regression_out_parameters" in locals():
            all_regression_out_parameters = np.append(all_regression_out_parameters, np.array([["  ", "  ",]]) ,axis = 0)
            all_regression_out_parameters = np.append(all_regression_out_parameters, np.array([["dependent", dependent_name]]) ,axis = 0)
        else:
            all_regression_out_parameters = np.array([["  ", "  "]])
            all_regression_out_parameters = np.append(all_regression_out_parameters, np.array([["dependent", dependent_name]]) ,axis = 0)
        all_regression_out_parameters = np.append(all_regression_out_parameters,  np.transpose(regression_out_parameters), axis=0)      
        #print("all_regression_out_parameters", all_regression_out_parameters)
    return all_regression_out_parameters

def calculate_r_squared(regression_parameters,independent_data,dependent_data):
    number_of_training_examples = independent_data.shape[0]
    independent_data = np.append(np.ones((number_of_training_examples,1)), \
        independent_data, axis=1)
    Y = np.expand_dims(dependent_data, axis=1)
    Y_hat = np.dot(independent_data, regression_parameters)
    sum_squares_residuals = mse(Y, Y_hat, number_of_training_examples)
    total_sum_squares = np.var(Y)
    r_squared = 1 - (sum_squares_residuals/total_sum_squares)
    return r_squared

# loss function aka error function:
def mse(y, y_hat, number_of_training_examples): 
  '''Calculate the mean squared error (mse) loss: (y_hat - y)squared. 
  y_hat is the estimate from the network, 
  y is the ground truth.'''
  return np.sum(np.square(y_hat - y), axis=0)/number_of_training_examples

def mse_gradient(Y, X, Y_hat, number_of_training_examples):
  '''gradient of mse: mean squared error loss: (y_hat - y). y_hat 
  is the estimate from the network, 
  y is the ground truth.'''
  return 0.5*np.sum(np.multiply((Y_hat - Y),X), axis=0)/number_of_training_examples

def regress(independent_data, dependent_data, threshold=0.9, random = 1, max_iter = 0, learning_rate = 0.005):
    #add column of ones, for the intercept, shape independent_data.shape[0],1
    #print("in regress function")
    column_length = independent_data.shape[0]
    independent_data = np.append(np.ones((column_length,1)), independent_data, axis=1)
    Y = np.expand_dims(dependent_data, axis=1)
    parameter_count = np.shape(independent_data[1])[0]
    #print("parameter count", parameter_count)
    
    # random initialisation or comparison to mean gradient and set intercept 0.
    print("random, ", random) 
    if random == 1:
        print("using pseudo random initial parameter values.")
        parameters = np.random.random((parameter_count,1))
    elif random == 0:
        print("setting initial parameters using gradient estimates.")
        grad = []
        for grad_count in range(parameter_count):
            # estimate the gradients
            delta_dependent = np.max(dependent_data) - np.min(dependent_data)
            grad.append((np.max(independent_data[grad_count]) \
                 - np.min(independent_data[grad_count])) /delta_dependent)
            grad_count += 1  
            #print("grad_count, ", grad_count)
        parameters = np.append(np.array([0.0]),np.array(grad[1:]))
        Y = np.expand_dims(dependent_data, axis=1)
        parameters = np.expand_dims(parameters, axis = 1)
        #print("parameters, ", parameters)
    else:
        print("random should be 1 or 0. ", random, " is not a valid value.")
        exit()

    Y_hat = np.dot(independent_data, parameters)
    number_of_training_examples = Y.shape[0]
    error = mse(Y, Y_hat, number_of_training_examples)
    #print("mean squared error ", error)
    iterations = 0
    while  error > threshold:
        gradient = np.expand_dims(mse_gradient(Y, independent_data, Y_hat, \
            number_of_training_examples), axis=1)
        #print("gradient: \n", gradient) 
        parameters = parameters - learning_rate * gradient
        #print("parameters: \n", parameters)
        Y_hat = np.dot(independent_data, parameters)
        #print("Y_hat", Y_hat)
        error = mse(Y, Y_hat, number_of_training_examples)
        #print("mean squared error: ", error)
        if max_iter > 0:
            if iterations == max_iter:  break
        iterations += 1
        #print("End of iteration: ", iterations, " of ", max_iter, " iterations")
        
    return parameters

