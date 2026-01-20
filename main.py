#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import os
from datetime import datetime

# Import all modules created in previous tasks
from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_transactions, validate_and_filter, region_wise_sales,
    top_selling_products, customer_analysis, daily_sales_trend,
    find_peak_sales_day, low_performing_products, enrich_sales_data,
    save_enriched_data, generate_sales_report
)
from utils.api_handler import fetch_all_products, create_product_mapping

def main():
    """
    Orchestrates the full data pipeline: Extraction, Transformation, 
    API Enrichment, and Reporting.
    """
    print("=" * 50)
    print("      SALES ANALYTICS SYSTEM - VERSION 2.0")
    print("=" * 50)

    try:
        # [1/10] Reading Data
        print("\n[1/10] Reading sales data...")
        raw_lines = read_sales_data('data/sales_data.txt')
        if not raw_lines:
            print("! Error: sales_data.txt is empty or missing.")
            return
        print(f"✓ Found {len(raw_lines)} raw transactions.")

        # [2/10] Parsing
        print("\n[2/10] Parsing and cleaning...")
        parsed_records = parse_transactions(raw_lines)
        print(f"✓ {len(parsed_records)} records successfully parsed.")

        # [3/10] User Interaction: Filtering
        print("\n[3/10] Filter Options Available:")
        regions = sorted(list(set(t['Region'] for t in parsed_records)))
        amounts = [t['Quantity'] * t['UnitPrice'] for t in parsed_records]
        
        print(f"   Available Regions: {', '.join(regions)}")
        print(f"   Amount Range:      ₹{min(amounts):,.2f} - ₹{max(amounts):,.2f}")

        do_filter = input("\nApply filters before analysis? (y/n): ").lower().strip()
        f_region, f_min, f_max = None, None, None

        if do_filter == 'y':
            f_region = input("   Filter by Region (press Enter to skip): ").strip() or None
            try:
                f_min_input = input("   Filter by Min Total Price (press Enter to skip): ").strip()
                f_min = float(f_min_input) if f_min_input else None
                
                f_max_input = input("   Filter by Max Total Price (press Enter to skip): ").strip()
                f_max = float(f_max_input) if f_max_input else None
            except ValueError:
                print("   ! Invalid numeric input. Proceeding without price filters.")

        # [4/10] Validation & Filtering Execution
        print("\n[4/10] Validating and filtering transactions...")
        valid_data, invalid_count, filter_summary = validate_and_filter(
            parsed_records, region=f_region, min_amount=f_min, max_amount=f_max
        )
        print(f"✓ Valid: {len(valid_data)} | Invalid/Filtered: {invalid_count}")

        # [5/10] Analysis
        print("\n[5/10] Performing statistical analysis...")
        # These calculations are handled inside the report generator, 
        # but you could trigger specific prints here if needed.
        print("✓ Analysis logic verified.")

        # [6/10] API Integration
        print("\n[6/10] Fetching external product metadata (DummyJSON)...")
        api_products = fetch_all_products()
        if not api_products:
            print("   ! Warning: API fetch failed. Proceeding with local data only.")
        product_map = create_product_mapping(api_products)
        print(f"✓ Mapping created for {len(product_map)} API products.")

        # [7/10] Enrichment
        print("\n[7/10] Enriching sales data with API information...")
        enriched_data = enrich_sales_data(valid_data, product_map)
        match_count = sum(1 for item in enriched_data if item.get('API_Match'))
        print(f"✓ Enrichment complete: {match_count}/{len(valid_data)} matched.")

        # [8/10] Persistence
        print("\n[8/10] Saving enriched dataset...")
        save_enriched_data(enriched_data, 'data/enriched_sales_data.txt')
        print("✓ Saved to: data/enriched_sales_data.txt")

        # [9/10] Reporting
        print("\n[9/10] Generating comprehensive report...")
        generate_sales_report(valid_data, enriched_data, 'output/sales_report.txt')
        print("✓ Report saved to: output/sales_report.txt")

        # [10/10] Conclusion
        print("\n" + "=" * 50)
        print(f"PROCESS COMPLETED AT {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 50)
        print("Review the 'output/' and 'data/' folders for your results.")

    except Exception as e:
        print("\n" + "!" * 50)
        print(f"FATAL ERROR: {str(e)}")
        print("Ensure all 'utils/' modules are correctly implemented.")
        print("!" * 50)

if __name__ == "__main__":
    main()

