def mail_fetch():
    # -*- coding: utf-8 -*-
    import scrapy
    import pandas as pd
    import os
    import re
    import csv
    import time
    import shutil

    print("Step 1 - Backup")
    ### MAKE BACKUPS ###
    now = time.time()
    if os.path.exists('output.csv'):
        shutil.copy('output.csv','backups/output_bkp'+str(now)+'.csv')
        
    if os.path.exists('listings.csv'):
         shutil.copy('listings.csv','backups/listings_bkp'+str(now)+'.csv')
    
    #### BACKUP MADE ###
    print("Step 1 - Backup DONE !!!")

    ############### FETCH UNREAD MAILS ###################     
    
    print("Step 2A - Importing libraries")
    import pickle
    import os.path
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from apiclient import errors
    import base64
    import re
    import csv
    print("Step 2A - Importing libraries DONE !!!")
    
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']
    print("Step 2B - Scope Defined")
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    print("Step 2C - Build Service ")
    service = build('gmail', 'v1', credentials=creds,cache_discovery=False)
    service.users().getProfile(userId='me').execute()
    print("Step 2C - Build Service DONE !!!")
    
    print("Step 2D - Reading mails ")
    try:
    
        msgs = service.users().messages().list(userId='me',labelIds=['UNREAD']).execute()
        message_snippet = []
        apple_watch = []
        flag=1
        inner_count = 0
        outer_count = 0
        
        while flag==1:
            if 'nextPageToken' in msgs.keys():
                print("Token",msgs['nextPageToken'])
            for i in range(0,len(msgs['messages'])):
                message = service.users().messages().get(userId='me', id=msgs['messages'][i]['id']).execute()
                if "Watch" in message['snippet']:
                    apple_watch.append(message['snippet'])
                else:
                    message_snippet.append(message['snippet'])
                message = service.users().messages().modify(userId='me', id=msgs['messages'][i]['id'],body={"addLabelIds": ['Label_907301759563378805'], "removeLabelIds": ['UNREAD']}).execute()
                inner_count+=1
            outer_count+=inner_count
            if 'nextPageToken' in msgs.keys():
                msgs = service.users().messages().list(userId='me',labelIds=['UNREAD'],pageToken= msgs['nextPageToken']).execute()
            else:
                flag=0
        print("Total Unread Messages",outer_count)
    
    except:
        print("Timed Out")
    print("Step 2D - Reading mails DONE !!!")
    
    listings = []
    for m in message_snippet:
        idx = m.find("View Listing")
        if re.findall(r'\D\D\D\D\d\d\d\d\d',m[idx+13:idx+22]):
            listings.append(str("https://swappa.com/listing/view/")+m[idx+13:idx+22])
    print("Total Listings Added to file",len(listings))
    
    listings_watch = []
    
    with open('listings.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(listings)
