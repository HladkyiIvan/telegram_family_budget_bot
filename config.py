from google.oauth2 import service_account
from google.cloud import secretmanager

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/cloud-platform'
]
credentials = service_account.Credentials.from_service_account_file('./mysite/service_account_credentials.json', scopes=SCOPES)
client = secretmanager.SecretManagerServiceClient(credentials=credentials)

BOT_TOKEN = client.access_secret_version(
    request={"name": 'projects/301143842980/secrets/telegram_family_budget_bot_token/versions/latest'}).payload.data.decode("UTF-8")

SPREADSHEET_ID = '1i965cdo9DVydbbCKsxZowLXJ57BqZ30GHQpC9FsMggM'
SPREADSHEET_TAB = 'Spendings Pool'
