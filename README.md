# Causal Network Generator

A project to generate causally linked nodes. I.e. nodes where the value of one node affects the value of another node, with the nodes creating a network. Different data values for the nodes can then be generated to produce a data set for investigating statistical confounding effects, causal colliders, the effects of conditioning on specific variables to mitigate confounding effects, and to better understand do-calculus for causal inference (see e.g. Dana Mackenzie and Judea Pearl's Book of Why for an introduction to the field, or these six posts on Medium: https://medium.com/@peterjameswinn/introduction-to-causal-inference-328559924791). 

pip install . 
in the top directory (i.e. the one containing this file) will make the classes/methods/procedures available in your Python script, however most of the examples are all written with relative paths and will need to be modified as described in the Tests and Examples section of the causaln/README.md file. Further details about the code and examples can be found in the same file.
