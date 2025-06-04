<h2>Project Overview</h2>
This Customer Call List project focuses on data cleaning and preparation of raw customer data extracted from an Excel file. The dataset included inconsistencies, unwanted formatting, and missing values across various fields such as phone numbers, names, addresses, and contact preferences. Using Python and pandas, the project applies essential data wrangling techniques to transform this unstructured information into a clean, analysis-ready dataset, suitable for CRM use, marketing campaigns, or customer support workflows.

<br />

<h2>Key Features</h2>

- <strong>Duplicate Handling</strong>  
  Removed all duplicate records to ensure data integrity and avoid repeated outreach efforts.

- <strong>Column Pruning</strong>  
  Dropped non-essential columns (e.g., "Not_Useful_Column") to reduce noise and focus on relevant data.

- <strong>Last Name Cleanup</strong>  
  Cleansed the <code>Last_Name</code> column by stripping out unwanted characters such as numbers, slashes, and punctuation for consistency.

- <strong>Phone Number Standardization</strong>  
  Removed non-alphanumeric characters from the <code>Phone_Number</code> column, and cleaned malformed entries (e.g., <code>nan--</code>, <code>Na--</code>) to ensure uniform formatting.

- <strong>Address Splitting</strong>  
  Separated the full <code>Address</code> field into three distinct columns: <code>street_address</code>, <code>state</code>, and <code>zip_code</code> for better geolocation and segmentation.

- <strong>Boolean Field Normalization</strong>  
  Standardized values in <code>Paying Customer</code> and <code>Do_Not_Contact</code> fields using Y/N format and handled odd cases (e.g., <code>NNN</code>, <code>NYN</code>) to improve clarity in filtering.

- <strong>Row Filtering</strong>  
  Removed all rows where:
  - <code>Do_Not_Contact</code> was marked 'Y'
  - <code>Phone_Number</code> was missing after cleaning  
  This ensures only active, reachable customers remain in the dataset.

- <strong>Column Name Standardization</strong>  
  Renamed and reformatted column names using snake_case conventions (e.g., <code>CustomerId</code> → <code>customer_id</code>) for consistency and coding best practices.

<br />

<h2>Tech Stack</h2>

- Python (pandas) – Data cleaning, text manipulation, and transformation  
- Jupyter Notebook – Interactive coding and documentation  
- Microsoft Excel – Source data format  
- Regex – Pattern-based text cleanup

<br />

<h2>Why This Project?</h2>
This project simulates a real-world CRM data preparation workflow. Raw customer lists often contain inconsistencies, noise, and irrelevant data. Through this project, practical data cleaning methods are applied to prepare accurate and usable contact lists. The end goal is to enhance marketing efficiency, customer service effectiveness, and overall data quality. This cleaned dataset can now be easily integrated into dashboards, databases, or outreach platforms with confidence.

