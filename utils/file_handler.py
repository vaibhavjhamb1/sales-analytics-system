#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os

def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues.
    
    Returns: list of raw lines (strings)
    
    Expected Output Format:
    ['T001|2024-12-01|P101|Laptop|2|45000|C001|North', ...]
    """
    # Requirements: Handle FileNotFoundError with appropriate error message
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return []

    # Requirements: Handle different encodings (try 'utf-8', 'latin-1', 'cp1252')
    encodings = ['utf-8', 'latin-1', 'cp1252']
    
    for enc in encodings:
        try:
            # Requirements: Use 'with' statement
            with open(filename, 'r', encoding=enc) as file:
                lines = file.readlines()
                
                # Requirements: Skip the header row and remove empty lines
                # We slice from [1:] to skip the header
                processed_lines = [line.strip() for line in lines[1:] if line.strip()]
                
                return processed_lines
                
        except (UnicodeDecodeError, LookupError):
            continue
    
    print("Error: Could not decode the file with supported encodings.")
    return []

def save_report(content, filename="summary_report.txt"):
    """Saves the final analysis to the output directory."""
    os.makedirs('output', exist_ok=True)
    with open(os.path.join('output', filename), 'w') as f:
        f.write(content)


# In[15]:


import os

def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues.
    
    Returns: list of raw lines (strings)
    
    Expected Output Format:
    ['T001|2024-12-01|P101|Laptop|2|45000|C001|North', ...]
    """
    # Requirement: Handle FileNotFoundError with appropriate error message
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return []

    # Requirement: Handle different encodings (try 'utf-8', 'latin-1', 'cp1252')
    encodings = ['utf-8', 'latin-1', 'cp1252']
    
    for enc in encodings:
        try:
            # Requirement: Use 'with' statement
            with open(filename, 'r', encoding=enc) as file:
                lines = file.readlines()
                
                # Requirement: Skip the header row and remove empty lines
                # We use slicing [1:] to skip the header line
                processed_lines = [line.strip() for line in lines[1:] if line.strip()]
                
                return processed_lines
                
        except (UnicodeDecodeError, LookupError):
            continue
    
    print("Error: Could not decode the file with supported encodings.")
    return []

def save_report(content, filename="summary_report.txt"):
    """Saves the final analysis to the output directory."""
    os.makedirs('output', exist_ok=True)
    with open(os.path.join('output', filename), 'w') as f:
        f.write(content)


# In[16]:


import os

def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues.
    
    Returns: list of raw lines (strings)
    
    Expected Output Format:
    ['T001|2024-12-01|P101|Laptop|2|45000|C001|North', ...]
    """
    # Requirement: Handle FileNotFoundError with appropriate error message
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return []

    # Requirement: Handle different encodings (try 'utf-8', 'latin-1', 'cp1252')
    encodings = ['utf-8', 'latin-1', 'cp1252']
    
    for enc in encodings:
        try:
            # Requirement: Use 'with' statement for file operations
            with open(filename, 'r', encoding=enc) as file:
                lines = file.readlines()
                
                # Requirement: Skip the header row
                # Requirement: Remove empty lines
                # lines[1:] slices the list to ignore the first header line
                processed_lines = [line.strip() for line in lines[1:] if line.strip()]
                
                return processed_lines
                
        except (UnicodeDecodeError, LookupError):
            # Continue to the next encoding if a decode error occurs
            continue
    
    print("Error: Could not decode the file with supported encodings.")
    return []

def save_report(content, filename="summary_report.txt"):
    """
    Saves the final analysis to the output directory.
    """
    os.makedirs('output', exist_ok=True)
    with open(os.path.join('output', filename), 'w') as f:
        f.write(content)


# In[ ]:




