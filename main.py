#!/usr/bin/env python
# coding: utf-8

# In[13]:


from utils.file_handler import load_raw_data, write_report
from utils.data_processor import clean_and_validate
from utils.api_handler import get_product_details

def main():
    # 1. Define the path to the messy data file
    # Ensure this matches the structure: data/sales_data.txt
    data_path = 'data/sales_data.txt'
    
    # 2. Load the raw data
    # This function handles the pipe-delimiters and non-UTF-8 encoding
    raw_data = load_raw_data(data_path)
    
    if not raw_data:
        print("No data found or file is empty.")
        return

    # 3. Clean and Validate Data
    # This will automatically print the 80/10/70 stats required by the manager
    clean_data = clean_and_validate(raw_data)
    
    # 4. Perform Analysis
    total_revenue = 0.0
    for record in clean_data:
        # Calculate revenue using cleaned numeric types
        total_revenue += record['Quantity'] * record['UnitPrice']
    
    # 5. Integrate API (Demonstration)
    # Fetch details for the first product in the cleaned list
    if clean_data:
        sample_product = clean_data[0]['ProductID']
        api_info = get_product_details(sample_product)
        category = api_info.get('category', 'N/A')
    else:
        category = "N/A"

    # 6. Generate the Final Report String
    report_content = f"""=====================================
SALES ANALYTICS REPORT
=====================================
Total Transactions: {len(clean_data)}
Total Revenue: ${total_revenue:,.2f}
Sample Product Category: {category}
====================================="""

    # 7. Print to console and save to output folder
    print("\n" + report_content)
    write_report(report_content, "summary_report.txt")
    print("\nSuccess: Report saved to output/summary_report.txt")

if __name__ == "__main__":
    main()


# In[ ]:




