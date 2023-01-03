
Files used by the UnitTest file for comparison:
temp
check_print_node_data

temp needs a better name!

All unit tests are in unit_test.py - which uses relative paths to find the network_generator code etc. 
unit_test_post_PIP_install.py is the same as unit_test.py excepting that it is set to run post a pip install of 
the causaln package and finds network_generator via the command from causaln.network_generator import *;
better would have been import causaln.network_generator as ng, but I think it's clear that all tests are on code 
containged in network_generator.py.  