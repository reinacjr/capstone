## Data Dictionary for Planned Testcases Database

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
