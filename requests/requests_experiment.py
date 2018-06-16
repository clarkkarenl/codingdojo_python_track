# Assignment: Requests (Optional)
# Karen Clark
# 2018-06-15

import requests

base_url = 'https://api.github.com'
events_endpoint = '/events/public'
users_endpoint = '/users'
commit_list = []

r = requests.get(base_url + users_endpoint + '/clarkkarenl' + events_endpoint)

for i in r.json():
    if i['type'] == 'PushEvent':
        for c in i['payload']['commits']:  
            info = {}
            info['sha'] = c['sha']
            info['msg'] = c['message']
            commit_list.append(info)

for i in range(0, 10):
    print commit_list[i]