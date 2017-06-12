from PB100TQues import linez,liney,linex,linew,linev,lineu

class Ycor:
    def __init__(self):
        self.name = name
        
    def translate(self):
        count = len(linez)
        n = []
        y = []
        line = []
        for number in range(1,70):
            n.append(number)
        for ycor in range(-352, 358, 10):
            y.append(ycor)
        y.reverse()
        
        for que in range(count):
            p = self[que]            
            line.append(y[p-1])
        return line   
        
        

linea = Ycor.translate(linez)
lineb = Ycor.translate(liney)
linec = Ycor.translate(linex)
lined = Ycor.translate(linew)    
linee = Ycor.translate(linev)
linef = Ycor.translate(lineu)
