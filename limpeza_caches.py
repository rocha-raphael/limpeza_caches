import os
from datetime import date, time
from time import sleep

#qual maximo em porcentagem de memoria para limpar
max_mem=85

date=os.popen('date \'+%Y-%m-%d %H:%M\'').read().strip()
# Total da memoria:
ramtotal=int(os.popen('free | grep -i mem | awk \'{print $2}\'').read().strip())
# Memoria livre:
ramlivre=int(os.popen('free | grep -i mem | awk \'{print $4}\'').read().strip())
#Memoria utilizada
ramusada=ramtotal-ramlivre
#Porcentagem usada
porcentagem=int(ramusada*100/ramtotal)
if porcentagem <= max_mem:
        #Printa na tela que está OK caso queira fazer log descomentar os debaixo
        os.system(f'echo \'caches em {porcentagem}% {date}\'')
        #print(f'Memoria está em {porcentagem}%')
        #os.system(f'echo \'caches em {porcentagem}% {date}\'  >> /tmp/logcaches.log')
if porcentagem >= max_mem:
        os.system(f'echo \'limpando  caches {date} porcentagem de ram em {porcentagem}%\' >> /tmp/logcaches.log')
        print(f'Memoria está em {porcentagem}%')
        os.system('echo 3 > /proc/sys/vm/drop_caches')
        # Total da memoria:
        ramtotal=int(os.popen('free | grep -i mem | awk \'{print $2}\'').read().strip())
        # Memoria livre:
        ramlivre=int(os.popen('free | grep -i mem | awk \'{print $4}\'').read().strip())
        #Memoria utilizada
        ramusada=ramtotal-ramlivre
        #Porcentagem usada
        porcentagem=int(ramusada*100/ramtotal)
        os.system('swapoff -a')
        sleep(1)
        os.system('swapon -a')
        os.system(f'echo \'caches limpos {date} porcentagem de ram em {porcentagem}%\' >> /tmp/logcaches.log')
        print(f'Cache limpo =  {porcentagem}%')
