# Introduction

This github repository is for storing datasets and code related to Project TROT for group 11.

## Data Dictionary for CRM Database

**1. Leads Table**

*   **LeadID:** E.g. "LEAD-001". Listed in 3 digits, in running order of leads received.
*   **Topic:** E.g. "ERP Implementation".  The subject or area of interest of the lead.
*   **FirstName:** E.g. "John". The lead's first name.
*   **LastName:** E.g. "Smith". The lead's last name.
*   **JobTitle:** E.g. "CTO". The lead's job title or position within their company.
*   **CompanyName:** E.g. "TechCorp Inc". The name of the company the lead works for.
*   **Email:** E.g. "john.smith@techcorp.com". The lead's email address.
*   **Phone:** E.g. "+1-555-0101". The lead's phone number. Currently all North American numbers as per provided data.
*   **Industry:** E.g. "Technology". The industry the lead's company operates in.
*   **LeadSource:** E.g. "Website". How the lead was acquired (e.g., Website, Trade Show, Referral, LinkedIn, Email Campaign).
*   **Status:** E.g. "New". The current stage of the lead in the sales process. Scope: "New", "Contacted", "Qualified", "Proposal Sent", "Closed Won", "Closed Lost".
*   **Rating:** E.g. "Hot".  A measure of the lead's potential value. Scope: "Hot", "Warm", "Cold".
*   **EstimatedValue:** E.g. 75000. The estimated monetary value of the potential deal.
*   **EstimatedCloseDate:** E.g. "2025-06-30". The estimated date when the deal is expected to close.
*   **CreatedOn:** E.g. "2025-01-15". The date when the lead record was created.
*   **ModifiedOn:** E.g. "2025-01-15". The date when the lead record was last modified.
*   **OwnerID:** E.g. "USER-001". The ID of the user who owns the lead.

**2. Opportunities Table**

*   **OpportunityID:** E.g. "OPP-001".  Listed in 3 digits, in running order of opportunities.
*   **Name:** E.g. "ERP Implementation - TechCorp". The name of the opportunity.
*   **AccountID:** E.g. "ACC-001". The ID of the account associated with the opportunity.
*   **LeadID:** E.g. "LEAD-001". The ID of the lead that this opportunity originated from.
*   **Stage:** E.g. "Proposal". The current stage of the opportunity in the sales pipeline. Scope: "Discovery", "Qualification", "Proposal", "Negotiation", "Closed".
*   **Probability:** E.g. 75. The probability (as a percentage) of winning the opportunity.
*   **EstimatedValue:** E.g. 75000.  The estimated monetary value of the opportunity.
*   **ExpectedCloseDate:** E.g. "2025-06-30". The expected date when the opportunity is expected to close.
*   **ActualCloseDate:** E.g. "2025-02-01". The actual date when the opportunity was closed (blank if still open).
*   **Status:** E.g. "Open". The current status of the opportunity. Scope: "Open", "Won", "Lost".
*   **Description:** E.g. "Complete ERP system implementation including training". A brief description of the opportunity.
*   **OwnerID:** E.g. "USER-001". The ID of the user who owns the opportunity.
*   **CreatedOn:** E.g. "2025-01-20". The date when the opportunity record was created.
*   **ModifiedOn:** E.g. "2025-01-20". The date when the opportunity record was last modified.

**3. Quotes Table**

*   **QuoteID:** E.g. "QUO-001". Listed in 3 digits, in running order of quotes generated.
*   **OpportunityID:** E.g. "OPP-001". The ID of the opportunity this quote is related to.
*   **Name:** E.g. "ERP Implementation Quote". The name of the quote.
*   **AccountID:** E.g. "ACC-001". The ID of the account the quote is for.
*   **QuoteNumber:** E.g. "Q2025-001". A unique number for the quote.
*   **Status:** E.g. "Sent". The current status of the quote. Scope: "Draft", "Sent", "Accepted", "Rejected".
*   **ValidFrom:** E.g. "2025-01-20". The date from which the quote is valid.
*   **ValidTo:** E.g. "2025-02-20". The date until which the quote is valid.
*   **TotalAmount:** E.g. 75000. The total amount of the quote before discounts.
*   **DiscountPercentage:** E.g. 5. The discount percentage applied to the quote.
*   **DiscountAmount:** E.g. 3750. The discount amount.
*   **FinalAmount:** E.g. 71250. The final amount of the quote after discounts.
*   **Description:** E.g. "ERP implementation services and licenses". A description of the quote.
*   **CreatedOn:** E.g. "2025-01-20". The date when the quote record was created.
*   **ModifiedOn:** E.g. "2025-01-20". The date when the quote record was last modified.

**4. Contracts Table**

*   **ContractID:** E.g. "CON-001". Listed in 3 digits, in running order of contracts.
*   **QuoteID:** E.g. "QUO-003". The ID of the quote the contract is based on.
*   **AccountID:** E.g. "ACC-003". The ID of the account the contract is with.
*   **ContractNumber:** E.g. "C2025-001". A unique number for the contract.
*   **Status:** E.g. "Active". The current status of the contract. Scope: "Draft", "Pending", "Active", "Terminated", "Expired".
*   **StartDate:** E.g. "2025-02-01". The start date of the contract.
*   **EndDate:** E.g. "2026-01-31". The end date of the contract.
*   **TotalValue:** E.g. 200000. The total value of the contract.
*   **BillingFrequency:** E.g. "Monthly". How often the contract is billed. Scope: "Monthly", "Quarterly", "Annually".
*   **PaymentTerms:** E.g. "Net 30". The payment terms of the contract. Scope: "Net 30", "Net 45", "Net 60".
*   **Description:** E.g. "Security audit and compliance services contract". A description of the contract.
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
