import turtle
from PBYcor import linea, lineb, linec, lined, linee, linef

from PB100Parse import dates

def authenticate():
    tta = turtle
    tta.bgcolor('black')
    tta.up()
    tta.color('#3adF10')
    tta.goto(-593, 350)
    tta.write(dates[len(linea)])
    tta.goto(-112 , 350)
    tta.write("Powerball 100",font=('sans ',10,'bold','italic'))
    tta.goto(390,350)
    tta.write(dates[0])
    tta.ht

def draw(line, color):
    tds = 12   #    turtle dot size #
    tps = 2    #    turtle pen size #    
    xs = -590  #   x starting point #
    tt = turtle
    tt.title(dates[0])
    tt.bgcolor("black")
    tt.color(color,'black')
    tt.shape('circle')
    tt.pensize(tps)
    tt.up()
    tt.ht()
    i = 0
    x = xs

    for l in range(len(line)):
        x += 10
        y = line[i]
        tt.goto(x, y)                    
        tt.dot(tds)   
        
        if line==linef:
            tt.stamp()
        tt.down()
        i += 1
    
def main(line, color):
    authenticate()
    draw(linef, color = 'yellow')
    draw(linea, color = 'red')
    draw(lineb, color = '#5050FF')
    draw(linec, color = '#3adF10')
    draw(lined, color = '#cc00cc')
    draw(linee, color = 'orange')
    
    
main('line','color')
