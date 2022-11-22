import requests
import re

############### Change Me
domain = 'NA'
api_key = 'NA'
api_username = 'NA'
###############


url = 'https://api.domaintools.com/v1/{}/whois/history/?api_username={}&api_key={}'.format(domain,api_username,api_key)

#rgx = r'(?:\.?)([\w\-_+#~!$&\'\.]+(?<!\.)(@|[ ]?\(?[ ]?(at|AT)[ ]?\)?[ ]?)(?<!\.)[\w]+[\w\-\.]*\.[a-zA-Z-]{2,3})(?:[^\w])'

r = requests.get(url=url, verify=True)
final_email = set()
if r:
    for history in r.json()['response']['history']:
        history_date = history['date']
        raw_data = history['whois']['record']

        match = re.findall(r'[\w\.-]+@[\w\.-]+', raw_data)
        myset = set(match)
        print("%s\t%s" %(history_date, ', '.join(myset)))

        final_email.update(myset)
        #print(history_date)
        #print(','.join(myset))
        #print('-----------')

#    match = re.findall(r'[\w\.-]+@[\w\.-]+', r.text)
#    myset = set(match)
#    print(myset)
else:
    print("Bad call!! %s" %(r.status_code))

print('Final List\t %s' %(', '.join(final_email)))