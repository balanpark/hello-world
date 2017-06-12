import re
from pwrballRead import pwrline

linez = re.findall('<time datetime=\\\(.*?)</span>',pwrline)
liney = ' '.join(linez)
days = re.findall('[A-Z][a-z]{2}', liney)
year = re.findall('[0-9]{4}',liney)
dates = re.findall('[0-9]{4}[-0-9]{3}[-0-9]{3}',liney)

linex = re.findall('(<li>)(.*?)</li>',pwrline)
linew = str(linex)
linexx= re.findall('Powerball</a>(.*?)<a href ="http:',linew)
linev = str(linexx)
lineu = re.findall('[\d]{1,2}',linev)
numbers = lineu
pwrball = re.findall('<li class="bonus powerball">(.*?)<span>', pwrline)
draws = 101 ## Line length for PowerballLines ##


def tickets():
    n = numbers
    nm= pwrball
    m = 0
    l = 0
    k = 1
    j = 2
    i = 3
    h = 4    
        
    for this in range(draws):        
        draw = ("{:>3}:{:>3} {:>2} {:>2} {:>2} {:>2} {:>4} ".format(this,n[l],n[k],n[j],n[i],n[h],nm[m]))
                    
        m += 1
        l += 5
        k += 5
        j += 5
        i += 5
        h += 5        
        print(draw)

        
def Mainline():
    mash = numbers
    load = mash 
    g = 0
    f = 1
    e = 2
    d = 3
    c = 4
    
    linea = []
    lineb = []
    linec = []
    lined = []
    linee = []

     
    for lineation in range(draws): 
        linea.append(load[g])  # first hit on ticket
        lineb.append(load[f])  #second
        linec.append(load[e])
        lined.append(load[d])
        linee.append(load[c])
        
        g += 5
        f += 5
        e += 5
        d += 5
        c += 5

        mainline = linea,  lineb,  linec,  lined,  linee
        
    return mainline

def Powerline(): # powerball seperate in source
    x = 0
    powerline = []   
    for pb in range(draws):
        powerline.append(pwrball[x])
        x += 1    
    return powerline
