df = pd.merge(df_left, df_right, on='Underlying', how='left')
df['Notional'] = df['Notional'] / df['Rate'] / 1e6
df