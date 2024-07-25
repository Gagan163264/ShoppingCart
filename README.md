# Shopping Cart Cost Splitter

This Python script calculates and splits the cost of a shopping cart among multiple people. It reads the cart information from a text file and applies any discounts specified. The script can handle percentage-based discounts and fixed amount discounts, distributing the cost appropriately among the people involved.

## Features

- **File Input**: Reads shopping cart data from a specified file.
- **Discount Handling**: Supports percentage and fixed amount discounts.
- **Cost Splitting**: Distributes costs among multiple people.
- **Validation**: Ensures valid input data for calculations.
- **Detailed Output**: Provides a breakdown of costs for each person.

## Usage

1. **Prepare the Input File**:
   - The first line should be the number of people sharing the cost.
   - The second line (optional) can specify a discount in one of the following formats:
     - `conv_fee-discount%` for percentage discounts (e.g., `10-5%` for a 5% discount with a $10 conversion fee).
     - `discount#` for fixed amount discounts (e.g., `50#` for a $50 discount).
   - The remaining lines specify the items in the format `persons-item-price`, where `persons` is a string of initials of the people sharing that item, `item` is the item name, and `price` is the cost (e.g., `AB-apples-30` for apples costing $30 shared between A and B).

2. **Run the Script**:
   ```bash
   python script.py [optional_cart_file_name]
