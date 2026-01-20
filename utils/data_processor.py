#!/usr/bin/env python
# coding: utf-8

# In[1]:


def parse_transactions(raw_lines):
    """
    Parses raw lines into a list of dictionaries.
    Handles comma removal and type conversion.
    """
    keys = ['TransactionID', 'Date', 'ProductID', 'ProductName', 
            'Quantity', 'UnitPrice', 'CustomerID', 'Region']
    parsed_records = []
    
    for line in raw_lines:
        # Requirement: Split by pipe delimiter '|'
        values = [v.strip() for v in line.split('|')]
        
        # Requirement: Skip rows with incorrect number of fields
        if len(values) == len(keys):
            try:
                # Requirement: Handle commas within ProductName (remove commas)
                product_name = values[3].replace(',', '')
                
                # Requirement: Remove commas from numeric fields before conversion
                qty_str = values[4].replace(',', '')
                price_str = values[5].replace(',', '')
                
                # Requirement: Convert to proper types
                record = {
                    'TransactionID': values[0],
                    'Date': values[1],
                    'ProductID': values[2],
                    'ProductName': product_name,
                    'Quantity': int(qty_str),   # int type
                    'UnitPrice': float(price_str), # float type
                    'CustomerID': values[6],
                    'Region': values[7]
                }
                parsed_records.append(record)
            except ValueError:
                continue # Skip rows that fail numeric conversion
    return parsed_records

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates and applies filters.
    Prints the required 80/10/70 validation summary.
    """
    total_parsed = len(transactions)
    valid_records = []
    
    # Requirement: Filter Display - Print available info to user
    regions = sorted(list(set(t['Region'] for t in transactions)))
    print(f"Available regions: {regions}")
    
    for t in transactions:
        # Validation Rules:
        # - Quantity and UnitPrice must be > 0
        # - All required fields must be present
        # - TransactionID must start with 'T'
        # - ProductID must start with 'P'
        # - CustomerID must start with 'C'
        
        is_valid = (
            t['Quantity'] > 0 and 
            t['UnitPrice'] > 0 and
            t['TransactionID'].startswith('T') and
            t['ProductID'].startswith('P') and
            t['CustomerID'].startswith('C') and
            all(t.values()) # Ensure no fields are empty
        )
        
        if not is_valid:
            continue

        # Optional Filters


# In[2]:


def parse_transactions(raw_lines):
    """
    Parses raw lines into a list of dictionaries as per Task 1.2.
    """
    keys = ['TransactionID', 'Date', 'ProductID', 'ProductName', 
            'Quantity', 'UnitPrice', 'CustomerID', 'Region']
    parsed_records = []
    
    for line in raw_lines:
        # Requirement: Split by pipe delimiter '|'
        values = [v.strip() for v in line.split('|')]
        
        # Requirement: Skip rows with incorrect number of fields
        if len(values) == len(keys):
            try:
                # Requirement: Handle commas within ProductName
                product_name = values[3].replace(',', '')
                
                # Requirement: Remove commas from numeric fields for conversion
                qty_val = values[4].replace(',', '')
                price_val = values[5].replace(',', '')
                
                record = {
                    'TransactionID': values[0],
                    'Date': values[1],
                    'ProductID': values[2],
                    'ProductName': product_name,
                    'Quantity': int(qty_val),      # Convert to int type
                    'UnitPrice': float(price_val),  # Convert to float type
                    'CustomerID': values[6],
                    'Region': values[7]
                }
                parsed_records.append(record)
            except ValueError:
                # Skips records where numeric conversion fails
                continue
    return parsed_records

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates records and applies optional filters as per Task 1.3.
    """
    total_input = len(transactions)
    valid_transactions = []
    
    # Requirement: Display available info before filtering
    available_regions = sorted(list(set(t['Region'] for t in transactions)))
    amounts = [t['Quantity'] * t['UnitPrice'] for t in transactions]
    print(f"Available Regions: {available_regions}")
    print(f"Transaction Range: Min ${min(amounts):.2f}, Max ${max(amounts):.2f}")

    for t in transactions:
        # Requirement: Apply strict Validation Rules
        is_valid = (
            t['Quantity'] > 0 and                       # Quantity must be > 0
            t['UnitPrice'] > 0 and                      # UnitPrice must be > 0
            all(t.values()) and                         # All fields must be present
            t['TransactionID'].startswith('T') and      # ID must start with 'T'
            t['ProductID'].startswith('P') and          # Product must start with 'P'
            t['CustomerID'].startswith('C')             # Customer must start with 'C'
        )
        
        if not is_valid:
            continue

        # Optional Filtering Logic
        total_price = t['Quantity'] * t['UnitPrice']
        if region and t['Region'] != region:
            continue
        if min_amount and total_price < min_amount:
            continue
        if max_amount and total_price > max_amount:
            continue
            
        valid_transactions.append(t)

    # Requirement: Validation Output Required
    invalid_count = total_input - len(valid_transactions)
    print(f"\nTotal records parsed: {total_input}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {len(valid_transactions)}")
    
    return valid_transactions


# In[3]:


def parse_transactions(raw_lines):
    """
    Parses raw pipe-delimited strings into a structured list of dictionaries.
    Handles comma removal and data type conversion as required.
    """
    keys = ['TransactionID', 'Date', 'ProductID', 'ProductName', 
            'Quantity', 'UnitPrice', 'CustomerID', 'Region']
    parsed_records = []
    
    for line in raw_lines:
        # Split by pipe delimiter and strip hidden whitespace
        values = [v.strip() for v in line.split('|')]
        
        # Requirement: Skip rows with incorrect number of fields
        if len(values) == len(keys):
            try:
                # CLEAN: Remove commas within ProductName (e.g., Mouse,Wireless)
                product_name = values[3].replace(',', '')
                
                # CLEAN: Remove commas from numeric fields before conversion
                qty_str = values[4].replace(',', '')
                price_str = values[5].replace(',', '')
                
                # REQUIREMENT: Convert to int and float types
                record = {
                    'TransactionID': values[0],
                    'Date': values[1],
                    'ProductID': values[2],
                    'ProductName': product_name,
                    'Quantity': int(qty_str),
                    'UnitPrice': float(price_str),
                    'CustomerID': values[6],
                    'Region': values[7]
                }
                parsed_records.append(record)
            except ValueError:
                # Skip rows that fail numeric conversion
                continue
                
    return parsed_records

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates records against strict business rules and applies optional filters.
    """
    total_parsed = len(transactions)
    valid_transactions = []
    
    # Requirement: Filter Display - Print regions and range before filtering
    regions = sorted(list(set(t['Region'] for t in transactions)))
    amounts = [t['Quantity'] * t['UnitPrice'] for t in transactions]
    print(f"Available regions: {regions}")
    print(f"Transaction Range: Min ${min(amounts):.2f}, Max ${max(amounts):.2f}")
    
    for t in transactions:
        # VALIDATION RULES:
        # - Quantity and UnitPrice must be > 0
        # - TransactionID must start with 'T'
        # - ProductID must start with 'P'
        # - CustomerID must start with 'C'
        # - All required fields must be present
        
        is_valid = (
            t['Quantity'] > 0 and
            t['UnitPrice'] > 0 and
            t['TransactionID'].startswith('T') and
            t['ProductID'].startswith('P') and
            t['CustomerID'].startswith('C') and
            all(str(val).strip() != "" for val in t.values())
        )
        
        if not is_valid:
            continue

        # Optional Filters
        total_price = t['Quantity'] * t['UnitPrice']
        if region and t['Region'] != region:
            continue
        if min_amount and total_price < min_amount:
            continue
        if max_amount and total_price > max_amount:
            continue
            
        valid_transactions.append(t)

    # VALIDATION OUTPUT REQUIRED
    invalid_count = total_parsed - len(valid_transactions)
    print(f"\nTotal records parsed: {total_parsed}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {len(valid_transactions)}")
    
    return valid_transactions, invalid_count, {
        'total_input': total_parsed,
        'invalid': invalid_count,
        'final_count': len(valid_transactions)
    }


# In[4]:


def parse_transactions(raw_lines):
    """Parses raw lines into clean dictionaries as per Task 1.2."""
    keys = ['TransactionID', 'Date', 'ProductID', 'ProductName', 
            'Quantity', 'UnitPrice', 'CustomerID', 'Region']
    parsed = []
    
    for line in raw_lines:
        values = [v.strip() for v in line.split('|')]
        if len(values) == len(keys):
            try:
                # Handle commas within ProductName and numeric fields
                qty = int(values[4].replace(',', ''))
                price = float(values[5].replace(',', ''))
                
                parsed.append({
                    'TransactionID': values[0], 'Date': values[1],
                    'ProductID': values[2], 'ProductName': values[3].replace(',', ''),
                    'Quantity': qty, 'UnitPrice': price,
                    'CustomerID': values[6], 'Region': values[7]
                })
            except ValueError:
                continue
    return parsed

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """Validates and filters transactions as per Task 1.3."""
    total_parsed = len(transactions)
    valid_records = []
    
    # Validation Rules:
    # 1. Quantity/UnitPrice > 0
    # 2. TransactionID starts with 'T', ProductID with 'P', CustomerID with 'C'
    for t in transactions:
        is_valid = (
            t['Quantity'] > 0 and t['UnitPrice'] > 0 and
            t['TransactionID'].startswith('T') and
            t['ProductID'].startswith('P') and
            t['CustomerID'].startswith('C')
        )
        
        if is_valid:
            valid_records.append(t)

    # REQUIRED OUTPUT FORMAT
    print(f"Total records parsed: {total_parsed}")
    print(f"Invalid records removed: {total_parsed - len(valid_records)}")
    print(f"Valid records after cleaning: {len(valid_records)}")
    
    return valid_records


# In[5]:


def parse_transactions(raw_lines):
    """Parses raw lines into clean list of dictionaries."""
    keys = ['TransactionID', 'Date', 'ProductID', 'ProductName', 
            'Quantity', 'UnitPrice', 'CustomerID', 'Region']
    parsed = []
    
    for line in raw_lines:
        # Split by pipe and strip hidden whitespace from every value
        values = [v.strip() for v in line.split('|')]
        
        if len(values) == len(keys):
            try:
                # Remove commas from names and numbers before conversion
                qty = int(values[4].replace(',', ''))
                price = float(values[5].replace(',', ''))
                
                parsed.append({
                    'TransactionID': values[0],
                    'Date': values[1],
                    'ProductID': values[2],
                    'ProductName': values[3].replace(',', ''),
                    'Quantity': qty,
                    'UnitPrice': price,
                    'CustomerID': values[6],
                    'Region': values[7]
                })
            except ValueError:
                continue
    return parsed

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """Validates transactions and applies optional filters."""
    total_parsed = len(transactions)
    valid_records = []
    
    for t in transactions:
        # Strict Validation Rules
        is_valid = (
            t['Quantity'] > 0 and t['UnitPrice'] > 0 and
            t['TransactionID'].startswith('T') and # Prefix 'T' for Transaction
            t['ProductID'].startswith('P') and     # Prefix 'P' for Product
            t['CustomerID'].startswith('C')         # Prefix 'C' for Customer
        )
        
        if is_valid:
            valid_records.append(t)

    # Required Terminal Output
    print(f"Total records parsed: {total_parsed}")
    print(f"Invalid records removed: {total_parsed - len(valid_records)}")
    print(f"Valid records after cleaning: {len(valid_records)}")
    
    return valid_records


# In[6]:


def parse_transactions(raw_lines):
    """
    Parses raw lines into clean dictionaries as per Task 1.2.
    """
    keys = ['TransactionID', 'Date', 'ProductID', 'ProductName', 
            'Quantity', 'UnitPrice', 'CustomerID', 'Region']
    parsed_records = []
    
    for line in raw_lines:
        # Requirement: Split by pipe delimiter '|' and strip whitespace
        values = [v.strip() for v in line.split('|')]
        
        if len(values) == len(keys):
            try:
                # Requirement: Handle commas within ProductName and numeric fields
                qty_clean = values[4].replace(',', '')
                price_clean = values[5].replace(',', '')
                
                record = {
                    'TransactionID': values[0],
                    'Date': values[1],
                    'ProductID': values[2],
                    'ProductName': values[3].replace(',', ''),
                    'Quantity': int(qty_clean),
                    'UnitPrice': float(price_clean),
                    'CustomerID': values[6],
                    'Region': values[7]
                }
                parsed_records.append(record)
            except ValueError:
                continue
    return parsed_records

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates records against strict rules to reach the 80/10/70 count.
    """
    total_parsed = len(transactions)
    valid_records = []
    
    # Validation Rules from Task 1.3:
    # - Quantity/UnitPrice > 0
    # - TransactionID starts with 'T', ProductID with 'P', CustomerID with 'C'
    for t in transactions:
        is_valid = (
            t['Quantity'] > 0 and t['UnitPrice'] > 0 and
            t['TransactionID'].startswith('T') and
            t['ProductID'].startswith('P') and
            t['CustomerID'].startswith('C')
        )
        
        if not is_valid:
            continue

        # Optional Filter Logic
        total_price = t['Quantity'] * t['UnitPrice']
        if region and t['Region'] != region: continue
        if min_amount and total_price < min_amount: continue
        if max_amount and total_price > max_amount: continue
            
        valid_records.append(t)

    # Required Validation Output for the Manager
    invalid_count = total_parsed - len(valid_records)
    print(f"Total records parsed: {total_parsed}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {len(valid_records)}")
    
    return valid_records


# In[7]:


def low_performing_products(transactions, threshold=10):
    """
    Identifies products with low sales based on a quantity threshold.
    """
    # Dictionary to store aggregates: {ProductName: [TotalQuantity, TotalRevenue]}
    product_stats = {}

    for t in transactions:
        name = t['ProductName']
        qty = t['Quantity']
        rev = t['Quantity'] * t['UnitPrice']
        
        # Requirement: Aggregate by ProductName
        if name not in product_stats:
            product_stats[name] = [0, 0.0]
        
        product_stats[name][0] += qty
        product_stats[name][1] += rev

    # Requirement: Find products with total quantity < threshold
    low_performers = []
    for name, stats in product_stats.items():
        total_qty = stats[0]
        total_rev = stats[1]
        
        if total_qty < threshold:
            # Requirement: Include total quantity and revenue in tuple
            low_performers.append((name, total_qty, total_rev))

    # Requirement: Sort by TotalQuantity ascending
    low_performers.sort(key=lambda x: x[1])

    return low_performers


# In[ ]:




