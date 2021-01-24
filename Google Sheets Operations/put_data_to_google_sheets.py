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
file = client.open('House Dashboard')

sheet=file.add_worksheet(title='test_sheet',rows=20,cols=2)

sheet.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")
