# userid: berkj
# Email: jacob.berk@vanderbilt.edu
# Assignment Number: assignment1
# Honor statement: I pledge on my honor that I have neither given nor
#  received unauthorized aid on this assignment.
# Exercise 9:

# Import the datadotworld module as dw and the sys module
import datadotworld as dw
import sys

# Import a dataset
refugee_dataset = dw.load_dataset('nrippner/refugee-host-nations')

# Get the size of the dataset:
sys.getsizeof(refugee_dataset)

# List all of the data files:
dataframes = refugee_dataset.dataframes
for df in dataframes:
    pp.pprint(df)

# print all of the files in a dataset:
resources = refugee_dataset.describe()['resources']
pp.pprint('name:')
for r in resources:
    pp.pprint(r['name'])
pp.pprint('\ntype of file:')
for r in resources:
    pp.pprint(r['format'])
