# -*- coding: utf-8 -*-

# Adicionar abaixo no crontab -e
# */30 * * * * /usr/bin/python2 /usr/src/cache.py
import os
from datetime import datetime
from time import sleep

# qual maximo em porcentagem de memoria para limpar
max_mem = 85

date = os.popen('date \'+%Y-%m-%d %H:%M\'').read().strip()
# Total da memoria:
ramtotal = int(os.popen('free | grep -i mem | awk \'{print $2}\'').read().strip())
# Memoria livre:
ramlivre = int(os.popen('free | grep -i mem | awk \'{print $4}\'').read().strip())
# Memoria utilizada
ramusada = ramtotal - ramlivre
# Porcentagem usada
porcentagem = int(ramusada * 100 / ramtotal)
if porcentagem <= max_mem:
    # Printa na tela que está OK caso queira fazer log descomentar os debaixo
    os.system('echo \'caches em {0}% {1}\' >> /tmp/logcaches.log'.format(porcentagem, date))
    # print('Memoria está em {0}%'.format(porcentagem))
    # os.system('echo \'caches em {0}% {1}\'  >> /tmp/logcaches.log'.format(porcentagem, date))
if porcentagem >= max_mem:
    os.system('echo \'limpando  caches {0} porcentagem de ram em {1}%\' >> /tmp/logcaches.log'.format(date, porcentagem))
    print('Memoria está em {0}%'.format(porcentagem))
    os.system('echo 3 > /proc/sys/vm/drop_caches')
    # Total da memoria:
    ramtotal = int(os.popen('free | grep -i mem | awk \'{print $2}\'').read().strip())
    # Memoria livre:
    ramlivre = int(os.popen('free | grep -i mem | awk \'{print $4}\'').read().strip())
    # Memoria utilizada
    ramusada = ramtotal - ramlivre
    # Porcentagem usada
    porcentagem = int(ramusada * 100 / ramtotal)
    os.system('swapoff -a')
    sleep(1)
    os.system('swapon -a')
    os.system('echo \'caches limpos {0} porcentagem de ram em {1}%\' >> /tmp/logcaches.log'.format(date, porcentagem))
    print('Cache limpo = {0}%'.format(porcentagem))
