# userid: berkj
# Email: jacob.berk@vanderbilt.edu
# Assignment Number: assignment1
# Honor statement: I pledge on my honor that I have neither given nor
#  received unauthorized aid on this assignment.
# Exercise 4:

# The datadotworld module and dataset have already been loaded for you:
import datadotworld as dw
dataset = dw.load_dataset('https://data.world/stephen-hoover/chicago-city-council-votes')

# Use the dataframes property to assign the alderman_votes table to the variable votes_dataframe.
votes_dataframe = dataset.dataframes['alderman_votes']

# Use the pandas shape property to get rows/columns size for the `votes_dataframe` dataframe.
pp.pprint(votes_dataframe.shape)

# Use the pandas head function to print the first 3 rows of the `votes_dataframe` dataframe.
pp.pprint(votes_dataframe.head(3))
