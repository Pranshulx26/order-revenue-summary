# Order Revenue Summary

A Python-based project that reads order data from a CSV file, processes the records, and generates a revenue summary across different sales channels.

## Features

- Loads order data from `orders.csv`.
- Handles CSV data and converts numeric fields into appropriate data types.
- Identifies and skips rows containing invalid numeric values using try and except (TypeError and ValueError).
- Calculates and displays total revenue.
- Calculates revenue for each sales channel.
- Identifies the channel with the highest revenue.

## How to Run

### 0. Install uv
```bash
pip install uv
```

### 1. Clone the Repository

```bash
git clone https://github.com/Pranshulx26/order-revenue-summary.git
```

### 2. Navigate to the Project Directory

```bash
cd order-revenue-summary
```

### 3. Run the Application

```bash
uv run main.py
```

## Sample Output

```text
Skipping Bad Row: {'order_id': '6', 'channel': 'Amazon', 'price': 'abc', 'qty': '2'}
Skipping Bad Row: {'order_id': '7', 'channel': 'Amazon', 'price': '500', 'qty': None}
Total Revenue : 5844
Channel : Amazon | Revenue : 1895
Channel : Myntra | Revenue : 3299
Channel : Flipkart | Revenue : 650
Top Channel: Myntra (3299)
```

## Key Learnings

Through this project, I learned:

- **CSV File Handling:** How to read and process CSV files using Python's built-in `csv` module and pandas library.
- **Data Type Conversion:** Understanding that CSV data is initially read as strings and learning how to convert numeric fields into integers and in pandas it can be handled using pd.to_numeric(col, errors='coerce') and pd.dropna() method.
- **Exception Handling:** Using `try-except` blocks to handle invalid data and skip malformed records without interrupting program execution and how to use assert statements to throw inline exceptions and something doesn't work as expected.
- **Code Reusability:** I created a function that calculates the total revenue and if ever there is need to change the formula i only need to change in this function and it's reflected else where.
- **Dictionary Operations:** Using Python dictionaries to aggregate revenue by sales channel.
- **Data Aggregation:** Calculating total revenue, revenue by channel, and identifying the highest-performing sales channel.



---

**Project:** Order Revenue Summary  
**Author:** [Pranshulx26](https://github.com/Pranshulx26)