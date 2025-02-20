##Data Generation Code for Customer Relations Database

## Do the necessary imports

import csv
import random
from datetime import datetime, timedelta


## * 1. Leads 

def generate_lead_data(num_records=100):
    topics = ["ERP Implementation", "Cloud Migration", "Security Audit", 
              "Data Analytics Solution", "Digital Transformation", "Penetration Testing", 
              "Compliance Consulting", "Incident Response", "Vulnerability Management", 
              "Security Awareness Training", "Cloud Security", "Data Loss Prevention", 
              "Endpoint Security", "SIEM Implementation", "Threat Intelligence", 
              "Vulnerability Scanning", "Security Consulting", "Data Encryption", 
              "Network Security", "Application Security", "Phishing Simulation", 
              "Red Teaming", "Security Architecture Design", "Zero Trust Implementation", 
              "SOAR Deployment", "DevSecOps", "GRC Consulting", "Data Privacy", 
              "Cybersecurity Risk Assessment", "IoT Security"]
    
    first_names = ["John", "Sarah", "Michael", "Emma", "Robert", "David", "Ashley", 
                   "Christopher", "Jessica", "Matthew", "Angela", "Kevin", "Brian", 
                   "Stephanie", "Eric", "Nicole", "Justin", "Lauren", "Brandon", "Tiffany", 
                   "William", "Elizabeth", "Ryan", "Megan", "Kyle", "Emily", "Jacob", 
                   "Abigail", "Ethan", "Madison"]
    
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Garcia", "Rodriguez", 
                  "Lee", "Clark", "Lewis", "Robinson", "Walker", "Hall", "Young", 
                  "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", 
                  "Adams", "Baker", "Nelson", "Carter", "Mitchell", "Perez", 
                  "Roberts", "Turner", "Phillips"]
    
    job_titles = ["CTO", "IT Director", "CISO", "CEO", "COO", "Security Manager", 
                  "Compliance Officer", "IT Manager", "Security Analyst", "HR Manager",
                    "Cloud Architect", "Data Security Officer", "IT Specialist", 
                    "Security Engineer", "Software Developer", "Network Engineer", 
                    "Data Analyst", "Project Manager", "Consultant", "System Administrator"]
    
    company_names = ["TechCorp Inc.", "Retail Solutions", "FinanceFirst", "Analytics Pro", 
                     "Manufacturing Plus", "SecureNet", "LegalEase", "HealthFirst", "RetailMart", 
                     "EduPlus", "Cloud Solutions", "DataGuard", "Office Solutions", "CyberSecure", 
                     "InfoDefense", "MedTech", "SecurePlus", "DataSafe", "NetSolutions", 
                     "AppSecure", "GlobalTech", "Innovate Inc.", "Summit Solutions", 
                     "Peak Performance", "Alpha Dynamics", "Beta Innovations", "Gamma Enterprises", 
                     "Delta Systems", "Epsilon Technologies", "Zeta Solutions"]
    
    industries = ["Technology", "Retail", "Financial Services", "Consulting", "Manufacturing", 
                  "Legal", "Healthcare", "Education", "Government", "Non-profit"]
    
    lead_sources = ["Website", "Trade Show", "Referral", "LinkedIn", "Email Campaign", 
                    "Webinar", "Social Media", "Partner", "Direct Mail", "Event"]
    
    # TODO Check these status scope w/ joe
    statuses = ["New", "Contacted", "Qualified", "Proposal Sent", "Closed Won", "Closed Lost"]

    ratings = ["Hot", "Warm", "Cold"]
    
    owner_ids = [f"USER-{i:03}" for i in range(1, 21)]  # Example: USER-001, USER-002, USER-003 - 20 users, might wanna edit this later

    data = []
    for i in range(1, num_records + 1):
        lead_id = f"LEAD-{i:03}"
        topic = random.choice(topics)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        job_title = random.choice(job_titles)
        company_name = random.choice(company_names)
        email = f"{first_name}.{last_name.lower()}@{company_name.lower().replace(' ', '')}.com"

        # ? Note that phone numbers are not Singaporean numbers
        phone = f"+1-555-{random.randint(100, 999):04}"

        industry = random.choice(industries)
        lead_source = random.choice(lead_sources)
        status = random.choice(statuses)
        rating = random.choice(ratings)

        # ? Note that we might need to adjust the value for estimated values
        estimated_value = random.randint(25000, 250000)

        # TODO check if there are instances where the estimated close date is before the created date (for the rest too)
        estimated_close_date = (datetime.now() + timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d")
        created_on = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        modified_on = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        owner_id = random.choice(owner_ids)

        data.append([lead_id, topic, first_name, last_name, job_title, company_name, email, phone, 
                     industry, lead_source, status, rating, estimated_value, estimated_close_date, 
                     created_on, modified_on, owner_id])
    return data

## * 2. Opportunity

def generate_opportunity_data(num_records=100, lead_ids=None):
    """Generates realistic opportunity data.

    Args:
        num_records (int): The number of opportunity records to generate.
        lead_ids (list, optional): A list of LeadIDs to associate with the opportunities.
                                   If None, random LeadIDs will be generated.

    Returns:
        list: A list of lists, where each inner list represents an opportunity record.
    """

    stages = ["Discovery", "Qualification", "Proposal", "Negotiation", "Closed"]

    # TODO: seems like there is a need to define the probabilities
    probabilities = random.randint(0, 100) # probabilities currently to between 0 and 1, can be modified accordingly

    statuses = ["Open", "Won", "Lost"]
    descriptions = [
        "Complete ERP system implementation including training",
        "AWS cloud migration with disaster recovery setup",
        "Comprehensive security audit and compliance review",
        "Custom analytics platform with ML capabilities",
        "End-to-end digital transformation consulting",
        "Penetration testing and vulnerability assessment",
        "Security awareness training for employees",
        "Incident response and recovery planning",
        "Data encryption and security solutions",
        "Network security architecture design",
    ]

    names = [
        "ERP Implementation - TechCorp",
        "Cloud Migration Project",
        "Security Audit Services",
        "Analytics Platform Development",
        "Digital Transformation Strategy",
        "Vulnerability Management & Penetration Testing Services",
        "Security Awareness Training Program",
        "ncident Response Planning & Recovery Services",
        "Data Encryption & Security Solutions Implementation",
        "Network Security Architecture Design & Implementation"
    ]
    owner_ids = [f"USER-{i:03}" for i in range(1, 4)]  # Example: USER-001, USER-002, USER-003

    if lead_ids is None:
        lead_ids = [f"LEAD-{i:03}" for i in range(1, num_records + 1)]

    data = []
    for i in range(1, num_records + 1):
        opportunity_id = f"OPP-{i:03}"

        # ! need to define the name here: will be random.choice
        name = random.choice(names)

        # * what in the world is an account id - and is it a problem if this is tagged directly 
        # * to opportunity id in a running manner?
        account_id = f"ACC-{i:03}"
        
        lead_id = random.choice(lead_ids)
        stage = random.choice(stages)
        probability = random.choice(probabilities)

        # ? Note that we might need to adjust the value for estimated values        
        estimated_value = random.randint(25000, 250000)

        # TODO check same thing as above
        expected_close_date = (datetime.now() + timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d")
        actual_close_date = ""  # Leave blank for Open opportunities
        if stage == "Closed":
            actual_close_date = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        status = random.choice(statuses) if stage == "Closed" else "Open"
        description = random.choice(descriptions)
        owner_id = random.choice(owner_ids)

        # todo same problem for earlier
        created_on = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        modified_on = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

        data.append([opportunity_id, name, account_id, lead_id, stage, probability, 
                     estimated_value, expected_close_date, actual_close_date, status, 
                     description, owner_id, created_on, modified_on])
    return data
    
## * 3. Quote

def generate_quote_data(num_records=100, opportunity_ids=None, account_ids=None):
    """Generates realistic quote data."""

    statuses = ["Draft", "Sent", "Accepted", "Rejected"]

    descriptions = [
        "ERP implementation services and licenses",
        "Cloud migration and setup services",
        "Security audit and compliance services",
        "Analytics platform development",
        "Digital transformation consulting services",
        "Penetration testing and vulnerability assessment",
        "Security awareness training for employees",
        "Incident response and recovery planning",
        "Data encryption and security solutions",
        "Network security architecture design",
    ]

    names = {
        "ERP Implementation Quote",
        "Cloud Migration Quote",
        "Security Audit Quote",
        "Analytics Platform Quote",
        "Digital Transformation Quote",
        "Penetration Testing Quote",
        "Security Awareness Quote",
        "Incident Response Quote",
        "Data Encryption Quote",
        "Network Security Quote"
    }

    if opportunity_ids is None:
        opportunity_ids = [f"OPP-{i:03}" for i in range(1, num_records + 1)]

    if account_ids is None:
        account_ids = [f"ACC-{i:03}" for i in range(1, num_records + 1)]

    data = []

    for i in range(1, num_records + 1):
        quote_id = f"QUO-{i:03}"
        opportunity_id = random.choice(opportunity_ids)

        # ! check this name  // yes it's wrong we need to change this - examples include 
        # ! "ERP implementation etc" -- need to random choice this 
        name = f"Quote-{i:03}"  # Generic name, can be made more descriptive

        account_id = random.choice(account_ids)
        quote_number = f"Q{datetime.now().year}-{i:03}"
        status = random.choice(statuses)
        valid_from = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        valid_to = (datetime.now() + timedelta(days=random.randint(30, 90))).strftime("%Y-%m-%d")
        total_amount = random.randint(50000, 300000)
        discount_percentage = round(random.uniform(0, 20), 2)  # Up to 20% discount
        discount_amount = round(total_amount * (discount_percentage / 100), 2)
        final_amount = round(total_amount - discount_amount, 2)
        description = random.choice(descriptions)
        created_on = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        modified_on = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

        data.append([quote_id, opportunity_id, name, account_id, quote_number, status, 
                     valid_from, valid_to, total_amount, discount_percentage, discount_amount, 
                     final_amount, description, created_on, modified_on])
    return data

## * 4. Contact 

def generate_contract_data(num_records=100, quote_ids=None, account_ids=None):
    """Generates realistic contract data."""

    statuses = ["Draft", "Pending", "Active", "Terminated", "Expired"]
    billing_frequencies = ["Monthly", "Quarterly", "Annually"]
    payment_terms = ["Net 30", "Net 45", "Net 60"]
    descriptions = [
        "Security audit and compliance services contract",
        "ERP implementation contract",
        "Cloud migration services contract",
        "Analytics platform development contract",
        "Digital transformation consulting contract",
        "Penetration testing and vulnerability assessment contract",
        "Security awareness training contract",
        "Incident response contract",
        "Data encryption contract",
        "Network security contract",
    ]

    if quote_ids is None:
        quote_ids = [f"QUO-{i:03}" for i in range(1, num_records + 1)]

    if account_ids is None:
        account_ids = [f"ACC-{i:03}" for i in range(1, num_records + 1)]

    data = []
    for i in range(1, num_records + 1):
        contract_id = f"CON-{i:03}"
        quote_id = random.choice(quote_ids)
        account_id = random.choice(account_ids)
        contract_number = f"C{datetime.now().year}-{i:03}"
        status = random.choice(statuses)
        start_date = (datetime.now() + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        end_date = (datetime.now() + timedelta(days=random.randint(365, 730))).strftime("%Y-%m-%d") # 1 to 2 years
        total_value = random.randint(50000, 300000)
        billing_frequency = random.choice(billing_frequencies)
        payment_terms = random.choice(payment_terms)
        description = random.choice(descriptions)
        created_on = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        modified_on = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

        data.append([contract_id, quote_id, account_id, contract_number, status, start_date, end_date, total_value, billing_frequency, payment_terms, description, created_on, modified_on])
    return data

## * 5. Milestones

def generate_milestone_data(num_records=100, contract_ids=None):
    """Generates realistic contract milestone data."""

    statuses = ["Planned", "In Progress", "Completed", "Delayed"]
    descriptions = [
        "Security infrastructure assessment completion",
        "Regulatory compliance review completion",
        "Final security audit report delivery",
        "ERP requirements documentation",
        "ERP system setup and configuration",
        "Cloud platform setup",
        "Data migration completion",
        "User training",
        "System go-live",
        "Post-implementation support",
    ]

    if contract_ids is None:
        contract_ids = [f"CON-{i:03}" for i in range(1, num_records + 1)]

    data = []
    for i in range(1, num_records + 1):
        milestone_id = f"MIL-{i:03}"
        contract_id = random.choice(contract_ids)

        # ! need to define the name here
        name = f"Milestone-{i:03}"  # Generic name, can be made more descriptive ! pretty sure this is wrong
        description = random.choice(descriptions)
        due_date = (datetime.now() + timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d")
        amount = round(random.uniform(10000, 100000), 2)  # Vary milestone amounts
        status = random.choice(statuses)
        completion_date = ""
        if status == "Completed":
            completion_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        invoice_id = f"INV-{i:03}" if status == "Completed" or random.random() < 0.5 else "" # some milestones might not have invoice yet
        created_on = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        modified_on = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

        data.append([milestone_id, contract_id, name, description, due_date, amount, 
                     status, completion_date, invoice_id, created_on, modified_on])
    return data

## * 6. Project

def generate_project_data(num_records=100, contract_ids=None):
    """Generates realistic project data."""

    statuses = ["Not Started", "Planning", "In Progress", "Completed", "Delayed", "On Hold"]
    descriptions = [
        "Comprehensive security audit project",
        "ERP system implementation project",
        "Cloud infrastructure migration project",
        "Custom analytics solution development",
        "Manufacturing digital transformation",
        "Penetration testing and vulnerability assessment project",
        "Security awareness training project",
        "Incident response and recovery planning project",
        "Data encryption implementation project",
        "Network security upgrade project",
    ]
    project_managers = [f"USER-{i:03}" for i in range(1, 6)]  # Example Project Managers

    if contract_ids is None:
        contract_ids = [f"CON-{i:03}" for i in range(1, num_records + 1)]

    data = []
    for i in range(1, num_records + 1):
        project_id = f"PRJ-{i:03}"
        contract_id = random.choice(contract_ids)

        # ! need to define the name here
        name = f"Project-{i:03}"  # Generic name, can be made more descriptive
        description = random.choice(descriptions)
        start_date = (datetime.now() + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        end_date = (datetime.now() + timedelta(days=random.randint(90, 365))).strftime("%Y-%m-%d")  # At least 3 months duration
        status = random.choice(statuses)
        project_manager = random.choice(project_managers)
        budget = random.randint(50000, 300000)
        actual_cost = random.randint(0, budget) if status != "Not Started" else 0 # Actual cost cannot be more than budget
        progress = random.randint(0, 100) if status != "Not Started" else 0
        risk = random.choice(["Low", "Medium", "High"])
        created_on = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        modified_on = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

        data.append([project_id, contract_id, name, description, start_date, end_date, 
                     status, project_manager, budget, actual_cost, progress, risk, 
                     created_on, modified_on])

    return data

## * 7. Invoice Data 

def generate_invoice_data(num_records=100, contract_ids=None, milestone_ids=None):
    """Generates realistic contract invoice data."""

    statuses = ["Draft", "Issued", "Paid", "Overdue", "Cancelled"]
    descriptions = [
        "Initial security assessment milestone",
        "Compliance review milestone",
        "Final security audit report delivery",
        "First quarter ERP implementation",
        "Monthly cloud migration services",
        "Analytics platform development",
        "Penetration testing services",
        "Security awareness training",
        "Incident response retainer",
        "Data encryption solution",
    ]

    if contract_ids is None:
        contract_ids = [f"CON-{i:03}" for i in range(1, num_records + 1)]

    if milestone_ids is None:
        milestone_ids = [f"MIL-{i:03}" for i in range(1, num_records + 1)]

    data = []
    for i in range(1, num_records + 1):
        invoice_id = f"INV-{i:03}"
        contract_id = random.choice(contract_ids)
        milestone_id = random.choice(milestone_ids) if random.random() < 0.7 else ""  # 70% chance of having a milestone
        invoice_number = f"INV{datetime.now().year}-{i:03}"
        status = random.choice(statuses)
        issue_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=random.randint(15, 45))).strftime("%Y-%m-%d")
        amount = round(random.uniform(1000, 50000), 2)
        paid_amount = 0
        paid_date = ""
        if status == "Paid":
            paid_amount = amount
            paid_date = (datetime.now() - timedelta(days=random.randint(0, 15))).strftime("%Y-%m-%d")
        description = random.choice(descriptions)
        created_on = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        modified_on = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

        data.append([invoice_id, contract_id, milestone_id, invoice_number, status, issue_date, due_date, amount, paid_amount, paid_date, description, created_on, modified_on])

    return data

## * 8. Timesheet

def generate_timesheet_data(num_records=100, project_ids=None):
    """Generates realistic approved timesheet data."""

    statuses = ["Approved", "Submitted", "Rejected"]  # You can add more statuses if needed
    employee_ids = [f"EMP-{i:03}" for i in range(1, 21)]  # Example Employee IDs
    approvers = [f"USER-{i:03}" for i in range(1, 6)]  # Example Approvers

    if project_ids is None:
        project_ids = [f"PRJ-{i:03}" for i in range(1, num_records + 1)]

    data = []
    for i in range(1, num_records + 1):
        timesheet_id = f"TS-{i:03}"
        project_id = random.choice(project_ids)
        employee_id = random.choice(employee_ids)
        week_start_date = (datetime.now() - timedelta(days=random.randint(7, 35))).strftime("%Y-%m-%d")  # Up to 5 weeks ago
        week_end_date = (datetime.strptime(week_start_date, "%Y-%m-%d") + timedelta(days=6)).strftime("%Y-%m-%d")
        status = random.choice(statuses)
        total_hours = random.randint(35, 45)  # Typical work hours
        billable_hours = random.randint(0, total_hours)
        non_billable_hours = total_hours - billable_hours
        approved_by = random.choice(approvers) if status == "Approved" else ""
        approval_date = (datetime.strptime(week_end_date, "%Y-%m-%d") + timedelta(days=random.randint(1, 3))).strftime("%Y-%m-%d") if status == "Approved" else ""
        comments = ""  # You can add random comments here if needed
        created_on = (datetime.strptime(week_end_date, "%Y-%m-%d") - timedelta(days=random.randint(0, 2))).strftime("%Y-%m-%d")
        modified_on = created_on if status!= "Approved" else approval_date

        data.append([timesheet_id, project_id, employee_id, week_start_date, week_end_date, 
                     status, total_hours, billable_hours, non_billable_hours, approved_by, 
                     approval_date, comments, created_on, modified_on])

    return data

def write_to_csv(data, filename, header):
    """Writes data to a CSV file with the given header."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)

# 1. Generate Lead Data
lead_data = generate_lead_data(100)
lead_ids = [row for row in lead_data]

# 2. Generate Opportunity Data
opportunity_data = generate_opportunity_data(100, lead_ids)
opportunity_ids = [row for row in opportunity_data]
account_ids = [row for row in opportunity_data]

# 3. Generate Quote Data
quote_data = generate_quote_data(100, opportunity_ids, account_ids)
quote_ids = [row for row in quote_data]

# 4. Generate Contract Data
contract_data = generate_contract_data(100, quote_ids, account_ids)
contract_ids = [row for row in contract_data]

# 5. Generate Milestone Data
milestone_data = generate_milestone_data(100, contract_ids)
milestone_ids = [row for row in milestone_data]

# 6. Generate Project Data
project_data = generate_project_data(100, contract_ids)
project_ids = [row for row in project_data]

# 7. Generate Invoice Data
invoice_data = generate_invoice_data(100, contract_ids, milestone_ids)

# 8. Generate Timesheet Data
timesheet_data = generate_timesheet_data(100, project_ids)

# --- Write data to CSV files ---
write_to_csv(lead_data, "leads_data.csv", ["LeadID", "Topic", "FirstName", "LastName", "JobTitle", "CompanyName", "Email", "Phone", "Industry", "LeadSource", "Status", "Rating", "EstimatedValue", "EstimatedCloseDate", "CreatedOn", "ModifiedOn", "OwnerID"])
write_to_csv(opportunity_data, "opportunities_data.csv", ["OpportunityID", "Name", "AccountID", "LeadID", "Stage", "Probability", "EstimatedValue", "ExpectedCloseDate", "ActualCloseDate", "Status", "Description", "OwnerID", "CreatedOn", "ModifiedOn"])
write_to_csv(quote_data, "quotes_data.csv", ["QuoteID", "OpportunityID", "Name", "AccountID", "QuoteNumber", "Status", "ValidFrom", "ValidTo", "TotalAmount", "DiscountPercentage", "DiscountAmount", "FinalAmount", "Description", "CreatedOn", "ModifiedOn"])
write_to_csv(contract_data, "contracts_data.csv", ["ContractID", "QuoteID", "AccountID", "ContractNumber", "Status", "StartDate", "EndDate", "TotalValue", "BillingFrequency", "PaymentTerms", "Description", "CreatedOn", "ModifiedOn"])
write_to_csv(milestone_data, "milestones_data.csv", ["MilestoneID", "ContractID", "Name", "Description", "DueDate", "Amount", "Status", "CompletionDate", "InvoiceID", "CreatedOn", "ModifiedOn"])
write_to_csv(project_data, "projects_data.csv", ["ProjectID", "ContractID", "Name", "Description", "StartDate", "EndDate", "Status", "ProjectManager", "Budget", "ActualCost", "Progress", "Risk", "CreatedOn", "ModifiedOn"])
write_to_csv(invoice_data, "invoices_data.csv", ["InvoiceID", "ContractID", "MilestoneID", "InvoiceNumber", "Status", "IssueDate", "DueDate", "Amount", "PaidAmount", "PaidDate", "Description", "CreatedOn", "ModifiedOn"])
write_to_csv(timesheet_data, "timesheets_data.csv", ["TimesheetID", "ProjectID", "EmployeeID", "WeekStartDate", "WeekEndDate", "Status", "TotalHours", "BillableHours", "NonBillableHours", "ApprovedBy", "ApprovalDate", "Comments", "CreatedOn", "ModifiedOn"])


print("All data generated and saved to CSV files.")

# 1. Generate Lead Data
lead_data = generate_lead_data(100)
lead_ids = [row for row in lead_data]

# 2. Generate Opportunity Data
opportunity_data = generate_opportunity_data(100, lead_ids)
opportunity_ids = [row for row in opportunity_data]
account_ids = [row for row in opportunity_data]

# 3. Generate Quote Data
quote_data = generate_quote_data(100, opportunity_ids, account_ids)
quote_ids = [row for row in quote_data]

# 4. Generate Contract Data
contract_data = generate_contract_data(100, quote_ids, account_ids)
contract_ids = [row for row in contract_data]

# 5. Generate Milestone Data
milestone_data = generate_milestone_data(100, contract_ids)
milestone_ids = [row for row in milestone_data]

# 6. Generate Project Data
project_data = generate_project_data(100, contract_ids)

# 7. Generate Invoice Data
invoice_data = generate_invoice_data(100, contract_ids, milestone_ids)


print(f"Generated {len(lead_data)} lead records.")
print(f"Generated {len(opportunity_data)} opportunity records.")
print(f"Generated {len(quote_data)} quote records.")
print(f"Generated {len(contract_data)} contract records.")
print(f"Generated {len(milestone_data)} milestone records.")
print(f"Generated {len(project_data)} project records.")
print(f"Generated {len(invoice_data)} invoice records.")

#... (Add more tables and generate data as needed.
#      When ready, write all data to separate CSV files.)

# 1. Generate Lead Data 
lead_data = generate_lead_data(100)
lead_ids = [row[0] for row in lead_data]

# 2. Generate Opportunity Data
opportunity_data = generate_opportunity_data(100, lead_ids)
opportunity_ids = [row[0] for row in opportunity_data]
account_ids = [row[2] for row in opportunity_data]

# 3. Generate Quote Data
quote_data = generate_quote_data(100, opportunity_ids, account_ids)
quote_ids = [row[0] for row in quote_data]

# 4. Generate Contract Data
contract_data = generate_contract_data(100, quote_ids, account_ids)
contract_ids = [row[0] for row in contract_data]

# 5. Generate Milestone Data
milestone_data = generate_milestone_data(100, contract_ids)

# 6. Generate Project Data
project_data = generate_project_data(100, contract_ids)


print(f"Generated {len(lead_data)} lead records.")
print(f"Generated {len(opportunity_data)} opportunity records.")
print(f"Generated {len(quote_data)} quote records.")
print(f"Generated {len(contract_data)} contract records.")
print(f"Generated {len(milestone_data)} milestone records.")
print(f"Generated {len(project_data)} project records.")

# ... (Add more tables and generate data as needed.
#      When ready, write all data to separate CSV files.)

# 1. Generate Lead Data and get Lead IDs
lead_data = generate_lead_data(100)
lead_ids = [row[0] for row in lead_data]

# 2. Generate Opportunity Data, linking to Lead IDs and get OpportunityIDs and AccountIDs
opportunity_data = generate_opportunity_data(100, lead_ids)
opportunity_ids = [row[0] for row in opportunity_data]
account_ids = [row[2] for row in opportunity_data]

# 3. Generate Quote Data, linking to OpportunityIDs and AccountIDs and get QuoteIDs
quote_data = generate_quote_data(100, opportunity_ids, account_ids)
quote_ids = [row[0] for row in quote_data]

# 4. Generate Contract Data, linking to QuoteIDs and AccountIDs and get ContractIDs
contract_data = generate_contract_data(100, quote_ids, account_ids)
contract_ids = [row[0] for row in contract_data]

# 5. Generate Milestone Data, linking to ContractIDs
milestone_data = generate_milestone_data(100, contract_ids)



print(f"Generated {len(lead_data)} lead records.")
print(f"Generated {len(opportunity_data)} opportunity records.")
print(f"Generated {len(quote_data)} quote records.")
print(f"Generated {len(contract_data)} contract records.")
print(f"Generated {len(milestone_data)} milestone records.")

# ... (Add more tables and generate data as needed.
#      When ready, write all data to separate CSV files.)

# 1. Generate Lead Data and get Lead IDs
lead_data = generate_lead_data(100)
lead_ids = [row[0] for row in lead_data]

# 2. Generate Opportunity Data, linking to Lead IDs and get OpportunityIDs and AccountIDs
opportunity_data = generate_opportunity_data(100, lead_ids)
opportunity_ids = [row[0] for row in opportunity_data]
account_ids = [row[2] for row in opportunity_data]

# 3. Generate Quote Data, linking to OpportunityIDs and AccountIDs and get QuoteIDs
quote_data = generate_quote_data(100, opportunity_ids, account_ids)
quote_ids = [row[0] for row in quote_data]

# 4. Generate Contract Data, linking to QuoteIDs and AccountIDs
contract_data = generate_contract_data(100, quote_ids, account_ids)


print(f"Generated {len(lead_data)} lead records.")
print(f"Generated {len(opportunity_data)} opportunity records.")
print(f"Generated {len(quote_data)} quote records.")
print(f"Generated {len(contract_data)} contract records.")

# ... (You can now add more tables and generate data as needed.
#      When ready, write all data to separate CSV files.)

# 1. Generate Lead Data and get Lead IDs
lead_data = generate_lead_data(100)
lead_ids = [row[0] for row in lead_data]  # Extract LeadIDs

# 2. Generate Opportunity Data, linking to Lead IDs and get OpportunityIDs and AccountIDs
opportunity_data = generate_opportunity_data(100, lead_ids)
opportunity_ids = [row[0] for row in opportunity_data]
account_ids = [row[2] for row in opportunity_data]

# 3. Generate Quote Data, linking to OpportunityIDs and AccountIDs
quote_data = generate_quote_data(100, opportunity_ids, account_ids)


# Now you have lead_data, opportunity_data, and quote_data in memory.
# You can add more tables and generate data for them similarly.
# When you're ready to write to CSV, use the write_to_csv function as before.

# Example of how to access the generated data:
# for quote in quote_data:
#     print(quote)

print(f"Generated {len(lead_data)} lead records.")
print(f"Generated {len(opportunity_data)} opportunity records.")
print(f"Generated {len(quote_data)} quote records.")
