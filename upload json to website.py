import os
from ftplib import FTP
from datetime import datetime

CRED = '\033[41m'
CPUR = '\33[45m'
CBLU = '\33[44m'
CEND = '\033[0m'
Filename = '<filename>.json'
PathToJson = 'C:/<pathToJsonFile>/' + Filename

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def changed():
    lastUpdate = os.path.getmtime(PathToJson)
    date_time = datetime.fromtimestamp(lastUpdate)
    now = datetime.now()
    print ('JSON File Last Updated: ' + CPUR + date_time.strftime("%d/%m/%Y %H:%M:%S") + CEND)
    print ('Current time is:        ' + CBLU + now.strftime("%d/%m/%Y %H:%M:%S") + CEND)
    print ("")

cls()
changed()

print ('Connecting to server...') 
ftp = FTP('<domain>','<username>','<password>')
# ftp.cwd("/incoming") If you need to change the folder, use change working directory (cwd)
print ('Uploading json file...')
file=open(PathToJson, 'rb')
ftp.storbinary('STOR ' + Filename, file)
print ('Closing connection...')
ftp.quit()
print ('Done.')
print ('')
now = datetime.now()
lastRun = now.strftime("%d/%m/%Y - %H:%M:%S")
print("Process Completed :", lastRun)
print ('')