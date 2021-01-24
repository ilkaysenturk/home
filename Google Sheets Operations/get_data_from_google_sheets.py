# importing the required libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('ProjectHouseDashboard-c8fce8f422c3.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
  

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

records_data = sheet_instance.get_all_records()

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
records_df=records_df.head()

# aggregation example on the data if needed
#runs = records_df.groupby(['col3'])['Col1'].count().reset_index()

# view the data
print(records_df)
