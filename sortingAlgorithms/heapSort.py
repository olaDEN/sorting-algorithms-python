
import pandas as pd

# Calling data frame constructor 
df = pd.DataFrame()

# list of string 
friends = [{'name': 'Rachel', 'Year': '1969'},{'name': 'Ross', 'Year': '1966'},{'name': 'Joey', 'Year': '1967'},{'name': 'Monica', 'Year': '1964'}]

# Calling DataFrame constructor on list 
df = pd.DataFrame(friends)

print(df.sort_values(by='Year',
kind='heapsort')) # the built-in sort_values() uses merge sort algorithm
print('\n')
print(df.sort_values(by='name',
kind='heapsort'))