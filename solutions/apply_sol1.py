df_bond['Price'] = df_bond.apply(
    lambda row: np.npv(
        rate=row['yield'],
        values=[row['2017_cashflow'],
                row['2018_cashflow'],
                row['2019_cashflow'],
                row['2020_cashflow']]),
    axis=1)

df_bond