import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv( 'https://sololearn.com/uploads/files/titanic.csv' )

plt.scatter( df[ 'Age' ], df[ 'Fare' ] )
plt.xlabel( 'Age' )
plt.ylabel( 'Fare' )

plt.scatter( df[ 'Age' ], df[ 'Fare' ], c = df[ 'Pclass' ] )
plt.show()