#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

def clean_and_validate(raw_records):
    """
    Processes a list of dictionaries, applying specific cleaning and 
    validation rules for sales data.
    """
    total_parsed = 0
    invalid_count = 0
    valid_records = []

    for record in raw_records:
        # 1. Skip Empty Lines
        if not any(value.strip() for value in record.values()):
            continue
            
        total_parsed += 1
        is_valid = True

        try:
            # 2. Validate TransactionID - Must start with 'T'
            tid = record.get('TransactionID', '')
            if not tid.startswith('T'):
                is_valid = False

            # 3. Check for Missing CustomerID or Region
            if not record.get('CustomerID') or not record.get('Region'):
                is_valid = False

            # 4. Clean Numeric Values (Remove commas)
            # Handle Quantity
            raw_qty = record.get('Quantity', '0').replace(',', '')
            qty = int(raw_qty)
            
            # Handle UnitPrice
            raw_price = record.get('UnitPrice', '0').replace(',', '')
            price = float(raw_price)

            # 5. Remove if Quantity <= 0 or UnitPrice <= 0
            if qty <= 0 or price <= 0:
                is_valid = False

            if is_valid:
                # 6. Clean ProductName - Remove internal commas
                clean_name = record.get('ProductName', '').replace(',', '')
                
                # Update record with cleaned data
                record['ProductName'] = clean_name
                record['Quantity'] = qty
                record['UnitPrice'] = price
                
                valid_records.append(record)
            else:
                invalid_count += 1

        except (ValueError, TypeError):
            # Handles cases where conversion to int/float fails
            invalid_count += 1

    # 7. Required Validation Output
    print(f"Total records parsed: {total_parsed}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {len(valid_records)}")

    return valid_records

def calculate_metrics(clean_data):
    """
    Optional helper to perform analysis on the cleaned dataset.
    """
    metrics = {
        'total_revenue': sum(row['Quantity'] * row['UnitPrice'] for row in clean_data),
        'transaction_count': len(clean_data)
    }
    return metrics


# In[ ]:




