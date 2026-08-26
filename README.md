# Python Data Processing & Automation

## Overview

This project demonstrates an automated data processing pipeline using Python and Pandas.

The pipeline simulates a common data engineering workflow where raw customer and transaction files are received from an operational system and need to be cleaned, transformed and prepared for downstream analytics.

The process includes:

- Reading raw CSV files
- Data profiling
- Data cleaning
- Data type conversion
- Duplicate handling
- Missing value handling
- Data transformation
- Data validation
- Output generation
- Logging
- Error handling

> This project uses synthetic data created specifically for portfolio and learning purposes.

---

## Business Scenario

A fictional organisation receives daily customer and transaction files.

The raw data may contain:

- Duplicate records
- Missing values
- Inconsistent text formatting
- Invalid transaction amounts
- Incorrect date formats
- Invalid customer IDs
- Unnecessary whitespace

Before the data can be used by reporting or analytics teams, the files need to be processed through an automated pipeline.

---

## Pipeline Architecture

```text
                RAW DATA
                   |
                   v
          +------------------+
          | File Validation  |
          +------------------+
                   |
                   v
          +------------------+
          | Data Profiling   |
          +------------------+
                   |
                   v
          +------------------+
          | Data Cleaning    |
          +------------------+
                   |
                   v
          +------------------+
          | Transformation   |
          +------------------+
                   |
                   v
          +------------------+
          | Data Validation  |
          +------------------+
                   |
                   v
          +------------------+
          | Cleaned Output   |
          +------------------+
                   |
                   v
               LOGGING
