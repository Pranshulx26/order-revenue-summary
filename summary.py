import pandas as pd 


def load_clean(path):
    if path.endswith('.xlsx'):
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    bad = (df['price'].isnull()) | df['qty'].isnull()
    #cleaned = df.copy()
    cleaned = df[~bad].copy()
    assert len(cleaned) == len(df) - len(bad), f"expected {len(df) - len(bad)} clean rows"

    cleaned['revenue'] = cleaned['price'] * cleaned['qty']
    return df, df[bad], cleaned 



def revenue_by_channel(clean):
    return clean.groupby('channel')['revenue'].sum()


def main(path):
    df, dropped, cleaned = load_clean(path)
    assert cleaned["revenue"].notna().all(), 'The dataframe contains null values'
    assert len(cleaned) + len(dropped) == len(df)
    print('Number of Dropped Rows: ',len(dropped))
    print(dropped['order_id'])

    print('Total Revenue: ', cleaned['revenue'].sum())
    print('Per Channel Revenue: ')
    per_channel_rev = revenue_by_channel(cleaned)
    print(per_channel_rev)


if __name__ == '__main__':
    main('orders.csv')
    main('clean_orders.xlsx')


