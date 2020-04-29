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

print(environment)
print(EventHandler)
print(ServiceName)
print(option)
            
                
        
        
    
    
    



