import socket
from datetime import datetime
import netifaces as ni
from requests import get

now = datetime.now()

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        list_ip = ""
        for x in ni.interfaces():
            ip = ni.ifaddresses(x)[ni.AF_INET][0]['addr']
            list_ip += "\n" + x + ": " + ip
        ip = get('https://api.ipify.org').text
        indirizzi_IP = "Hostname: "+str(host_name)+"\nDevice's IP: "+list_ip+"\nPublic IP: {}".format(ip)+"\nActual date and time: "+str(dt_string)
        print (indirizzi_IP)

    except Exception as err:
        print("Error: ", err)

get_Host_name_IP()
