
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Googlesheets:
    
    def main():
        
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        SAMPLE_SPREADSHEET_ID = '1UUgaSPF4iUeqm6ic8KvOfJfXl0lnSTl2E93adXhEKxQ'
        SAMPLE_RANGE_NAME = 'testlist!A1:E'

        id = []
        order = []
        pricerub = []
        order_date = []
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'creds.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return

            class Table:
                    for row in values:
                        #print('%s, %s, %s, %s' % (row[0], row[1], row[2], row[3]))
                        id.append(row[0])
                        order.append(row[1])
                        pricerub.append(row[2])
                        order_date.append(row[3])
                    #print(order_date)
        except HttpError as err:
            print(err)
            



