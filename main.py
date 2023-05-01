# fixed no.s
# start_date = "2021-01-01"
# end_date = "2023-04-30"
# min_total_sales_range = 19.04
# max_total_sales_range = 175.91
# total_sales_average = 42.50
# repeat_customer_avg = 2.3
# total_rows = int(input("Enter the total rows of data for generation: "))

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_fake_transactions(start_date, end_date, min_total_sales_range, max_total_sales_range, total_sales_average, repeat_customer_avg, total_rows):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    
    dates = []
    customer_ids = []
    total_sales = []
    
    unique_customer_ids = total_rows // repeat_customer_avg
    
    for _ in range(total_rows):
        random_date = start_date + (end_date - start_date) * random.random()
        dates.append(random_date.strftime(date_format))
        
        random_customer_id = random.randint(1, unique_customer_ids)
        customer_ids.append(random_customer_id)
        
        random_total_sale = total_sales_average + np.random.uniform(min_total_sales_range, max_total_sales_range)
        total_sales.append(round(random_total_sale, 2))
    
    data = {'day': dates, 'customer_id': customer_ids, 'total_sales': total_sales}
    df = pd.DataFrame(data)
    
    df.to_csv('fake_transactions.csv', index=False)
    print("CSV file generated successfully.")

start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
min_total_sales_range = float(input("Enter the minimum total sales range for generation: "))
max_total_sales_range = float(input("Enter the maximum total sales range for generation: "))
total_sales_average = float(input("Enter the total sales average for generation: "))
repeat_customer_avg = int(input("Enter the average number of repeated customer_id for generation: "))
total_rows = int(input("Enter the total rows of data for generation: "))

generate_fake_transactions(start_date, end_date, min_total_sales_range, max_total_sales_range, total_sales_average, repeat_customer_avg, total_rows)