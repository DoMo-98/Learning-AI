import pandas as pd

df = pd.read_csv( 'https://sololearn.com/uploads/files/titanic.csv' )

# The head method returns the first 5 rows of the DataFrame.
print( df.head() )

# The describe method returns a table of statistics about the columns.
print( df.describe() )

# To select a single column, we use the square brackets and the column name.
# It returns a Pandas Series
fare = df[ 'Fare' ]
print( fare )

# To select multiple columns from our original DataFrame, creating a smaller DataFrame.
selected_columns = [ 'Age', 'Sex', 'Survived' ]
small_df = df[ selected_columns ]
print( small_df.head() )

# We create a Pandas Series that will be a series of Trues and Falses (True if the passenger is male and False if the passenger is female).
male = df['Sex'] == 'male'
# To create a new column
df['male'] = male
print( df.head() )

# ----------------------------------------------------------------------------------
#                                   Numpy part
# ----------------------------------------------------------------------------------

# The values attribute of a Pandas Series give the data as a numpy array.
print( df['Fare'].values )

# The values attribute of a Pandas DataFrame give the data as a 2d numpy array.
print( df.values )
selected_columns = [ 'Pclass', 'Fare', 'Age' ]
print( df[ selected_columns ].values )

# Use the shape attribute to find the number of rows and number columns for a Numpy array.
# You can also use the shape attribute on a pandas DataFrame (df.shape).
arr = df[ selected_columns ].values
print( arr.shape )
print( df.shape )

# Using different syntax within brackets, we can select single values, a whole row or a whole column.
print( arr[ 0, 1 ] )
print( arr[ 0 ] )
print( arr[ :, 2 ] )

# A mask is a boolean array (True/False values) that tells us which values from the array we’re interested in.
# In this example, we'll select all the rows of children (passengers under the age of 18).
mask = arr[ :, 2 ] < 18
print( arr[ mask ] )
print( arr[ arr[ :, 2 ] < 18 ] )

# Summing an array of boolean values gives the count of the number of True values.
# To know how many passengers, under the age of 18, are
print( mask.sum() )
print( ( arr[ :, 2 ] < 18 ).sum() )