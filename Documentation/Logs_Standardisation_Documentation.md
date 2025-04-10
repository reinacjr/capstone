
# Logs Standardisation & Extraction System Documentation

## Overview

The **Logs Standardisation & Extraction System** is a Python-based tool designed to streamline the process of extracting key information from raw log files, aligning them with planned test cases information and standardising outputs for easier analysis at a quick glance, dashboarding and reporting.

---

## Features of the System:

**Input Files:**
- File 1: Load field requirements and manual flags (xlsx file): This enables easier editing for users if they want to extract fewer or more fields from the system
- File 2: Process planned test case inputs (csv file)
- File 3: Parse raw Burpsuite log entries (txt file) and identify relevant information blocks

**Code System:**
- Extract and standardise fields from logs
- Align extracted data with planned test cases: Ties in raw Burpsuite Logs and planned test cases data, performing a **matching process** to generate the **Test Case Status** Field

**Output File:**
- Export clean outputs in CSV format for easier analysis, dashboard visualisation and reporting purposes

---

## Project Structure

```
├── Logs Standardisation & Extraction System.ipynb (Code File)
├── Data Extraction Fields.xlsx (Input File 1)
├── refined_security_test_cases.csv (Input File 2)
├── updated_logs.txt (Input File 3)
├── logs_system_output.csv (Output File)
```

---

## How the System Works:

### Step 1: Loading in the Input Files
- **Field Requirements** (`Data Extraction Fields.xlsx`): Specifies field names and whether they require manual input.
- **Test Cases** (`refined_security_test_cases.csv`): Contains structured planned security test cases.
- **Raw Logs** (`updated_logs.txt`): Raw logs with the delimiter `======================================================`.

### Step 2: Preprocess Fields

```python
field_df = pd.read_excel("Data Extraction Fields.xlsx", header=None)
field_df.columns = ["Field Name", "Manual Input"]
field_df["Manual Input"] = field_df["Manual Input"].fillna("").astype(str).str.lower()
```

### Step 3: Load & Segment Log Entries

```python
with open("updated_logs.txt", "r", encoding="utf-8") as f:
    log_blocks = f.read().split("======================================================")
```

### Step 4: Extract Field Values

Using regex patterns and predefined field lists, the system iterates through each log block and extracts values for the specified fields. Manual inputs are flagged accordingly.

### Step 5: Match Logs to Test Cases (Matching Process)

A logic layer matches extracted log entries to test cases using identifiers (Project ID and Test Case ID).

### Step 6: Export Results

The final result is exported as both `.csv` format for further analysis or archiving.

---

## Output

The resulting file includes:
- All extracted fields (as per configuration)
- Manual flags
- Matching test case information
- Other key information from log entries

---

## Dependencies

Do ensure that the following packages are installed before running the code
```bash
pip install pandas openpyxl
```

---

## Other Notes

- The raw logs should consistently use the delimiter `======================================================`.
- Fields in the Excel configuration should try to match those present in the logs to avoid any missed extractions.
- Manual review is suggested for fields marked as needing manual input.
