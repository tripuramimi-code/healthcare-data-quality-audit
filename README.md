# Healthcare Data Quality Audit & Cleaning Pipeline

## Project Objective
This project establishes an automated Python data-profiling and remediation engine designed to audit incoming healthcare registry data. It identifies data anomalies (missing fields, duplicate records) to protect analytical integrity before downstream clinical reporting.

## Tech Stack & Tools
- **Language:** Python 3.13
- **Libraries:** Pandas

## Data Quality Audit Metrics (Before vs. After)
- **Original Records Scanned:** 55,500
- **Identified Duplicate Records:** 534 (Removed automatically)
- **Total Corrupted Records Dropped:** 534
- **Final Data Integrity Score:** 99.04%

## Key Actions Performed
1. **Schema Validation:** Verified column data types and mapping structures.
2. **Uniqueness Enforcement:** Deduplicated historical client entries using Python vectorization.
3. **Data Export:** Generated a clean, analysis-ready target dataset (`clean_healthcare_data.csv`).
