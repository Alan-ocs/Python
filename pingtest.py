import os
import csv
import subprocess
import socket

name = {}
CI = {}
hostname = {}
status = {}
with open('Output1.csv', 'r', newline='') as csvinput:
    reader = csv.DictReader(csvinput)

    for rows in reader:
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
        elif 'destination host unreachable' in response:
            status = 'Unreachable'
        else:
            status = 'Down'
        if status == 'Down':
            ip = 'Not Found'
        with open('Output Final.csv', 'a', newline='') as csvoutput:
            output = csv.writer(csvoutput)
            output.writerow([hostname] + [data] + [status] + [ip])