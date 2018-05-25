df_left = pd.merge(df_prices, df_turnovers)  # on=['Underlying', 'Month'] is optional
df_left['Notional'] = df_left['Price'] * df_left['Turnover']
df_left