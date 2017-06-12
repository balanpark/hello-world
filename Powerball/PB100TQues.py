import re
from PB100Parse import Mainline, Powerline

lineq = Mainline()
linea = lineq[0]
lineb = lineq[1]
linec = lineq[2]
lined = lineq[3]
linee = lineq[4]
linef = Powerline()

i = 0
linez = []
for i in range(len(linea)):
    linez.append(int(linea[i]))
    i += 1
linez.reverse()

    
i = 0
liney = []
for i in range(len(lineb)):
    liney.append(int(lineb[i]))
    i += 1
liney.reverse()
    
i = 0
linex = []
for i in range(len(linec)):
    linex.append(int(linec[i]))
    i += 1
linex.reverse()
    
i = 0
linew = []
for i in range(len(lined)):
    linew.append(int(lined[i]))
    i += 1
linew.reverse()
    
i = 0
linev = []
for i in range(len(linee)):
    linev.append(int(linee[i]))
    i += 1
linev.reverse()
    
i = 0
lineu = []
for i in range(len(linef)):
    lineu.append(int(linef[i]))
    i += 1
lineu.reverse()

import PBstats
PBstats.Stats.main(linez)
