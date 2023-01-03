import pandas as pd
import matplotlib.pyplot as plt

def all_against_all__individual_scatter(input_file_name, 
        output_file_stem="output"):
    '''
    For the data in a .csv file scatter plot all the data against the first 
    column, each pair on a different pair of axes, but all graphs
    next to each other on the same the same plot, 
    and then all the data against the second column, each pair on 
    a different set of axes,
    and so on. 

    Plots to .png and .pdf formats. 
    '''
    #input_file_name = "Example1_3_node_chain_NetworkValues.csv"
    #output_file_name = "Example1_AllPlots_part_"
    data_frame = pd.read_csv(input_file_name)
    outer_loop_index = 1  # for naming the different ouput files
    for (column_name,column_data) in data_frame.iteritems():
        #print(data_frame.shape[1])
        fig, axes = plt.subplots(1, data_frame.shape[1], 
            sharex=True, sharey=True)
        fig.set_facecolor("white")
        inner_loop_index = 0 
        for (comparison_column_name,comparison_column_data)  \
               in data_frame.iteritems():
            axes[inner_loop_index].scatter(column_data, \
                comparison_column_data, color="black")
            print(column_name, comparison_column_name)
            axes[inner_loop_index].set_xlabel(column_name, color="red")
            axes[inner_loop_index].set_ylabel(comparison_column_name, \
                color="red")
            axes[inner_loop_index].yaxis.set_tick_params(labelsize=15)
            axes[inner_loop_index].yaxis.set_tick_params(labelsize=15)
            
            inner_loop_index += 1
        fig.savefig(output_file_stem + str(outer_loop_index) + '.pdf')
        fig.savefig(output_file_stem + str(outer_loop_index) + '.png')
        outer_loop_index += 1

def one_plot(input_file_name, output_file_stem="output"):
    '''
    For the data in a .csv file line plot all the data against the first 
    column, all the same plot, 
    and then all the data against the second column, 
    and so on. 

    Plots to .png and .pdf formats. 
    '''
    #input_file_name = "Example1_3_node_chain_NetworkValues.csv"
    #output_file_name = "Example1_AllPlots_part_"
    data_frame = pd.read_csv(input_file_name)
    plot = data_frame.plot(xlabel = data_frame.columns[0])
    plot = data_frame.plot()
    fig = plot.get_figure()
    fig.set_facecolor("white")
    fig.savefig(output_file_stem + ".png")

def all_against_all__superposed_scatter(input_file_name, \
        output_file_stem = "output"):
    '''
    For the data in a .csv file scatter plot all the data
    against the first  column, on the same plot, and then all the data 
    against the second column, and so on. 

    Plots to .png and .pdf formats. 
    '''
    #input_file_name = "Example1_3_node_chain_NetworkValues.csv"
    #output_file_stem = "Example1_Scatter_Superposed_part_"

    print("output file name stem: ", output_file_stem)
    data_frame = pd.read_csv(input_file_name)
    outer_loop_index = 1  # for naming the different ouput files
    for (column_name,column_data) in data_frame.iteritems():
        inner_loop_index = 0 
        for (comparison_column_name,comparison_column_data) \
                in data_frame.iteritems():
            plt.scatter(column_data, comparison_column_data, 
                label = comparison_column_name)
            plt.xlabel(column_name, color="black")
            plt.legend()
            print(column_name, comparison_column_name)
            inner_loop_index += 1
        plt.savefig(output_file_stem + str(outer_loop_index)+'.pdf')
        plt.savefig(output_file_stem + str(outer_loop_index)+'.png')
        plt.show()
        outer_loop_index += 1
