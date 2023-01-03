# prints to screen/stdout the regression of each variable in the csv file
# with every other variable in the csv file. Coefficient values are 
# in the same order as the output list of independent names of the variables
import sys 
sys.path.append('..\\..\\..\\') # to pick up regression module.
#import multiple_regression_random_initialisation as mregress
import calculate_multiple_regression as cmr
input_csv = "ExampleTwo_SimpleFork_U1Noise_NetworkValues_butU1deleted.csv"
cmr.multi_regress_from_csv(input_csv) 