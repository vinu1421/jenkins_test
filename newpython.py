#!/usr/bin/env python3
import os
import json
import requests
from requests.auth import HTTPBasicAuth

environment = os.getenv("C4Environment").split()
EventHandler = os.getenv("EventHandler").split()
ServiceName = os.getenv("ServiceName").split()
option = os.getenv("EventHandlerAction")
omduser = 'omdguest'
omdpass = 'omdguest'

if option == 'Enable':
    ACTION="enable_svc_event_handler"
elif option == 'Disable':
    ACTION="disable_svc_event_handler"

print(environment)
print(ServiceName)

for eventhandlers in EventHandler:
    
    url_data = "http://omd.carrefour.es/c4omd/thruk/cgi-bin/status.cgi?view_mode=json&s0_op=%3D&s0_type=event+handler&s0_value=" + eventhandlers + "&columns=host_name,description,event_handler,host_groups"
    response = requests.get(url_data, verify=False, auth=HTTPBasicAuth(omduser, omdpass))
    json_data = json.loads(response.content)
    
    for data in json_data:
        
        hostgroup = data['host_groups'][0]
        description = data['description']
        hostname = data['host_name']
        
        if hostgroup in environment and description in ServiceName:
            
            print(hostgroup)
            print(description)
            print(hostname)
        else:
            print(error)
            
  
            
                
        
        
    
    
    



