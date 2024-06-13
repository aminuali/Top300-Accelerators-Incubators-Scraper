# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 02:34:51 2024

Project 3: Scraping Top 300 Accelerators and Incubators in the US

Project Description:
    
    Scrape the following from the given website below for the Top 300 Accelerators and Incubators in the US:
      
    i.  company name
    ii. company website address
    iii. company details including: 
        city 
        year it was started
        founders
        industries
        number of investment
        funding amount 
        number of exits
        equity taken
        accelerator duration in weeks
        
        Website to scrape:"https://www.failory.com/startups/united-states-accelerators-incubators"
deliverables: 
    
    1. The python script and documentation on how to run it
    2.  A CSV or excel file containing the following for each company
        i. company name
        ii. company website address
        iii. company details including: 
            city 
            year it was started
            founders
            industries
            number of investment
            funding amount 
            number of exits
            equity taken
            accelerator duration in weeks
    
    
@author: Aminu Ali 
"""
#importing the necessary packages 

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data(url):
  """
  Extracts data from a website.

  Args:
      url (str): The URL of the website to scrape.

  Returns: 
      
      List containing all the top 300 Accelerators and Incubators companies in the US
      
  """

  # Make a request to the website and get the HTML content
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find all unordered lists
  uL = soup.find_all('ul')
  # Find all the company name
  comp_name = soup.find_all('h3')
  # Find all the website address in the p tag
  url = [p.find('a') for p in soup.find_all('p') if p.find('a')]
  #print(len(uL))
  # Initialize an empty list to store extracted data
  extracted_data = []

  # Loop through each unordered list
  for i, ul in enumerate(uL):
      # Create an empty dictionary to store data for each list item
      item_data = {}
            
      # Extract company_name from the corresponding h3 tag
      if i < len(comp_name):
          item_data['Company_Name'] = comp_name[i].text.strip()
          
       # Extract URL from the corresponding a tag
      if i < len(url) and url[i] is not None:
           item_data['URL'] = url[i]['href']    
     
          
    # Extract data from each list item (li)
      for li in ul.find_all('li'):
          text = li.text.strip().split(': ', 1)
          if len(text) == 2:
              # Extract field name and value
              field, value = text
              item_data[field] = value
    
             
      # Append the dictionary to the data list
      extracted_data.append(item_data)
 
           
  return extracted_data #end of extract_data function 

# the URL of the website to scrape
url = "https://www.failory.com/startups/united-states-accelerators-incubators" 

# call the extract data function to get and extract data from the given website
extracted_data = extract_data(url)

# Print the extracted data 

df = pd.DataFrame(extracted_data)

# Save the DataFrame to a CSV file
df.to_csv('EXFinal_Data.csv', index=False)

print("Data extracted and saved to extList.csv")

print(df.head())
