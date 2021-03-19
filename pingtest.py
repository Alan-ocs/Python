import os
import csv
import subprocess
import socket
from datetime import datetime

name = {}
CI = {}
hostname = {}
status = {}
username = {}
today = {}

with open('Output1.csv', 'r', newline='') as csvinput:
    reader = csv.DictReader(csvinput)

    for rows in reader:
        today = datetime.now()
        CI = rows['CI_Name']
        try:
            ip = socket.gethostbyname(CI)
        except socket.error:
            pass
        name = socket.getfqdn(CI)
        data = name

        hostname = rows['CI_Name']
        response = subprocess.Popen(['ping.exe',hostname], stdout = subprocess.PIPE).communicate()[0]
        response = response.decode()
        print(response)
        if 'bytes=32' in response:
            status = 'Up'
            username = subprocess.Popen(['powershell.exe','Get-WmiObject -class Win32_ComputerSystem -computername {} | Format-List Username'.format(hostname)], stdout = subprocess.PIPE).communicate()[0]
            username = username.decode().strip()
            if 'Get-WmiObject : The RPC server is unavailable.' in username:
                username = 'unavailable'
        elif 'destination host unreachable' in response:
            status = 'Unreachable'
            username = 'User Not Found'
        else:
            status = 'Down'
            username = 'User Not Found'
        if status == 'Down':
            ip = 'Not Found'
            username = 'User Not Found'
        with open('Output Final.csv', 'a', newline='') as csvoutput:
            output = csv.writer(csvoutput)
            output.writerow([hostname] + [status] + [ip] + [username] + [today])
