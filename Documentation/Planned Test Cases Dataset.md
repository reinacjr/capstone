## Data Dictionary for Planned Testcases Database

### **ProjectID**
- **Example**: `"PRJ-082"`
- **Description**: A unique identifier for each project being tested.

### **ProjectName**
- **Example**: `"Web Application Contract Project"`
- **Description**: Describes the official title of the contract project undergoing testing.

### **UserID**
- **Example**: `"USER-015"`
- **Description**: Identifies the individual user responsible for running or managing the test case.

### **TestingScope**
- **Example**: `"WEB"`, `"APP"`
- **Description**: Refers to the type of platform or environment being tested (e.g., Web application, Mobile app).

### **TestCaseID**
- **Example**: `"TC-001"`
- **Description**: Unique identifier for each test case linked to the project.

### **TestCase**
- **Example**: `"Input Validation"`, `"XSS"`, `"SQL Injection"`
- **Description**: Describes the nature of the vulnerability or the specific security test being performed.

### **Findings (Affected Components)**
- **Example**: `"User profile page"`, `"Database"`
- **Description**: Indicates the component or area in the system where the vulnerability was found.

### **SeverityRatings**
- **Example**: `"Low"`, `"Medium"`, `"High"`, `"Critical"`
- **Description**: Describes the potential impact level of the vulnerability or issue discovered.

### **Deadline**
- **Example**: `"05-Oct-2024"`
- **Description**: The deadline by which the testing or remediation is expected to be completed.

- # Planned Security Test Cases Generator Documentation

## Overview

The **Planned Security Test Cases Generator** is a Python-based utility that programmatically simulates a series of structured test case records for security testing projects. It integrates OWASP categories, MITRE techniques, and compliance mapping, producing a ready-to-use dataset for dashboards, analysis, and matching with system logs.

---

## Features of the System

**Key Functions:**
- Simulates realistic test case data across multiple projects and scopes.
- Incorporates **OWASP WSTG categories**, **MITRE ATT&CK techniques**, and **CVSS scoring**.
- Adds metadata such as `Severity`, `Deadline`, `Test Case Description`, and `Compliance Framework`.
- Supports randomization for variability and realism.

**Generated Fields Include:**
- `ProjectID`
- `ProjectName`
- `UserID`
- `TestingScope`
- `TestCaseID`
- `TestCase`
- `OWASP_WSTG_CATEGORIES`
- `MITRE_TECHNIQUES`
- `CVSS_SCORES`
- `COMPLIANCE_FRAMEWORKS`
- `Deadline` and `DaysAllocated`

---

## Project Structure


---

## How the System Works

### Step 1: Set Up Taxonomies
Defines mappings for:
- **OWASP_WSTG_CATEGORIES**
- **MITRE_TECHNIQUES**
- **COMPLIANCE_FRAMEWORKS**
- **CVSS_SCORES**

### Step 2: Generate Dummy Project Metadata
Populates mock:
- `ProjectID`, `UserID`, and `TestCaseID`
- `Test Case Titles` (e.g. XSS, SQLi, Authentication)
- Platform scope (`WEB`, `APP`, `API`)

### Step 3: Random Assignment & Logical Mapping
- Randomly selects OWASP, MITRE, and CVSS tags per test case
- Maps test types to attack techniques and severity scores
- Simulates deadlines (e.g. within 30 days from generation)

### Step 4: Output File Creation
Exports the synthetic test case dataset in `.csv` format.

---

## Output

Each generated record contains:
- Contextual metadata for testing
- Standardized categorization fields (OWASP, MITRE, CVSS, Compliance)
- Usable in alignment with logs and dashboards

---


