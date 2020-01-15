from __future__ import print_function

import requests
from googleapiclient.discovery import build

# 657435896205-o1k3g5qj8rud25ifidoclsk8bnt3jitb.apps.googleusercontent.com
# 9YAJHIY8NbdGTC5ER6ubmomo

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


# oauth2client.Credentials or
#       google.auth.credentials.Credentials, credentials to be used for
#       authentication.
#

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token.pickle', 'wb') as token:
    #         pickle.dump(creds, token)
    #
    # creds = Credentials()
    # service = build('drive', 'v3', credentials=creds)

    # flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', scopes=['profile', 'email'])

    from google.oauth2 import service_account



    # credentials = service_account.Credentials.from_service_account_file('service_account.json')
 #   credentials = service_account.Credentials.from_service_account_info(scinfo)

    scoped_credentials = credentials.with_scopes([
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/drive.appdata",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.metadata",
        "https://www.googleapis.com/auth/drive.metadata.readonly",
        "https://www.googleapis.com/auth/drive.photos.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/drive.scripts"
    ])
    # flow.run_local_server()
    # credentials = flow.credentials

    service = build('drive', 'v3', credentials=scoped_credentials)

    # Call the Drive v3 API

    # z = service.files().get(fileId="1zdc0YNWzY8LVnJn5EzTEy_Yt0GLMCiHoId796IQkkis").execute()

    # u = service.files().export(fileId="1a7lqY1dyPDtCt91j9PtiWKqrqXIxlULiwxOMPXIa-8I", mimeType="text/plain").execute()
    u = service.files().get(fileId="1a7lqY1dyPDtCt91j9PtiWKqrqXIxlULiwxOMPXIa-8I").execute()

    # https://docs.google.com/spreadsheets/d/1a7lqY1dyPDtCt91j9PtiWKqrqXIxlULiwxOMPXIa-8I/edit?usp=sharing

    # spreadsheetUrl = result['spreadsheetUrl']
    # exportUrl = re.sub("\/edit$", '/export', spreadsheetUrl)
    headers = {
        'Authorization': 'Bearer ' + scoped_credentials.token,
    }

    # params = {
    #     'format': 'csv',
    #     'gid': sheet['properties']['sheetId'],
    # }

    url = "https://docs.google.com/spreadsheets/d/1a7lqY1dyPDtCt91j9PtiWKqrqXIxlULiwxOMPXIa-8I/gviz/tq?tqx=out:csv"

    x = requests.get(url, headers=headers)

    # queryParams = urllib.parse.urlencode(params)
    # url = exportUrl + '?' + queryParams
    # response = requests.get(url, headers=headers)
    # filePath = '/tmp/foo-%s.csv' % (+ params['gid'])
    with open("test.csv", 'wb') as csvFile:
        csvFile.write(x.content)
    # results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    # items = results.get('files', [])
    #
    # if not items:
    #     print('No files found.')
    # else:
    #     print('Files:')
    #     for item in items:
    #         print(u'{0} ({1})'.format(item['name'], item['id']))


if __name__ == '__main__':
    main()
