# Order Revenue Summary

A Python-based project that reads order data from a CSV file, processes the records, and generates a revenue summary across different sales channels.

## Features

- Loads order data from `orders.csv`.
- Handles CSV data and converts numeric fields into appropriate data types.
- Identifies and skips rows containing invalid numeric values.
- Calculates and displays total revenue.
- Calculates revenue for each sales channel.
- Identifies the channel with the highest revenue.

## How to Run

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

- **CSV File Handling:** How to read and process CSV files using Python's built-in `csv` module.
- **Data Type Conversion:** Understanding that CSV data is initially read as strings and learning how to convert numeric fields into integers.
- **Exception Handling:** Using `try-except` blocks to handle invalid data and skip malformed records without interrupting program execution.
- **Code Reusability:** Writing reusable functions to avoid code duplication and improve maintainability.
- **Dictionary Operations:** Using Python dictionaries to aggregate revenue by sales channel.
- **Data Aggregation:** Calculating total revenue, revenue by channel, and identifying the highest-performing sales channel.

## Technologies Used

- Python
- CSV Module
- UV (Python Package and Project Manager)

---

**Project:** Order Revenue Summary  
**Author:** [Pranshulx26](https://github.com/Pranshulx26)