
import csv
NUMERIC_FIELDS = ('order_id', 'price', 'qty')

def load_orders(path):
    orders = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = {}
            try:
                for key, val in row.items():
                    if key in NUMERIC_FIELDS:
                        d[key] = int(val)
                    else:
                        d[key] = val

                orders.append(d)

            except (ValueError, TypeError):
                print(f"Skipping Bad Row: {row}")
                continue

    return orders 

def line_total(order):
    return order['price'] * order['qty']



def total_revenue(orders):

    revenue = 0
    for order in orders:
        revenue += line_total(order)
    return revenue 

def revenue_by_channel(orders):
    rev_by_channel = {}

    for order in orders:
        channel = order['channel']
        rev_by_channel[channel] = rev_by_channel.get(channel, 0) + line_total(order)

    return rev_by_channel



def top_channel(totals):
    best = max(totals.items(), key=lambda x: x[1])

    return best

def main(orders):
    print(f'Total Revenue : {total_revenue(orders)}')
    rev_per_channel = revenue_by_channel(orders)
    for key, val in rev_per_channel.items():
        print(f'Channel : {key} | Revenue : {val}')

    name, amount = top_channel(rev_per_channel)
    print(f"Top Channel: {name} ({amount})")




if __name__ == "__main__":
    orders = load_orders('orders.csv')
    main(orders)

