import pandas as pd


def load_clean(path):
    # Load the file
    if path.endswith('.xlsx'):
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path)

    # Convert numeric columns
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    # Identify invalid rows
    bad = df['price'].isna() | df['qty'].isna()

    # Separate dropped and cleaned rows
    dropped = df[bad].copy()
    cleaned = df[~bad].copy()

    # Validate row counts
    assert len(cleaned) == len(df) - len(dropped), \
        "Cleaned row count does not match expected count"

    assert len(cleaned) + len(dropped) == len(df), \
        "Total row count does not match original row count"

    # Calculate revenue
    cleaned['revenue'] = cleaned['price'] * cleaned['qty']

    return dropped, cleaned


def revenue_by_channel(clean):
    return clean.groupby('channel')['revenue'].sum()


def main(path):
    dropped, cleaned = load_clean(path)

    assert cleaned['revenue'].notna().all(), \
        'The dataframe contains null revenue values'

    print('\nFile:', path)
    print('Number of Dropped Rows:', len(dropped))
    print('Dropped Order IDs:')
    print(dropped['order_id'])

    print('\nTotal Revenue:', cleaned['revenue'].sum())

    print('\nPer Channel Revenue:')
    per_channel_rev = revenue_by_channel(cleaned)
    print(per_channel_rev)


if __name__ == '__main__':
    main('orders.csv')
    main('clean_orders.xlsx')