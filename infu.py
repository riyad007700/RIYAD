import requests
import json,os
os.system("clear")
number = str(input(" Enter Robi/Airtel Number : "))
url = "http://api.cybersh.xyz/siminfo.php?key=FREE&number="+number
print(" Please wait...")
response = requests.post(url).text
json_object = json.loads(response) 
info = json.dumps(json_object, indent=1)
os.system("clear")
print(info)