from googleapiclient.discovery import build
from config import SPREADSHEET_ID, SPREADSHEET_TAB, credentials


spreadsheet_service = build('sheets', 'v4', credentials=credentials)
drive_service = build('drive', 'v3', credentials=credentials)

def _read_range():
    read_range = f'{SPREADSHEET_TAB}!A:D'
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID, range=read_range).execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))
    return rows


def append_range(row):
    new_row_id = len(_read_range()) + 1
    add_range = f'{SPREADSHEET_TAB}!A{new_row_id}:D{new_row_id}'
    body = {
        'values': [row]
    }
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=add_range,
        valueInputOption='USER_ENTERED', body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))
    
