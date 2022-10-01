import requests
import json
import concurrent.futures 

founds = []


headers =  {
    "authorization": "Bearer Twitter has no validtion loool",
    "x-guest-token": "Twitter has no validtion loool",
}

def look(username):
    r = requests.get("https://twitter.com/i/api/i/users/username_available.json?username={}".format(username) , headers=headers)
    if r.json()['valid']:
        print('Valid' , username)
        founds.append(username)
    else:
        print('Invalid' , username , r.json())
        
to_be_sure = set()
    
names = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt').text.splitlines()
for line in names:
    to_be_sure.add(line.strip())

with concurrent.futures.ThreadPoolExecutor(max_workers=25) as pool:
    pool.map(look , to_be_sure)

print('Done ..')

with open('users.txt' , 'w') as x:
    for line in founds:
        x.write('\n')
        x.write(line)

