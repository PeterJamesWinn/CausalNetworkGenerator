
# Game 5 from Chapter 4 (Confounding and Deconfounding ...) 
# of The Book of Why.  

from network_generator_2 import *


A = Node("A", 5)
B = Node("B")
C = Node("C", 1)
Y = Node("Y")
X = Node("X")

A.add_out_connection(B, (0.5, linear))
A.add_out_connection(X, (0.5, linear))
B.add_out_connection(X, (0.5, linear))
C.add_out_connection(B, (0.5, linear))
C.add_out_connection(Y, (0.5, linear))
X.add_out_connection(Y, (0.5, linear))

# node_list = [A, C, B, X, Y]:  giving nodes in this order leads to
# convergence in the first iteration, since a node is only visited
# once the nodes on which it is dependent has been visited. 
# Any other order is a suboptimal order but network converges for this
# topology on second pass.
node_list = [A, B, Y, X, C]
network = NetworkInstance(node_list)
network.evaluate_network()
network_dataframe_game5 = network.make_network_dataframe()
print(network_dataframe_game5)
network.converge_network()
network_dataframe_game5 = network.make_network_dataframe()
print(network_dataframe_game5)
network_dataframe_game5.to_csv(
    "NetworkParameters_game5.csv",
    index=False,
    na_rep='None')
