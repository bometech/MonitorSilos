#FTP Library for Server protocol
from ftplib import FTP
#Time from the computer
from datetime import date
from datetime import datetime
#Date
today = date.today()
now = datetime.now()
#Concatenation date required format

f =  str(today.year)
mes = str(today.month)
f += '-'
mes = mes.rjust(2,"0")
f += mes
dia = str(today.day)
f += '-'
dia = dia.rjust(2, "0")
dia_anterior=int(dia)-1
f_anterior=(f+str(dia_anterior))
f += dia
#f='2021-07-13'

print('Archivo a importar: '+f+'.csv')
print('Conectando...')
#quit()

#Here we establish the credentials that are set for the PLC and the FTP Server.
host='192.168.1.247'
user='MyFTP'
password='Omron1234'

try:
    with FTP(host) as ftp:
        ftp.login(user=user, passwd=password)
        print(ftp.getwelcome())

        ftp.cwd('/MEMCARD1/HISTORIAL') #FTP Directory in which you might find the files writen on the SD Card
        ftp.retrbinary('RETR '+str(f)+'.csv', open('C:/DATAMonitor/data_um.csv','wb').write) #File that is read by the synchronizer
        ftp.retrbinary('RETR '+str(f)+'.csv', open('C:/DATAMonitor/HISTORIAL/'+f+'.csv','wb').write) #Backup writing on the Computer
        print('LISTO UM1')

        ftp.quit()
        print('OK')
except:
    print('Error al conectar con el servidor')
    quit()
