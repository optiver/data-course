# Using loc
df.loc['Wednesday', 'volatility']

# Using iloc
df.iloc[2, 2]

# Using a combination of labels and locations
df.loc['Wednesday', df.columns[2]]
df.loc[df.index[2], 'volatility']
