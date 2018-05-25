df_qte = pd.read_csv('data/quote.csv')
df_qte.columns = ['Index', 'Timestamp', 'BidPrice', 'BidSize', 'AskPrice', 'AskSize']
df_qte = df_qte.drop(columns='Index')
df_qte['Timestamp'] = pd.to_datetime(df_qte['Timestamp'])
df_qte = df_qte.set_index('Timestamp', drop=True)
df_qte.head()