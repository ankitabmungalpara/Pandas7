"""

Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key (column with unique values) of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.

The result format is in the following example.

 
Example 1:

Input: 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+
Output: 
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+
Explanation: The orders with delivery id 2 and 3 are immediate while the others are scheduled.

"""

# This function calculates the percentage of food delivery orders that were delivered on the customer's preferred date.  
# It first compares the 'order_date' and 'customer_pref_delivery_date' columns to identify immediate deliveries.  
# The proportion of such immediate orders is then computed and returned as a DataFrame with the percentage rounded to two decimal places.  


import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    # method 1:
  
    immediate_order_series = delivery['order_date'] == delivery['customer_pref_delivery_date']
    immediateCount = immediate_order_series.sum()
    return pd.DataFrame([round(immediateCount / len(delivery) * 100, 2)], columns=['immediate_percentage'])

    # method 2:
  
    is_valid = delivery['order_date'] == delivery['customer_pref_delivery_date']
    
    # Count the number of valid (immediate) orders and the number of all orders.
    valid_count = is_valid.sum()
    total_count = len(delivery)

    # Round the percentage to 2 decimal places.
    percentage = round(100 * valid_count / total_count, 2)

    df = pd.DataFrame({'immediate_percentage': [percentage]})
    return df
  
