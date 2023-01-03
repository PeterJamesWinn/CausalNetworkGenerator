
'''
calculate pairwise regression analysis comparing every pair of columns.
Iterate column by column for every column against 
every other column in a csv file and save in a dataframe.
Dataframe written to .tex, .csv, .html files. 
'''

from scipy import stats
import pandas as pd

def regress_from_csv(filename):
    '''All by all regression of the columns in a csv file.'''
    data_frame = pd.read_csv(filename)
    # initialise data storage lists
    slope_list = []
    intercept_list = []
    correlation_list = []
    p_list = []
    std_err_list = []
    key_list = []
    data_names = []

    # nested for loops for all against all comparison
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
        # if stdout_flag == true:
        # print to stdout stuff picked up in the next loop - 
        # next line provides the header for the output to stdout
        print("calculation_key, slope, intercept, r_value, p_value, std_err")
        for (comparison_column_name,comparison_column_data) in data_frame.iteritems():
            independent_data = comparison_column_data
            independent_name = comparison_column_name
            # scipy regression
            slope, intercept, r_value, p_value, std_err = \
                stats.linregress(independent_data, dependent_data)

            # if stdout_flag == true:
            # print to stdout stuff.
            calculation_key =  independent_name + dependent_name
            print(calculation_key, slope, intercept, r_value, p_value, std_err)
            
            #add to their row list for each output, slope, intercept ...
            slope_row_data.append(slope)
            key_row_data.append(calculation_key)
            intercept_row_data.append(intercept)
            correlation_row_data.append(r_value)
            p_row_data.append(p_value)
            std_err_row_data.append(std_err)
        # add row data to the full list for each slope, intercept etc. 
        slope_list.append(slope_row_data)
        key_list.append(key_row_data)
        intercept_list.append(intercept_row_data)
        correlation_list.append(correlation_row_data)
        p_list.append(p_row_data)
        std_err_list.append(std_err_row_data)
    # convert  to dataframes
    slope_dataframe = pd.DataFrame(slope_list)
    intercept_dataframe = pd.DataFrame(intercept_list)
    correlation_dataframe = pd.DataFrame(correlation_list)
    p_dataframe = pd.DataFrame(p_list)
    std_err_dataframe = pd.DataFrame(std_err_list)

    # Label columns/rows as Inpendent/Dependent variables.
    for dataframe in [slope_dataframe, intercept_dataframe, 
                     correlation_dataframe, p_dataframe, std_err_dataframe]:
        dataframe.columns = pd.MultiIndex.from_product([["Dependent"],
                                                       data_names])
        dataframe.index = pd.MultiIndex.from_product([["Independent"], 
                                                     data_names])
    return slope_dataframe, intercept_dataframe, correlation_dataframe, \
        p_dataframe, std_err_dataframe

def dataframe_to_html(dataframe, filename_stem):
    '''write dataframe to html file called filename_stem".html"'''
    html_filepointer = open(filename_stem+".html", "w")
    html_filepointer.write(dataframe.to_html())
    html_filepointer.close()

def dataframe_to_tex(dataframe, filename_stem):
    '''write dataframe to tex file called filename_stem".tex"''' 
    html_filepointer = open(filename_stem+".tex", "w")
    html_filepointer.write(dataframe.to_latex())
    html_filepointer.close()
        
def dataframe_to_csv(dataframe, filename_stem):
    '''write dataframe to .csv file called filename_stem".csv"''' 
    html_filepointer = open(filename_stem+".csv", "w")
    html_filepointer.write(dataframe.to_csv())
    html_filepointer.close()

