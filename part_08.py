# userid: berkj
# Email: jacob.berk@vanderbilt.edu
# Assignment Number: assignment1
# Honor statement: I pledge on my honor that I have neither given nor
#  received unauthorized aid on this assignment.
# Exercise 8:

# datadotworld module has been imported as dw
import datadotworld as dw

# We've written a SPARQL query for you and assigned it to the `sparql_query` variable:
sparql_query = "PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/> SELECT ?FName ?LName WHERE {?person GOT:col-got-house \"Stark\" . ?person GOT:col-got-fname ?FName . ?person GOT:col-got-lname ?LName .}"

# Use the pre-defined SPARQL query to query dataset http://data.world/tutorial/sparqltutorial and return the results to a queryResults variable
queryResults = dw.query('http://data.world/tutorial/sparqltutorial', sparql_query, query_type='sparql')

# Use the dataframe property of the resulting query to create a dataframe variable named `houseStark`
houseStark = queryResults.dataframe

# Use pp.pprint() to print the dataframe to the screen.
pp.pprint(houseStark)
