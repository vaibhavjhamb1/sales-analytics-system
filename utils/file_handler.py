#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

def load_raw_data(filepath):
    """
    Reads the pipe-delimited file with non-UTF-8 encoding.
    """
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found.")
        return []

    data = []
    # Using latin-1 as specified for non-UTF-8 encoding issues
    with open(filepath, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        if not lines:
            return []
            
        # Extract header and split by pipe
        header = lines[0].strip().split('|')
        
        for line in lines[1:]:
            line = line.strip()
            if not line: # Skip empty lines
                continue
                
            values = line.split('|')
            # Handle rows with missing or extra fields
            if len(values) == len(header):
                data.append(dict(zip(header, values)))
    return data

def write_report(report_content, filename="summary_report.txt"):
    """Saves the final analysis to the output directory."""
    os.makedirs('output', exist_ok=True)
    with open(os.path.join('output', filename), 'w') as f:
        f.write(report_content)


# In[ ]:




