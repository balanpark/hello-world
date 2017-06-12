import re
from PB100TQues import linez,liney,linex,linew,linev,lineu

class Stats():
    def __init__(self, name):
        self.name = name
        
    def Hot(line):
        a = 0            
        bucket= []        
        card = []
        box = []        
        std = sorted(line)
        cop = max(std)                    
        for hit in range(len(std)):
            box.append(std.pop())
            a += 1            
            if (len(std))>0:        
                if cop > max(std):                                         
                    quip = box[-1],a                                        
                    comment = " {:>2}{:>4}{:>2}x ".format(quip[0],'hit',quip[1])
                    bucket.append(comment)                                        
                    a = 0
                cop = max(std)            
            if len(std)==0:                 
                quip = box[-1],a                  
                comment = " {:>2}{:>4}{:>2}x ".format(quip[0],'hit',quip[1])
                bucket.append(comment)                        
                a = 0
                
        hot = Stats.hotnum(bucket)            
        avg = Stats.Average(line)
        span = Stats.span(line)        
        
        print("  Avg: {:>3}".format(avg))        
        print(" Orbit: {:>2}".format(len(bucket)))    
        print(" Range: {:>2}\n".format(span))
                
        for report in range(len(bucket)):                            
            quip = bucket[report]
            card.append(quip)
            card.reverse()
        for data in range(len(card)):
            print(card[data])    
            
    def Average(line):
        divisor = len(line)
        total= 0
        for tally in range(divisor):
            total = total+line[tally]         
        avg = total / divisor        
        return round(avg)

    def span(line):
        a = max(line)
        b = min(line)
        span = a-b
        return span
    
    def hotnum(line):
        hots=[]
        stubs=[]
        hits=[]
        nums=[]       
        counts=[]        
        str(line)

        for q in range(len(line)):
           quip = line[q]
           grab = re.findall("[\d]{1,2}",quip)           
           num = grab[0]
           nums.append(num)
           count = grab[1]
           counts.append(count)
           
        for h in range(len(counts)):
            hot = int(nums[h])
            hots.append(hot)
            hit = int(counts[h])           
            hits.append(hit)
        a = 0
        mx = max(hits)
        for x in range(len(line)):
            if hits[a]== mx:
                stub = "{:>3} hit {:>1}x".format(hots[a],hits[a])      
                print(stub)
            a += 1
        a = 0         

    def main(line):        
        lines = [linez,liney,linex,linew,linev,lineu]
        for names in range(len(lines)):
            
            if lines[names]==linez:                
                name = ' Red line'
                line = (linez)
                print(name)
                print(" Hot number\n")
                Stats.Hot(line)
                
            if lines[names]==liney:
                line = liney
                name = ' Blue line'                
                print(name)
                print(" Hot number\n")
                Stats.Hot(line)
                
            if lines[names]==linex:
                line = linex
                name = ' Green line'                
                print(name)
                print(" Hot number\n")
                Stats.Hot(line)

            if lines[names]==linew:
                line = linew
                name = ' Purple line'
                print(name)
                print(" Hot number\n")
                Stats.Hot(line)

            if lines[names]==linev:
                line = linev
                name = ' Orange line'
                print(name)
                print(" Hot number\n")
                Stats.Hot(line)
                
            if lines[names]==lineu:
                line = lineu
                name = ' Yellow line'
                print(name)
                print(" Hot number\n")
                Stats.Hot(line)
                
            print()
