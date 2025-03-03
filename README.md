# Introduction

This github repository is for storing datasets and code related to Project TROT for group 11.

## Data Dictionary for CRM Database

**1. Leads Table**

*   **LeadID:** E.g. "LEAD-001". Listed in 3 digits, in running order of leads received.
*   **Topic:** E.g. "Scope Walkthrough".  The subject or area of interest of the lead.
*   **FirstName:** E.g. "John". The lead's first name.
*   **LastName:** E.g. "Smith". The lead's last name.
*   **JobTitle:** E.g. "CTO". The lead's job title or position within their company.
*   **CompanyName:** E.g. "TechCorp Inc". The name of the company the lead works for.
*   **Email:** E.g. "john.smith@techcorp.com". The lead's email address.
*   **Phone:** E.g. "+65 8766 2834". The lead's phone number. All Singaporean numbers as requested
*   **Industry:** E.g. "Technology". The industry the lead's company operates in.
*   **LeadSource:** E.g. "Website". How the lead was acquired (e.g., Website, Trade Show, Referral, LinkedIn, Email Campaign).
*   **Status:** E.g. "Open". The current stage of the lead in the sales process. Scope: "Open", "Converted"
*   **Rating:** E.g. "Hot".  A measure of the lead's potential value. Scope: "Hot", "Warm", "Cold".
*   **EstimatedValue:** E.g. 30,000. The estimated monetary value of the potential deal. Scope: between 8,000 to 60,000
*   **EstimatedCloseDate:** E.g. "2025-06-30". The estimated date when the deal is expected to close.
*   **CreatedOn:** E.g. "2025-01-15". The date when the lead record was created.
*   **ModifiedOn:** E.g. "2025-01-15". The date when the lead record was last modified.
*   **OwnerID:** E.g. "USER-001". The ID of the user who owns the lead.

**2. Opportunities Table**

*   **OpportunityID:** E.g. "OPP-001".  Listed in 3 digits, in running order of opportunities.
*   **Name:** E.g. "ERP Implementation - TechCorp". The name of the opportunity.
*   **AccountID:** E.g. "ACC-001". The ID of the account associated with the opportunity.
*   **LeadID:** E.g. "LEAD-001". The ID of the lead that this opportunity originated from.
*   **Stage:** E.g. "Discovery". The current stage of the opportunity in the sales pipeline. Scope: "Discovery", "Connected", "Follow up".
    * **Discovery**: 
        * Initial identification of a potential client's security testing needs
        * Preliminary discussions to understand the client's infrastructure, compliance requirements, and security concerns
        * Gathering basic information about their web applications, systems, or networks that need testing
        * Identifying key stakeholders and decision-makers within the client organization
    * **Connected**:
        * Meaningful engagement established with decision-makers
        * Detailed scoping discussions using OWASP-based methodologies
        * Deeper technical discovery of the client's environment
        * Alignment on testing objectives, compliance requirements (PCI DSS, HIPAA, etc.)
        * Presentation of initial testing approach and methodology
    * **Follow up**: 
        * Development and presentation of formal testing proposals
        * Refinement of scope based on client feedback
        * Discussion of specific testing timelines and logistics
        * Addressing any technical or business concerns
        * Finalizing contract terms and testing parameters
        * Coordinating pre-testing requirements and access credentials
*   **Probability:** E.g. 30. The probability (as a percentage) of winning the opportunity. Scope: "30", "60", "90"
*   **EstimatedValue:** E.g. 8,000.  The estimated monetary value of the opportunity. Scope: Between 8,000 to 60,000
*   **ExpectedCloseDate:** E.g. "2025-06-30". The expected date when the opportunity is expected to close.
*   **ActualCloseDate:** E.g. "2025-02-01". The actual date when the opportunity was closed (blank if still open).
*   **Status:** E.g. "In Progress". The current status of the opportunity. Scope: "In Progress", "Won".
*   **Description:** E.g. "Vulnerability Analysis and Exploitation". A brief description of the opportunity.
*   **OwnerID:** E.g. "USER-001". The ID of the user who owns the opportunity.
*   **CreatedOn:** E.g. "2025-01-20". The date when the opportunity record was created.
*   **ModifiedOn:** E.g. "2025-01-20". The date when the opportunity record was last modified.

**3. Quotes Table**

*   **QuoteID:** E.g. "QUO-001". Listed in 3 digits, in running order of quotes generated.
*   **OpportunityID:** E.g. "OPP-001". The ID of the opportunity this quote is related to.
*   **Name:** E.g. "Vulnerability Analysis and Exploitation". The name of the quote.
*   **AccountID:** E.g. "ACC-001". The ID of the account the quote is for.
*   **QuoteNumber:** E.g. "Q2025-001". A unique number for the quote.
*   **Status:** E.g. "Sent". The current status of the quote. Scope: "Draft", "Sent", "Accepted", "Rejected".
*   **ValidFrom:** E.g. "2025-01-20". The date from which the quote is valid.
*   **ValidTo:** E.g. "2025-02-20". The date until which the quote is valid.
*   **TotalAmount:** E.g. 75000. The total amount of the quote before discounts.
*   **DiscountPercentage:** E.g. 5. The discount percentage applied to the quote. Scope: 3 to 20%.
*   **DiscountAmount:** E.g. 3750. The discount amount.
*   **FinalAmount:** E.g. 71250. The final amount of the quote after discounts.
*   **Description:** E.g. "Vulnerability Analysis and Exploitation". A description of the quote.
*   **CreatedOn:** E.g. "2025-01-20". The date when the quote record was created.
*   **ModifiedOn:** E.g. "2025-01-20". The date when the quote record was last modified.

**4. Contracts Table**

*   **ContractID:** E.g. "CON-001". Listed in 3 digits, in running order of contracts.
*   **QuoteID:** E.g. "QUO-003". The ID of the quote the contract is based on.
*   **AccountID:** E.g. "ACC-003". The ID of the account the contract is with.
*   **ContractNumber:** E.g. "C2025-001". A unique number for the contract.
*   **Status:** E.g. "Draft". The current status of the contract. Scope: "Draft", "Pending", "Approved", "Suspended", "Completed", "Cancelled", "Expired".
*   **StartDate:** E.g. "2025-02-01". The start date of the contract.
*   **EndDate:** E.g. "2026-01-31". The end date of the contract.
*   **TotalValue:** E.g. 200000. The total value of the contract.
*   **BillingFrequency:** E.g. "Monthly". How often the contract is billed. Scope: "Monthly", "Quarterly", "Annually", "As Per Contract Milestones".
*   **PaymentTerms:** E.g. "Net 30". The payment terms of the contract. Scope: "Net 30", "Net 60", "Net 90".
*   **Description:** E.g. "remediation validation and retest". A description of the contract.
*   **CreatedOn:** E.g. "2025-02-01". The date when the contract record was created.
*   **ModifiedOn:** E.g. "2025-02-01". The date when the contract record was last modified.

**5. Contract Milestones Table**

*   **MilestoneID:** E.g. "MIL-001". Listed in 3 digits, in running order of milestones.
*   **ContractID:** E.g. "CON-001". The ID of the contract the milestone belongs to.
*   **Name:** E.g. "Initial Assessment". The name of the milestone.
*   **Description:** E.g. "Security infrastructure assessment completion". A description of the milestone.
*   **DueDate:** E.g. "2025-03-01". The date the milestone is due.
*   **Amount:** E.g. 40000. The amount associated with the milestone.
*   **Status:** E.g. "Completed". The current status of the milestone. Scope: "Planned", "In Progress", "Completed", "Delayed".
*   **CompletionDate:** E.g. "2025-02-28". The date the milestone was completed

**6. Projects Table**

* **ProjectID:** E.g. "PRJ-001". Listed in 3 digits, in running order of projects.
* **ContractID:** E.g. "CON-001". The ID of the contract this project is associated with.
* **Name:** E.g. "Security Audit 2025". The name of the project.
* **Description:** E.g. "Comprehensive security audit project". A description of the project.
* **StartDate:** E.g. "2025-02-01". The start date of the project.
* **EndDate:** E.g. "2025-05-01". The end date of the project.
* **Status:** E.g. "Active". The current status of the project. Scope: "Active", "Closed", "Inactive".
* **ProjectManager:** E.g. "USER-001". The ID of the user managing the project. Scope: 3 project managers. 
* **Budget:** E.g. 200000. The total budget allocated to the project. 
* **ActualCost:** E.g. 45000. The actual cost incurred on the project so far.
* **Progress:** E.g. 35. The percentage of project completion.
* **Risk:** E.g. "Low". The risk level associated with the project. Scope: "Low", "Medium", "High".
* **CreatedOn:** E.g. "2025-02-01". The date when the project record was created.
* **ModifiedOn:** E.g. "2025-02-01". The date when the project record was last modified.

**7. Contract Invoices Table**

* **InvoiceID:** E.g. "INV-001". Listed in 3 digits, in running order of invoices.
* **ContractID:** E.g. "CON-001". The ID of the contract the invoice is related to.
* **MilestoneID:** E.g. "MIL-001". The ID of the milestone the invoice is related to (if applicable, otherwise blank).
* **InvoiceNumber:** E.g. "INV2025-001". A unique number for the invoice.
* **Status:** E.g. "Billed". The current status of the invoice. Scope: "Billed", "Cancelled", "Complete", "New".
    * **Cancelled**: can be due to a variety of reasons, such as the following 
        * **Material scope changes** 
            * After invoice issuance, significant changes to the penetration testing scope may require cancellation and reissuance (e.g., additional test cases or attack vectors were added or removed)
        * **Technical errors in the invoice** 
            * Incorrect billing details such as:
                * Wrong testing hours or rates
                * Incorrect OWASP methodology references
                * Errors in compliance framework citations (PCI DSS, HIPAA, etc.)
                * Inaccurate description of delivered testing services
        * **Client organizational changes**
            * Changes on the client side such as:
                * Corporate restructuring affecting billing entity
                * Project ownership transfer between departments
                * Updated purchase order requirements
        * **Timing/scheduling changes**
            * When testing engagements are rescheduled or delayed significantly after invoice issuance
        * **Compliance and regulatory requirements** 
            * The need to reflect specific regulatory language or compliance attestations not included in the original invoice
        * **Contract renegotiation** 
            * Terms of the penetration testing engagement were renegotiated after invoice issuance
* **IssueDate:** E.g. "2025-02-28". The date the invoice was issued.
* **DueDate:** E.g. "2025-03-30". The date the invoice is due.
* **Amount:** E.g. 40000. The total amount of the invoice. Scope: ?
* **PaidAmount:** E.g. 40000. The amount paid on the invoice. Scope: ? 
* **PaidDate:** E.g. "2025-03-25". The date the invoice was paid (blank if not paid).
* **Description:** E.g. "Initial security assessment milestone". A description of the invoice.
* **CreatedOn:** E.g. "2025-02-28". The date when the invoice record was created.
* **ModifiedOn:** E.g. "2025-03-25". The date when the invoice record was last modified.

**8. Approved Timesheets Table**

* **TimesheetID:** E.g. "TS-001". Listed in 3 digits, in running order of timesheets.
* **ProjectID:** E.g. "PRJ-001". The ID of the project the timesheet is for.
* **EmployeeID:** E.g. "EMP-001". The ID of the employee who submitted the timesheet. Scope: 20 Employees
* **WeekStartDate:** E.g. "2025-02-03". The start date of the week the timesheet covers.
* **WeekEndDate:** E.g. "2025-02-09". The end date of the week the timesheet covers.
* **Status:** E.g. "Approved". The current status of the timesheet. Scope: "Draft", "Submitted", "Approved", "Rejected", "Under Review", "Processed", "Finalised".
    * **Draft**:  Initial creation of the timesheet with testing hours recorded
    * **Submitted**: Timesheet sent for management review
    * **Under Review**: Management actively reviewing timesheet entries
    * **Approved / Rejected**: Decision on timesheet validity. If rejected, typically returns to Draft status for correction
    * **Processed**:  Administrative handling of approved timesheets
    * **Finalized**: Timesheet locked for billing/invoicing
* **TotalHours:** E.g. 40. The total number of hours worked during the week. Scope: ?
* **BillableHours:** E.g. 35. The number of billable hours worked during the week. Scope: ?
* **NonBillableHours:** E.g. 5. The number of non-billable hours worked during the week. Scope: ?
* **ApprovedBy:** E.g. "USER-001". The ID of the user who approved the timesheet. Scope: 2 approvers
* **ApprovalDate:** E.g. "2025-02-10". The date the timesheet was approved.
* **Comments:** E.g. "Security assessment activities". Any comments related to the timesheet.
* **CreatedOn:** E.g. "2025-02-09". The date when the timesheet record was created.
* **ModifiedOn:** E.g. "2025-02-10". The date when the timesheet record was last modified.

## ERD Diagram
![image](https://github.com/user-attachments/assets/bc47384a-8f77-4ae5-9666-438a6a0951c1)

## Status Relationships
- Converted Leads becomes Opportunities
- All Opportunities becomes Quotes
- Cancelled Opportunities must have Rejected Quotes
- Accepted Quotes become Contracts
- Approved Contacts becomes Milestones & Project
- Suspended / Completed / Expired Contract must have Cancelled Milestones & Inactive Project
- Completed Contract must have Completed Milestones & Closed Project
- Completed Milestones must have Completed Invoice for those with Payment Term 'As Per Contract milestone'
- Closed Projects must have Finalized Timesheets 



