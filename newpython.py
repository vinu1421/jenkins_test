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



print(ACTION)

print('//////////////')              

print(option)
                
        
        
    
    
    



