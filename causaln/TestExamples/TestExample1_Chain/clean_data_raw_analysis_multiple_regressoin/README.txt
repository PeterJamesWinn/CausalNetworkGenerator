Data for chain junction X->B->Y with no noise added, not Gaussian observational noise, nor external unknown variable noise. 
No Gaussian noise. B varies 1 to 15, with X and Y calculated appropriately. 
Multiple regression for every combination, i.e. X against B and Y; B against X and Y; Y against B and X.

Input Data:
Example1_3_node_chain_NetworkValues.csv -  The data, generated with an edited version of ../TestExampleOne_CreateNetworkAndData_XBY.py

Data Analysis Scripts:
*.ipynb - Jupyter notebooks - multiple regression with scikit learn, which always converges to one set of 
                         parameters even when the system is undetermined, and using my own code that has different pseduo random starting 
                         points in parameter space and optimises with steepest gradient descent. 

Output Data:
in the Jupyter notebooks. 




 