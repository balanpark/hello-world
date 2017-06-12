import turtle
from PB100Lines import linea,lineb,linec,lined,linee,linef

class PBHGrid(object):
    def __init__(self, name):
        self.name = name

    def lmscribe(x, y, lnum):
        ttl = turtle
        ttl.bgcolor('black')
        ttl.up()
        ttl.goto(x, y)
        ttl.color('#00DDCC')
        ttl.write(lnum, move=True,align='right',font= ('Arial',8,'normal'))        
        ttl.color('#758293')          
        lead = 1
        for dots in range(lead):
            x += 10
            ttl.goto(x, y)
            ttl.dot(3)            

    def hscribe(x, y, lnum):
        hott = turtle
        hott.ht()
        off ='#759382'
        big = 10
        hott.color('#759382')
        hott.up()
        hott.goto(x, y)
        hott.dot(3)
        
        for dot in range(len(linea)):
            d = dot
            hott.goto(x, y)
            hott.dot(3)
            marker = linea, lineb, linec, lined, linee, linef
            
            for mark in range(len(marker)):
                line = marker[mark]
                if line == linea:
                    lit = '#000000'#EECACB'
                if line == lineb:
                    lit = '#000000'#CACBEE'
                if line == linec:
                    lit = '#000000'#CAEECA'
                if line == lined:
                    lit = '#000000'#EE68EE'
                if line == linee:
                    lit = '#000000'#EE8430'
                if line == linef:
                    lit = '#000000'#EEEE00'
                    
                lenl = len(line)
                if y == line[d]:
                    hott.color(lit)
                    hott.dot(big)
                    hott.color(off)
                    if d < lenl -2:
                        d += 1
                else:
                    pass
                
            hott.dot(3)
            x += 10
            
    def rmscribe(x, y, lnum):
        ttr = turtle
        ttr.color('#928180')
        ttr.ht()
        ttr.up()
        ttr.goto(x, y)
        ttr.dot(3)
        trail = 4 # number of dots in rmargin #
        for dots in range(trail):
            ttr.goto(x, y)
            x += 10
            ttr.dot(3)            
        ttr.color('#00CCCC')
        x += 4
        ttr.goto(x, y)
        ttr.write(lnum,move=True, align='right',font=('Arial',8,'normal'))
    
    def lmargin(x, y, lnum):
        lnum = 0
        for lmar in range(69):
            y -= 10
            lnum += 1
            PBHGrid.lmscribe(x, y, lnum)
            
    def hotgrid(x, y, lnum):
        lnum = 0
        for hg in range(69):
            y -= 10
            lnum += 1
            PBHGrid.hscribe(x, y, lnum)
            
    def rmargin(x, y, lnum):
        lnum = 0
        for mar in range(69):
            y -= 10
            lnum += 1
            PBHGrid.rmscribe(x, y, lnum)
            
    def main(x, y, lnum):
        PBHGrid.lmargin(-600, 358,1)
        PBHGrid.hotgrid(-580, 358,1)
        PBHGrid.rmargin( 420, 358,1)
        
PBHGrid.main(0,0,0)
