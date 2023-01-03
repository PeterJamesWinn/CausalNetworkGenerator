

'''
Calculate multiple regression, every variable described as a 
function of all other variables.
Iterate column by column for every column against 
Calculation results returned to stdout. 
'''

from sklearn import linear_model
import pandas as pd

def multi_regress_from_csv(filename):
    '''Regress one column against all other columns in a csv file, 
    iterating to include every column in turn as the dependent variable'''
    data_frame = pd.read_csv(filename)
    multi_regress_from_dataframe(data_frame)

def multi_regress_from_dataframe(dataframe):
    '''Regress one column against all other columns in a csv file, 
    iterating to include every column in turn as the dependent variable'''
    data_frame = dataframe
    slope_list = []
    intercept_list = []
    correlation_list = []
    p_list = []
    std_err_list = []
    key_list = []
    data_names = []
    
    for (column_name,column_data) in data_frame.iteritems():
        dependent_data = column_data
        dependent_name = column_name
        data_names.append(dependent_name)
        slope_row_data = []
        key_row_data = []
        intercept_row_data = []
        correlation_row_data = []
        p_row_data = []
        std_err_row_data = []

        independent_data = data_frame.loc[:, data_frame.columns != column_name]
        print("dependent name: ", dependent_name)
        independent_names = list(data_frame.loc[:, data_frame.columns != column_name])
        print("independent names: ", independent_names)
        # with sklearn
        regression_model = linear_model.LinearRegression()
        regression_model.fit(independent_data, dependent_data)

        print('Intercept: \n', regression_model.intercept_)
        print('Coefficients: \n', regression_model.coef_)
