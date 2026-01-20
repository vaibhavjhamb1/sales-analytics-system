#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

BASE_URL = "https://dummyjson.com/products"

def get_product_details(product_id):
    """
    Fetches a single product by ID from DummyJSON.
    Returns the JSON response or None if the request fails.
    """
    try:
        # Requirement: Get a SINGLE product by ID
        response = requests.get(f"{BASE_URL}/{product_id}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch product {product_id}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def search_products(query):
    """
    Search for products by name or category.
    """
    try:
        # Requirement: Search products
        response = requests.get(f"{BASE_URL}/search?q={query}")
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Search Error: {e}")
        return None


# In[2]:


import requests

def get_product_metadata(product_id):
    """
    Fetches details for a specific product by ID.
    Example: product_id '1' returns the 'iPhone 9' object.
    """
    url = f'https://dummyjson.com/products/{product_id}'
    
    try:
        # Requirement: Get a SINGLE product by ID
        response = requests.get(url)
        
        if response.status_code == 200:
            # Requirement: Returns single product object
            product = response.json()
            
            # Useful fields from the sample response:
            title = product.get('title')       # e.g., "iPhone 9"
            category = product.get('category') # e.g., "smartphones"
            brand = product.get('brand')       # e.g., "Apple"
            rating = product.get('rating')     # e.g., 4.69
            
            return product
        else:
            print(f"Error: Product {product_id} not found (Status: {response.status_code})")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return None


# In[3]:


import requests

BASE_URL = "https://dummyjson.com/products"

def get_limited_products(count=100):
    """
    Fetches a specific number of products from DummyJSON.
    Example: count=100 returns the first 100 product objects.
    """
    try:
        # Requirement: Get specific number of products using 'limit'
        response = requests.get(f"{BASE_URL}?limit={count}")
        
        if response.status_code == 200:
            data = response.json()
            # The JSON response contains 'products' (list) and 'total' (count)
            return data.get('products', [])
        else:
            print(f"Error: Unable to fetch products (Status: {response.status_code})")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return []


# In[4]:


import requests

def search_products(query):
    """
    Searches for products in the DummyJSON database matching the query string.
    
    Returns: A list of product dictionaries.
    """
    base_url = "https://dummyjson.com/products/search"
    params = {'q': query} # Requirement: Use 'q' parameter for searching
    
    try:
        # Requirement: GET request to the search endpoint
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            # The 'products' key contains the list of all matching objects
            return data.get('products', [])
        else:
            print(f"Search failed with status: {response.status_code}")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"API Error during search: {e}")
        return []


# In[6]:


import requests

def fetch_all_products():
    """
    Fetches all products from DummyJSON API using a limit of 100.
    
    Returns: list of product dictionaries
    """
    url = "https://dummyjson.com/products?limit=100"
    
    try:
        # Requirement: Fetch all available products (use limit=100)
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Requirement: Print status message (success)
            print("Successfully fetched products from API.")
            
            # Extract data from the JSON response
            data = response.json()
            
            # The API returns an object with a 'products' key containing the list
            return data.get('products', [])
        else:
            # Requirement: Print status message (failure)
            print(f"Failed to fetch products. Status Code: {response.status_code}")
            return []
            
    except requests.exceptions.RequestException as e:
        # Requirement: Handle connection errors with try-except
        print(f"Error: Connection to API failed. {e}")
        # Requirement: Return empty list if API fails
        return []


# In[7]:


def create_product_mapping(api_products):
    """
    Creates a mapping of product IDs to product info for efficient lookup.

    Parameters: api_products from fetch_all_products()

    Returns: dictionary mapping product IDs to info
    """
    # Requirement: Return a dictionary mapping product IDs to info
    product_map = {}
    
    for product in api_products:
        # Requirement: Map the numeric 'id' to a dictionary of metadata
        product_id = product.get('id')
        
        # Requirement: Include title, category, brand, and rating
        product_map[product_id] = {
            'title': product.get('title'),
            'category': product.get('category'),
            'brand': product.get('brand'),
            'rating': product.get('rating')
        }
        
    return product_map


# In[9]:


import os

def save_enriched_data(enriched_transactions, filename='data/enriched_sales_data.txt'):
    """
    Saves enriched transactions back to file with all original and API fields.
    """
    # Requirement: Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Requirement: Define all original + new fields for the header
    headers = [
        'TransactionID', 'Date', 'ProductID', 'ProductName', 
        'Quantity', 'UnitPrice', 'CustomerID', 'Region',
        'API_Category', 'API_Brand', 'API_Rating', 'API_Match'
    ]
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Requirement: Write header with pipe delimiter
            f.write("|".join(headers) + "\n")
            
            for t in enriched_transactions:
                row_values = []
                for field in headers:
                    # Requirement: Handle None values appropriately
                    # Convert None to an empty string or "N/A" as per your preference
                    value = t.get(field)
                    if value is None:
                        row_values.append("")
                    else:
                        row_values.append(str(value))
                
                # Requirement: Use pipe delimiter for data rows
                f.write("|".join(row_values) + "\n")
                
        print(f"Successfully saved {len(enriched_transactions)} records to {filename}")
        
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")


# In[10]:


import os
from datetime import datetime

def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    """
    Generates a comprehensive formatted text report as per the final project requirements.
    """
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Pre-calculate data for the report
    total_rev = sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
    total_txns = len(transactions)
    avg_order = total_rev / total_txns if total_txns > 0 else 0
    dates = [t['Date'] for t in transactions]
    
    # 1. & 2. HEADER AND OVERALL SUMMARY
    report_lines = [
        "=" * 60,
        "           SALES ANALYTICS REPORT",
        f"        Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"        Records Processed: {total_txns}",
        "=" * 60,
        "\nOVERALL SUMMARY",
        "-" * 60,
        f"Total Revenue:       ₹{total_rev:,.2f}",
        f"Total Transactions:  {total_txns}",
        f"Average Order Value: ₹{avg_order:,.2f}",
        f"Date Range:          {min(dates)} to {max(dates)}",
    ]

    # 3. REGION-WISE PERFORMANCE
    # Note: Requires region_wise_sales function from previous modules
    region_stats = region_wise_sales(transactions) # Assuming function from Task 2.1b
    report_lines.extend(["\nREGION-WISE PERFORMANCE", "-" * 60])
    report_lines.append(f"{'Region':<12} {'Sales':<15} {'% Total':<12} {'Transactions'}")
    for reg, data in region_stats.items():
        report_lines.append(f"{reg:<12} ₹{data['total_sales']:<14,.0f} {data['percentage']:<12}% {data['transaction_count']}")

    # 4. TOP 5 PRODUCTS
    top_products = top_selling_products(transactions, n=5) # Assuming Task 2.1c
    report_lines.extend(["\nTOP 5 PRODUCTS", "-" * 60])
    report_lines.append(f"{'Rank':<6} {'Product Name':<20} {'Qty':<10} {'Revenue'}")
    for i, (name, qty, rev) in enumerate(top_products, 1):
        report_lines.append(f"{i:<6} {name:<20} {qty:<10} ₹{rev:,.2f}")

    # 5. TOP 5 CUSTOMERS
    customer_stats = customer_analysis(transactions) # Assuming Task 2.1d
    report_lines.extend(["\nTOP 5 CUSTOMERS", "-" * 60])
    report_lines.append(f"{'Rank':<6} {'Customer ID':<15} {'Spent':<15} {'Orders'}")
    top_customers = list(customer_stats.items())[:5]
    for i, (cid, data) in enumerate(top_customers, 1):
        report_lines.append(f"{i:<6} {cid:<15} ₹{data['total_spent']:<14,.2f} {data['purchase_count']}")

    # 6. DAILY SALES TREND
    trends = daily_sales_trend(transactions) # Assuming Task 2.2a
    report_lines.extend(["\nDAILY SALES TREND", "-" * 60])
    report_lines.append(f"{'Date':<15} {'Revenue':<15} {'Txns':<10} {'Unique Cust'}")
    for date, data in trends.items():
        report_lines.append(f"{date:<15} ₹{data['revenue']:<14,.2f} {data['transaction_count']:<10} {data['unique_customers']}")

    # 7. PRODUCT PERFORMANCE ANALYSIS
    peak_date, peak_rev, peak_txns = find_peak_sales_day(transactions) # Assuming Task 2.2b
    low_performers = low_performing_products(transactions) # Assuming Task 2.3a
    report_lines.extend(["\nPRODUCT PERFORMANCE ANALYSIS", "-" * 60])
    report_lines.append(f"Best Selling Day: {peak_date} (₹{peak_rev:,.2f} with {peak_txns} txns)")
    report_lines.append(f"Low Performing Products: {len(low_performers)} items found below threshold")

    # 8. API ENRICHMENT SUMMARY
    enriched_count = sum(1 for et in enriched_transactions if et.get('API_Match'))
    success_rate = (enriched_count / total_txns * 100) if total_txns > 0 else 0
    missing_ids = sorted(list(set(et['ProductID'] for et in enriched_transactions if not et.get('API_Match'))))
    
    report_lines.extend(["\nAPI ENRICHMENT SUMMARY", "-" * 60])
    report_lines.append(f"Total Products Enriched: {enriched_count}")
    report_lines.append(f"Success Rate:            {success_rate:.2f}%")
    report_lines.append(f"Not Enriched:            {', '.join(missing_ids) if missing_ids else 'None'}")

    # Write to file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(report_lines))
        print(f"Comprehensive report generated successfully at: {output_file}")
    except IOError as e:
        print(f"Error writing report to {output_file}: {e}")


# In[ ]:




