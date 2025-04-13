# How to use

Run without arguments, the program will ask for inputs

summary of inputs:

name of file: the name of the file you want to make, without the .txt at the end. The file will be created in the autoTestCases/ directory
number of nodes: the number of nodes you want e.g. 100
min x: minimum possible x value
max x: largest possible x value
min y: minimum possible y value
max y: largest possible y value
min edge cost: smallest possible cost of edge
max edge cost: largest possible cost of edge (the cost of an edge will be chosen by selecting a random number between min edge and max edge)
min edge amount per node: smallest number of edges coming OUT of a node
max edge amount per node: largest number of edges coming OUT of a node (a random number will be chosen for each node, between min and max again)
number of destinations: how many destinations you want
(origin will be chosen randomly)

NOTE: Little input validation has been implemented, invalid inputs may cause the program to hang or crash