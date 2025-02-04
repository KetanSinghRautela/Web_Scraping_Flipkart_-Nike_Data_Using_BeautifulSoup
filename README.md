# Web Scraping Flipkart Nike Data Using BeautifulSoup
## Workflow for Scraping Mobile Data from Flipkart
###  Import Necessary Libraries

- Requests: For sending HTTP requests to access the web pages.
- BeautifulSoup: For parsing HTML content and extracting data.
- Pandas: For organizing the scraped data into a structured format (DataFrame) and saving it as a CSV file.

###  Initialize Data Lists
#### Create empty lists to store the scraped data:
- Product_name: To hold product names.
- Prices: To hold product prices.
- Description: To hold product descriptions.
- Reviews: To hold product reviews.
  
### Send HTTP Request and Parse HTML

- For each page, send a GET request to the URL.
- Use BeautifulSoup to parse the HTML response.
### Locate Main Container 
 Identify the main container that holds the product listings using specific HTML classes.
### Extract Product Information:
- Product Names: Find and extract the names of the products.
- Prices: Locate and extract the prices of the products.
- Descriptions: Retrieve descriptions of the products.
- Reviews: Collect user reviews for the products.
### Store Extracted Data 
Append the extracted information to the respective lists created in step 2.
### Compile Data into a Structured Format
Organize the collected data into a dictionary or DataFrame, ensuring each attribute aligns correctly (e.g., names with their corresponding prices).
### Display the Data
Print the compiled data for review and verification.
### Export to CSV
 Save the structured data into a CSV file for future analysis and reference.<br><br><br><br>
## Workflow for Scraping Nike Air Jordan Shoes Data
### Import Libraries 
Begin by importing the necessary libraries for web scraping 
- (requests)
- HTML parsing (BeautifulSoup)
- Data manipulation (pandas).
### Initialize Data Structures
Create empty lists to store product-
- names
- prices
- images.
### Define the Target URL
Specify the URL for the Nike website's search results for "Air Jordan shoes.
### Send HTTP Request
Use the requests library to send a GET request to the specified URL to retrieve the HTML content.
### Parse HTML Content
Utilize BeautifulSoup to parse the retrieved HTML, preparing it for data extraction.
### Extract Product Names
- Locate all elements containing product names using the appropriate HTML class names.
- Append each extracted product name to the Product_Name list.
### Extract Prices
- Find all elements containing product prices using the relevant HTML class names.
- Append each extracted price to the Prices list.
### Compile Data into a DataFrame
Create a pandas DataFrame to organize the extracted product names and prices into a structured format.
### Display the DataFrame
Print the DataFrame to review the collected data, checking the number of products scraped.
### Export to CSV 
Save the DataFrame containing product names and prices to a CSV file for future use.<br><br>
#### ** (I have not explicitly performed any data cleanup operations.)


