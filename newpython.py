#!/usr/bin/env python3
import os
import requests
vinu = os.getenv("ServiceName")
print(vinu)

url_data = "http://omd.carrefour.es/c4omd/thruk/cgi-bin/status.cgi?view_mode=json&s0_op=%3D&s0_type=event+handler&s0_value=sf_restart&columns=host_name,description,event_handler,host_groups"
response = requests.get(url_data)

print(response)