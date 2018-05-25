df_right = pd.merge(df_currency, df_forex, on='Currency', how='left')
df_right